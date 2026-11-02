# 557 烹饪锅占位模型替换技术分析

> 日期：2026-10-29
> 状态：**静态视觉修复；未实机**
> 约束：视觉可用，但不做大面积贴图重绘。

## 1. 问题

`CookingPan` 的 block model 原为：

```json
{
  "parent": "minecraft:block/cube_all",
  "textures": { "all": "minecraft:block/iron_block" }
}
```

即整个方块就是一块铁块，没有锅的形状。

## 2. 修复

改为自包含 6 个 element 的平底锅模型：

- 锅底：`[1,0,1] → [15,1,15]`
- 四面锅壁：`y 1 → 4`
- 手柄：`[15,1,7.5] → [19,2,8.5]`

纹理全部复用 TFC 现有：

```text
tfc:block/metal/smooth/wrought_iron
```

没有新增/重绘任何 PNG。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
json 6483 / models 3689 / blockstates 539
final_static_audit problems 0
static_resource_audit problems 0
```

## 4. 未完成

- 未实机查看实际渲染；
- 未做锅的 GUI/内容物 BER 视觉；
- 未处理其它占位模型。
