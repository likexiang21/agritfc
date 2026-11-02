# 673 种子生长 boost 农田限制修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- `SeedTreatmentGrowthHandler` 增加点击方块农田判定；
- 非农田/非 `farmland` 方块不再调度生长 boost；
- 兼容 vanilla `FarmBlock` 与 TFC/A 命名 farmland；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,926,339 bytes
SHA-256 F79E9CA3B05B2245A2D224FB9CCB5DDD59BA821311C23F92B652E53735DB52B8
```

## 3. 未做

- 未实机；
- 未验证全部 TFC/A 农田类型。
