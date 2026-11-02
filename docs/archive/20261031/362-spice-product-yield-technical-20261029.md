# 362 香料形态产物产量 P0-AK 技术分析

> 日期：2026-10-29
> 目标：让 tree/root 形态香料在收获时稳定多产 1 个产物，而不是所有形态都只能得 1 个。
> 约束：不推送；不伪造；未实机。

## 1. 数据

`SpiceSpecies.productYield()`：

- `tree` → 2；
- `root` → 2；
- `herb/vine/corm/shrub` → 1。

## 2. 实现

- `CropBItemResolver.productForCropBlock` / `productCountForCropBlock`；
- `UnifiedCropHarvestHandler` 统计原 loot 中已有产物，按差额补足；
- 避免原 loot 已有 2 个时再次超发。

## 3. 测试

```text
PASS: 363 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
```

新增 20 条 productYield 校验。

## 4. 风险

- 未实机；
- tree/root 没有真实树/根机制，只是产量差异；
- 原 loot 产物数量未逐项验证；
- 数值未平衡。
