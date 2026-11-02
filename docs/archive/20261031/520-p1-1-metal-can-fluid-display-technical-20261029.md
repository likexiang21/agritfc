# 520 P1-1 金属罐液体显示技术分析

> 日期：2026-10-29
> 状态：**静态显示修复完成；未实机**
> 约束：不实机、不处理视觉、不推送。

## 1. 问题

用户报告：

- 金属罐交互几乎失效；
- 物品无法反映装入液体；
- 对照 TFC 陶罐实现。

静态确认：

- `MetalCanItem extends FluidContainerItem`，容量 500 mB；
- 已注册 `Capabilities.FluidHandler.ITEM`；
- 但 19 个金属罐 item model 只有：
  ```json
  {"parent":"item/generated","textures":{"layer0":"tfc:item/metal/sheet/<metal>"}}
  ```
- 没有 `tfc:fluid_container` loader，也没有 `.filled` 名称键；
- 因此即使流体组件存在，物品图标/名称也不反映液体。

## 2. 对照 TFC 陶罐

TFC `ceramic/jug.json`：

```json
{
  "loader": "tfc:fluid_container",
  "parent": "neoforge:item/default",
  "textures": {
    "base": "tfc:item/ceramic/jug_empty",
    "fluid": "tfc:item/ceramic/jug_overlay"
  }
}
```

金属罐改为同样 loader：

```json
{
  "loader": "tfc:fluid_container",
  "parent": "neoforge:item/default",
  "textures": {
    "base": "tfc:item/metal/sheet/<metal>",
    "fluid": "tfc:item/metal/bucket/overlay"
  }
}
```

并新增 19 × 2 个 `.filled` 名称键：

```text
item.tfcagricultureplus.metal_can.<metal>.filled
  zh_cn: 装有%s的金属罐
  en_us: %s Metal Can
```

## 3. 覆盖

19 个金属：

```text
bismuth · bismuth_bronze · black_bronze · bronze · brass · copper · gold
nickel · rose_gold · silver · tin · zinc · sterling_silver · wrought_iron
cast_iron · steel · black_steel · blue_steel · red_steel
```

## 4. 校验

```text
gradle build BUILD SUCCESSFUL
lang en_us 1080 / zh_cn 1080
missing 0 / extra 0
final_static_audit problems 0
static_audit json 6425 / bad 0
```

## 5. 明确未完成

- 未实机验证流体装入/倒出/图标变化；
- 未改基础贴图：仍借用 TFC 金属板/桶 overlay，属于视觉问题；
- `metal_can_fluids` 仍只接受 `#c:plantoil` / `#firmalife:oils`；是否扩到其他 TFC 流体是玩法决策，未擅自修改；
- 未证明交互“完全恢复”，只完成显示链路的静态修复。
