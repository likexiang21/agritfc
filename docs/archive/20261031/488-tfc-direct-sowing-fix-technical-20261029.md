# 488 TFC 直接播种回归修复 P0-CV 技术分析

> 日期：2026-10-29
> 目标：修复 `DirectSeedPlantingGate` 与 292-#3 计划的冲突。
> 约束：不推送；不伪造。

## 1. 计划依据

`292-crop-open-issues-decisions` 第 3 项：

> 不给 TFC 作物强行加育苗；TFC 仍直接播种。

## 2. 原实现问题

`DirectSeedPlantingGate` 对所有 `SeedTreatments.isSeedItemId` 的种子取消右键耕地：

- 包括 TFC 种子；
- 导致 TFC 29 无法直接播种，与计划冲突。

## 3. 修复

```java
if (itemId.startsWith("tfc:")) {
    return;
}
```

- TFC 种子恢复直接播种；
- A/B 种子仍走育苗盘→seedling→移栽；
- TFC 收获/掉落覆盖不受影响（仍在 UnifiedCropHarvestHandler 中）。

## 4. 构建

```text
gradle build BUILD SUCCESSFUL
validate_crop_p0a.py PASS
jar 2,745,942 bytes
```

## 5. 未验证

- TFC 直接播种实机右键；
- A/B 育苗门仍生效的实机复测；
- 收获覆盖与直接播种组合。
