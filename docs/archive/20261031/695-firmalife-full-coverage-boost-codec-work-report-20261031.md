# 695 严格评估收尾工作报告

> 日期：2026-10-31
> 状态：**代码/数据已修改；未实机**

## 1. 完成

- Firmalife 20 个 `plant/*` + 2 个 `grape_string_plant_*` 全部接入 B 副产物链：
  - 8 香草：`spice_waste` + 刀具门槛；
  - 14 其余：新增 `crop_waste/*` 物品、模型、语言、堆肥标签；
- 种子处理 boost 支持 A/TFC `CropBlockEntity`：
  - `SeedTreatmentGrowthHandler` 与 `SeedlingItem` 均改用 TFC `CropHelpers.growthTickStep`；
- `TfcFarmlandCropBlock` 增加 codec；
- build 成功，jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
json 6530 / models 3704 / blockstates 539 / item_models 957
lang en_us 1107 / zh_cn 1107
final_static_audit problems 0
```

当前 jar：

```text
2,954,689 bytes
SHA-256 9CAA9D331665B567C14FF283C7C45022FCF0F9F9A22CB81671B246B2629A106A
```

## 3. 未完成 / 需确认

- 未实机；
- TFC 耕地上 A 38 物种 + TFC 10 物种 + B 草莓不能再直播，需确认这是否是用户要的“不豁免”；
- 香料/草莓 8 age 单一模型，无视觉生长；
- AFC 树叶 nut_state 资产缺口。
