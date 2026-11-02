# 671 方块全量列表去重修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- `AgricultureBlocks.all()` 不再重复追加 `DRYING_RACKS`；
- `AgricultureBlocks.allIds()` 同样去重；
- 只保留独立注册在 `TimberBlocks.ALL` 的原木件追加；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,926,105 bytes
SHA-256 E83EDC52ED0A393C2CCCB3DD579147A3FF1601AEFA4831E77DD46AC69C46C8D8
```

## 3. 未做

- 未实机；
- 未验证客户端自检计数。
