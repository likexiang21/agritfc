# 299 野生蘑菇 P0-D 技术分析

> 日期：2026-10-28
> 目标：加入 15 种野生蘑菇方块、世界生成、随机刻刷新；4 种自然专用，不做菌包。
> 约束：不推送；不伪造；贴图暂时指向 TFC。

## 1. 范围

本轮实现：

- `MushroomSpecies` 15 条：
  - 可栽培候选 11：oyster · shiitake · button · enoki · wood_ear · reishi · lions_mane · maitake · king_oyster · shimeji · turkey_tail；
  - 自然专用 4：porcini · morel · chanterelle · black_truffle；
- 15 个 `wild_mushroom/<species>` 方块与 BlockItem；
- 15 个 wild blockstate/model/loot table；
- 15 组 configured/placed feature；
- 一个 `neoforge:add_features` biome modifier；
- 随机刻生长与局部扩散；自然专用 4 种同样只从野生刷新。

本轮**不实现**菌包（cultivation bag）；因此所有 15 种当前都只能从野生获得，自然专用 4 种未来也不能有菌包配方。

## 2. API 评估

`WildMushroomBlock extends BushBlock`：

- `codec()` 必须实现（BushBlock 的抽象方法，编译时实际踩到）；
- `AGE` 0..2；
- `mayPlaceOn` 接受：
  - `#minecraft:dirt` / grass / moss / podzol / mycelium；
  - TFC `#tfc:dirt` 与 `#tfc:grass`，否则 TFC 地形上无法生成/存活；
- `randomTick`：
  - 未成熟：概率长一龄；
  - 成熟：概率向附近 3×3 兼容土壤扩散 age=0；
- `isRandomlyTicking` 返回 true；
- 不使用 BE，不依赖客户端逻辑。

## 3. 世界生成

每种：

```text
worldgen/configured_feature/wild_mushroom_<species>.json
worldgen/placed_feature/wild_mushroom_<species>.json
```

放置：

- `count` 1–2；
- `in_square`；
- `MOTION_BLOCKING`；
- biome filter。

加入：

```text
data/tfcagricultureplus/tags/worldgen/biome/wild_mushroom_biomes.json
data/tfcagricultureplus/neoforge/biome_modifier/add_wild_mushrooms.json
```

biome tag 使用 `#minecraft:is_forest` / `#minecraft:is_taiga` / `#minecraft:is_swamp`。

## 4. 原型/校验

纯 Java：

```text
PASS: 134 crop P0 checks
```

资源校验：

```text
PASS: 99 item models, 2 lang files, 17 recipes, 82 crop_waste, 15 wild mushrooms, tags valid
```

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

## 5. 风险/未验证

- biome modifier/feature 配方**未实机验证**；
- 所有蘑菇使用同一个 TFC 临时贴图；
- 自然专用“禁止菌包”目前只体现为没有菌包系统；未来菌包实现时必须显式排除；
- 随机刷新只从已有成熟蘑菇扩散，不保证灭绝后重新出现；
- 没有真实世界生成密度调参。

## 6. 下一步

1. 实机验证 wild mushroom 生成/刷新；
2. 菌包系统，排除 4 种自然专用；
3. 自然专用 4 种的世界生成密度/林下限制；
4. TFC 29 完整覆盖；
5. 坚果叶状态。
