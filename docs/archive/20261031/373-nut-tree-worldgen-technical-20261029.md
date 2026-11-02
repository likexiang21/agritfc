# 373 坚果树立世界生成 P0-AQ 技术分析

> 日期：2026-10-29
> 目标：让 pistachio/cashew 树苗进入世界生成，而不是只能靠配方/树叶获得。
> 约束：不推送；不伪造；未实机。

## 1. 配置

每种树：

- configured feature：`minecraft:simple_block`，放置 `nut_sapling/<tree>` stage=0；
- placed feature：
  - count 1–2；
  - in_square；
  - heightmap MOTION_BLOCKING；
  - `would_survive` 过滤；
  - biome；
- biome modifier：`neoforge:add_features`，step `vegetal_decoration`。

复用现有：

```text
#tfcagricultureplus:wild_mushroom_biomes
```

作为群系标签，避免再定义一套。

## 2. 文件

```text
data/tfcagricultureplus/worldgen/configured_feature/nut_sapling_pistachio.json
data/tfcagricultureplus/worldgen/configured_feature/nut_sapling_cashew.json
data/tfcagricultureplus/worldgen/placed_feature/nut_sapling_pistachio.json
data/tfcagricultureplus/worldgen/placed_feature/nut_sapling_cashew.json
data/tfcagricultureplus/neoforge/biome_modifier/add_nut_saplings.json
```

## 3. 测试

```text
PASS: pistachio/cashew tree worldgen resources
gradle processResources
BUILD SUCCESSFUL
```

## 4. 风险

- 未实机；
- 复用蘑菇群系标签，分布可能过宽；
- `would_survive` 过滤是否符合 TFC 土壤未验证；
- 放置的是树苗，不是成树；
- 树苗生长依赖随机刻；
- 不能宣称坚果生态完成。
