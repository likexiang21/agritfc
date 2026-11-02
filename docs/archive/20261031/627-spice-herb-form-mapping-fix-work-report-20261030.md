# 627 香料草本形态映射修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- 找到 `SpiceSpecies` 的 `herb` 分支缺失；
- 在 `AgricultureSpices.newSpiceCrop` 增加 `case "herb"`；
- `SpiceCropBlocks.Herb` 不再未使用；
- `gradle build` 成功；
- 新 jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,921,587 bytes
SHA-256 DCCECB1C97E2909D9B44856B3C39D30309EB1E094E26410D6E6EF4D1F01CEC2D
```

## 3. 未做

- 未实机；
- 未验证全部 20 种香料形态。
