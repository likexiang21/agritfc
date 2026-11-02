# 649 木料堆 insert all 参数修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- `LumberPileBlockEntity.insert` 让 `all` 参数生效；
- `all=false` 行为保持每次 1 个；
- `all=true` 插入 `min(held.count, capacity)`；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,926,150 bytes
SHA-256 CCB0A91E5B836529F3A7BBD451D0E6E1CFC4669992273ABA4EEDAE07ACEAFDD6
```

## 3. 未做

- 未实机；
- 未接 shift 批量插入。
