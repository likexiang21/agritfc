# 379 香料树世界生成 P0-AT 技术分析

> 日期：2026-10-29
> 目标：让 5 个 tree form 香料树苗进入世界生成。
> 约束：不推送；不伪造；未实机。

## 1. 配置

每种树：

- configured feature：`minecraft:simple_block`；
- 放置 `spice_sapling/<spice>` stage=0；
- placed feature：
  - count 1–2；
  - in_square；
  - heightmap MOTION_BLOCKING；
  - `would_survive`；
  - biome；
- biome modifier：`neoforge:add_features`；
- step `vegetal_decoration`；
- 群系复用 `#tfcagricultureplus:wild_mushroom_biomes`。

## 2. 文件

```text
worldgen/configured_feature/spice_sapling_<5>.json
worldgen/placed_feature/spice_sapling_<5>.json
neoforge/biome_modifier/add_spice_trees.json
```

## 3. 测试

```text
PASS: spice tree worldgen resources
processResources BUILD SUCCESSFUL
PASS: 381 crop P0 checks
```

## 4. 风险

- 未实机；
- 群系标签复用可能过宽；
- 土壤过滤未验证；
- 只生成树苗，不生成成树；
- 树苗生长依赖随机刻；
- 香料树与 crop 形态仍并存。
