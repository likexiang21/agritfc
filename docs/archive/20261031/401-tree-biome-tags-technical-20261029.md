# 401 树木群系标签 P0-BE 技术分析

> 日期：2026-10-29
> 目标：把坚果/香料树 worldgen 从蘑菇群系标签拆出，各自使用更合适群系。
> 约束：不推送；不伪造；未实机。

## 1. 新增标签

`nut_tree_biomes`：

```text
#minecraft:is_forest
#minecraft:is_taiga
```

`spice_tree_biomes`：

```text
#minecraft:is_forest
#minecraft:is_jungle
```

## 2. biome modifier

```text
add_nut_saplings.json  -> #tfcagricultureplus:nut_tree_biomes
add_spice_trees.json   -> #tfcagricultureplus:spice_tree_biomes
```

蘑菇仍用 `wild_mushroom_biomes`。

## 3. 测试

```text
PASS: tree biome tags
processResources BUILD SUCCESSFUL
PASS: 393 crop P0 checks
```

## 4. 风险

- 未实机；
- TFC 群系是否完整映射到 minecraft:is_forest/is_jungle 未验证；
- 香料树 jungle 可能过窄/不存在；
- 密度仍未平衡。
