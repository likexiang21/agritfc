# 563 OPEN-005 扩展：作物废枝叶图标差异技术分析

> 日期：2026-10-29
> 状态：**静态视觉映射完成；未实机**
> 约束：视觉可用，但不重绘贴图。

## 1. 问题

82 个 `crop_waste/*` 原本全部使用同一张：

```text
tfc:item/straw
```

导致创造页整页相同图标。

## 2. 修复

不绘制任何新贴图，改为把每个物种映射到**已有作物贴图**：

- A 作物：`tfcfarmingplus:block/crop/<species>_age_N[_top]`；
- TFC 作物：`tfc:block/crop/<species>_N`；
- 草莓：`tfc:block/berry_bush/strawberry_bush`。

例：

```text
spinach   → tfcfarmingplus:block/crop/spinach_age_5
faba_bean → tfcfarmingplus:block/crop/faba_bean_age_5_top
potato    → tfc:block/crop/potato_6
strawberry→ tfc:block/berry_bush/strawberry_bush
```

## 3. 覆盖

脚本：`map_crop_waste_textures.py`

```text
species 82
mapped  82
missing 0
```

82 个 item model 的 `layer0` 全部改为对应物种贴图。

## 4. 校验

```text
json 6483 / bad 0
models 3689
final_static_audit problems 0
static_resource_audit problems 0
gradle build BUILD SUCCESSFUL
```

## 5. 未完成

- 未实机查看图标可读性；
- 仍不是专门绘制的“废枝叶”图标，只是复用作物贴图；
- 未处理视觉细节。
