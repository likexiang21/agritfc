# 360 草莓废枝叶来源 P0-AJ 技术分析

> 日期：2026-10-29
> 目标：A 87 记录包含 strawberry；TFC 仍保留 strawberry_bush。为草莓补真实 crop_waste 来源，同时不把它算进 TFC 10 灌木。
> 约束：不推送；不伪造；未实机。

## 1. 背景

- `CropWasteCrops` 82 条包含 `strawberry`；
- B 的 `crop_waste/strawberry` 物品已存在；
- 但 A 没有 `crop/strawberry` 方块，TFC 只有 `tfc:plant/strawberry_bush`；
- 原 `BushSpecies` 10 种刻意排除 strawberry，因此草莓废枝叶之前没有来源。

## 2. 实现

`StrawberryWasteHandler`：

- 精确匹配 `tfc:plant/strawberry_bush`；
- 若是 `SeasonalPlantBlock` 且 `Lifecycle.FRUITING` 才掉；
- 追加 1 个 `crop_waste/strawberry`；
- 不取消原 TFC 草莓掉落；
- 不影响 TFC 10 bush handler。

## 3. 测试

```text
gradle compileJava
BUILD SUCCESSFUL
PASS: 343 crop P0 checks
```

## 4. 风险

- 未实机；
- 只补废枝叶，不处理草莓种植/繁殖；
- 草莓仍不是真正 A 普通作物；
- 不能宣称 A 87 全部验收。
