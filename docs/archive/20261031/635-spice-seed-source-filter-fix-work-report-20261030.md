# 635 香料种子源过滤修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- `SpiceSeedDropHandler` 只从有 `SEEDS` 的香料物种随机；
- 避免树形香料空掉落；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,922,504 bytes
SHA-256 D214794275030D777106CE6155EA17DD76416862E9837BB642F3708416F1388D
```

## 3. 未做

- 未实机；
- 未设计树形香料独立种子源。
