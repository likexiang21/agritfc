# 573 育苗盘/菌包占位模型替换技术分析

> 日期：2026-10-30
> 状态：**静态视觉修复；未实机**
> 约束：视觉可用，但不重绘贴图。

## 1. 问题

`nursery_tray` 和 `mushroom_bag` 的 block model 原来都是：

```json
{"parent":"minecraft:block/cube_all","textures":{"all":"tfc:block/wood/planks/oak"}}
```

整块橡木板，与方块功能无关。

## 2. 育苗盘

- 木框：`tfc:block/wood/planks/oak`；
- 土壤：`tfc:block/dirt/entisol`；
- 模型：底板 + 四边矮墙 + 土壤面；
- 高度 4，与 `NurseryTrayBlock` 的 `box(0,0,0,16,4,16)` 一致；
- 没有新增贴图。

## 3. 菌包

- 袋体：`tfc:block/burlap`；
- 模型：袋身 + 收口 + 袋口；
- 高度 10，与 `MushroomBagBlock` 的 `box(1,0,1,15,10,15)` 一致；
- 没有新增贴图。

## 4. 校验

```text
gradle build BUILD SUCCESSFUL
json 6483 / models 3689 / blockstates 539
final_static_audit problems 0
```

## 5. 未完成

- 未实机查看渲染；
- 未按 stage 做模型变化（仍共用同一模型）；
- 未处理其它占位模型。
