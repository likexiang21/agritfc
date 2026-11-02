# 697 严格评估 P1 收尾工作报告

> 日期：2026-10-31
> 状态：**代码已修复；未实机**

## 1. 完成

- `SeedlingItem`、`CormItem`、`SpiceRootItem` 在放置前检查目标可替换，避免覆盖已有方块；
- `SeedTreatmentGrowthHandler`：
  - 只处理真正种子（排除 seedling）；
  - 非直接播种物种不排队 boost；
  - 目标必须可替换；
- A/TFC 种子处理 boost 改用 TFC `CropHelpers.growthTickStep`，不再直接 `setGrowth`；
- 消除带处理幼苗的双重 boost。

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
- 新 Firmalife 废枝叶图标/中文名质量、potted 与 `grape_string_red/white`、创造模式 guard；
- 香料/草莓视觉模型、AFC nut_state 资产。
