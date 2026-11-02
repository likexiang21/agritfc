# 514 P0-2 删除重复木碗/陶碗技术分析

> 日期：2026-10-29
> 状态：**静态修复完成；未实机**
> 约束：不实机、不处理视觉、不推送。

## 1. 问题

TFC 已有：

- `tfc:wooden_bowl` 方块/物品；
- `tfc:ceramic/bowl` 方块/物品。

B 又注册：

- `tfcagricultureplus:bowl/wood`
- `tfcagricultureplus:bowl/ceramic`

并添加 2 个转换/占位配方：

```json
// bowl_ceramic
ingredients: [{"item":"tfc:ceramic/bowl"}]
result: tfcagricultureplus:bowl/ceramic

// bowl_wood
ingredients: [2 × "#tfc:lumber"]
result: tfcagricultureplus:bowl/wood
```

同时 B 的 `ServingBowlItem` 只用于“盘装菜分装到碗”，与 TFC 碗的
可放置 `BowlBlock` / 汤碗用途不同，属于错误重复物品。

## 2. 修复

删除：

- `AgricultureBowls.java`
- `ServingBowlItem.java`
- `bowl_wood.json`
- `bowl_ceramic.json`
- 2 个 item model
- 2 个语言键 / 语言文件
- 创造页 2 个入口
- 主类 `AgricultureBowls.register(...)`
- `DishEating.transferToBowl(...)`
- `ServingPlateBlock.useItemOn(...)` 的碗分支

## 3. 行为变化（明确记录）

- 盘装菜不再能“分装到 B 碗”；
- 仍可直接从盘子食用；
- 不再新增任何重复碗物品；
- 将来若需要分装，应基于 TFC `BowlBlock` 正确实现，而不是再注册新碗。

这是**功能缩减**，不是等价替换；必须记录，不能声称“完整保留”。

## 4. 静态校验

```text
gradle clean build BUILD SUCCESSFUL
validate_crop_p0a.py PASS
final_static_audit.py problems 0
static_audit.py JSON 6250 / bad 0
lang 1061 / 1061
item_models 922
models 3668
```

## 5. 未完成

- 未实机；
- 未实现 TFC BowlBlock 分装；
- OPEN-004 工作方块配方仍未处理。
