# 637 TFC 灌木采收废枝修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- `BushHarvestHandler` 采收后掉 `bush_waste`；
- `BushRightClickHarvestHandler` 同样处理；
- `BushWasteHandler` 保留普通破坏路径；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,923,052 bytes
SHA-256 D33A87538B2575B55026709090501E8CB13F80F825C944C3A80C58E195CC9A98
```

## 3. 未做

- 未实机；
- 未做产量平衡。
