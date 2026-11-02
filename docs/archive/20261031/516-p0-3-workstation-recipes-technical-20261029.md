# 516 P0-3 工作方块配方与掉落表技术分析

> 日期：2026-10-29
> 状态：**静态修复完成；未实机**
> 约束：不实机、不处理视觉、不推送。

## 1. 问题

用户报告：

- 全部工作方块没有合成表；
- 家具只有低质量占位配方。

静态确认：

- `log_cutting_board/*`、`cutting_board/*`、`knife_block/*`、`mortar/*`、`drying_rack/*`、`cooking_pan`、`silkworm_rack` 均无产物配方；
- 大量工作方块同时缺 loot table，破坏后无掉落。

## 2. 本次补齐

新增：

```text
data/tfcagricultureplus/recipe/workstations/
```

共 **174** 个配方：

| 族 | 数量 | 主要材料 | 工具 |
|---|---:|---|---|
| log_cutting_board | 34 | 对应原木 | 斧（损坏） |
| cutting_board（木） | 34 | 4 对应 lumber | 锯（损坏） |
| cutting_board（石） | 21 | 对应 raw rock | 锤（损坏） |
| knife_block | 34 | 6 lumber + 2 rods | 无 |
| drying_rack | 34 | 3 lumber + 4 rods | 无 |
| mortar | 15 | 2 raw rock | 锤（损坏） |
| cooking_pan | 1 | 3 wrought iron sheets | 锤（损坏） |
| silkworm_rack | 1 | 5 oak lumber + 2 rods | 无 |

说明：

- `lumber_pile` **不是** crafting 方块，而是 TFC 木材“潜行右键放入”的堆叠设备；已有 `TimberBlocks.registerPlacement()`，不为其伪造 crafting 配方。
- `log_cutting_board` 用斧 + 原木，符合“早期没锯也能做”的定位。
- 木/石案板分别用锯/锤，且工具通过 `tfc:damage_crafting_remainder` 损失耐久。
- 使用 `tfc:advanced_shapeless_crafting` 的配方均保留 `primary_ingredient` 与伤害 remainder。

## 3. 掉落表

新增 **174** 个 `loot_table/blocks/...`：

- 每个工作方块至少掉落自身；
- 覆盖 34 log board + 34 木案板 + 21 石案板 + 34 刀架 + 34 晾架 + 15 臼 + 锅 + 蚕架；
- `lumber_pile` 也补自身掉落。

## 4. 静态校验

```text
json 6425 / problems 0
recipe reference problems 0
validate_crop_p0a.py PASS
gradle build BUILD SUCCESSFUL
```

## 5. 未完成

- 未实机验证配方能否被 TFC workbench 正确匹配；
- `tfc:advanced_shapeless_crafting` 的重复 lumber 条目依赖运行时 schema，需实机复核；
- 家具 204 个占位配方仍在；
- 检查发现家具 `food_display` 与 `sink_cabinet` 的 shaped 配方**完全相同**（同木材同 pattern），是 OPEN-004 家具部分的真实冲突，留待 P1。
- `lumber_pile` 无 crafting 配方是设计选择，不是遗漏。
