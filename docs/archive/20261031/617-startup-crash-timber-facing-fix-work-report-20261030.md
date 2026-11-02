# 617 启动崩溃修复工作报告（OPEN-014）

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 完成

- 复现日志中的首个异常根因；
- 拆分 `TimberPieceBlock` / `DirectionalTimberPieceBlock`；
- `TimberBlocks` 按 part 选择类；
- `weight()`、`canSurvive` 同时支持两种类；
- `gradle build` 成功；
- 新 jar 已迁移到 `mods/`。

## 2. 证据

```text
logs/latest.log:
  TimberPieceBlock.<init> line 22
  Cannot set property facing as it does not exist
```

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,921,008 bytes
SHA-256 1EC50C413A63A1B2E94CCF7A325CB5749628398614C7F10AE86291E299BE4658
```

## 3. 未做

- 没有 Java 21/PCL 环境，未实机；
- 需用户启动确认次级 NPE 是否消失。
