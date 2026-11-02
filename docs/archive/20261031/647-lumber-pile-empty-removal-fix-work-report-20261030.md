# 647 木料堆空方块移除修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- `LumberPileBlockEntity.updateState` 在库存为 0 时移除方块；
- 取空最后一块木料不再留下空木堆；
- 加载到空库存的旧方块也会清理；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,926,135 bytes
SHA-256 ED226F53654E48452C19C25280F37D902E48C349B1F6F79681A5748C9AD05C63
```

## 3. 未做

- 未实机；
- 未验证客户端同步。
