# 661 锅油勺实际转移修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- `PanInteractions.scoopOil` 的 `tryFluidTransfer` 从模拟改为实际转移；
- 副手油容器减少 5 mB，锅油罐增加 5 mB；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,925,998 bytes
SHA-256 997E6C69AE6E836CD356AB7F31386B758162CD274D97625EDF1F4314F52F3A84
```

## 3. 未做

- 未实机；
- 未验证不同油容器边界。
