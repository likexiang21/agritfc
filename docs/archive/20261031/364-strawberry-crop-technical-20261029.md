# 364 草莓普通作物 P0-AL 技术分析

> 日期：2026-10-29
> 目标：把 A 87 记录中缺失的 strawberry 补成真正的 B 普通作物，而不是只靠 TFC strawberry_bush 的废枝叶。
> 约束：不推送；不伪造；未实机。

## 1. 新增

- B 方块 `tfcagricultureplus:crop/strawberry`；
- B 种子 `tfcagricultureplus:seeds/strawberry`（BlockItem）；
- 8 龄 CropBlock；
- loot：
  - 1 × `tfc:food/strawberry`；
  - 1 × B strawberry seed；
- `crop_waste/strawberry` 由统一收获追加。

## 2. 接线

- `CropBItemResolver.seedForCropBlock` 识别 B strawberry；
- `wasteForCropBlock` 识别 B strawberry → 已有 `crop_waste/strawberry`；
- `UnifiedCropHarvestHandler` 走原 loot + 种子 + 废枝叶；
- `SeedTreatments.isSeedItemId` 识别 `seeds/strawberry`；
- 直播拦截/育苗盘/幼苗移栽自动覆盖。

## 3. 资源

- blockstate age 0..7；
- block model（临时 strawberry bush 贴图）；
- seed item model（临时 strawberry food 贴图）；
- loot table；
- en/zh。

## 4. 测试

```text
PASS: strawberry crop resources
PASS: 363 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
processResources BUILD SUCCESSFUL
```

## 5. 风险

- 未实机；
- B 命名空间是替代实现，不是 A 的 `crop/strawberry`；
- TFC strawberry_bush 仍存在，两者并存；
- 没有野生生成；
- 临时贴图；
- 不能宣称 A 87 全部验收。
