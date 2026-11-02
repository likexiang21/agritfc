# 565 OPEN-011 扩展：AFC 木工物品图标技术分析

> 日期：2026-10-30
> 状态：**静态视觉补全；未实机**
> 约束：视觉可用，但不重绘贴图。

## 1. 问题

TFC 20 木材已有 TFCW 原版 debarked item 图标。

AFC 14 木材没有 debarked item 图标，之前 item model 直接用 block parent，创造页显示 3D 方块。

## 2. 修复

不新增/不重绘 PNG，复用 AFC 已有原木图标：

```text
afc:item/wood/log/<wood>
```

14 木材 ×3 类型 = 42 个 item model 改为：

```json
{
  "parent": "minecraft:item/generated",
  "textures": { "layer0": "afc:item/wood/log/<wood>" }
}
```

覆盖：

```text
araucaria / baobab / beech / cypress / eucalyptus / fig / ginkgo /
hevea / ipe / ironwood / mahoe / mahogany / teak / tualang
```

## 3. 边界

- 这是 **AFC 原木物品图标**，不是 TFCW 那种专用 debarked 图标；
- 与 TFC 20 木材的精确原版图标仍有差别；
- 没有新增贴图。

## 4. 校验

```text
gradle build BUILD SUCCESSFUL
item_models 943
final_static_audit problems 0
static_resource_audit problems 0
```

## 5. 未完成

- 未实机查看图标；
- 未制作 AFC 专用 debarked 图标；
- 未做 TFCW 交互/音效对照。
