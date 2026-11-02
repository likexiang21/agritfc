# 693 严格评估 P0-2/P1 修复工作报告

> 日期：2026-10-31
> 状态：**代码已修复；未实机**

## 1. 本轮完成

- 新增 `TfcFarmlandCropBlock`，让 B 的香料/草莓作物同时接受：
  - vanilla `minecraft:farmland`；
  - TFC `#tfc:farmlands` 的 8 种耕地；
- 6 个 `SpiceCropBlocks` 形态类与 `STRAWBERRY_CROP` 全部改用该基类；
- 统一 `DirectSeedPlantingGate`、`SeedTreatmentGrowthHandler` 的耕地判断；
- `CropWasteHandler` 支持 `tfc:wild_crop` / `tfcfarmingplus:wild_crop` 的布尔 `mature`；
- 修正 `wintergreen` 的 TFC 方块 ID 为 `wintergreen_berry_bush`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,954,689 bytes
SHA-256 9CAA9D331665B567C14FF283C7C45022FCF0F9F9A22CB81671B246B2629A106A
```

## 3. 未完成

- 未实机；
- Firmalife 剩余 12+2 植物已在 694/695 接入；
- 香料/草莓 8 个 age 仍共用单一临时模型，无视觉生长差异；
- P0-1（BlockEntity 参数）、P0-2（TFC 耕地）只能静态证明参数链正确，实际产量/生长仍需运行期。
