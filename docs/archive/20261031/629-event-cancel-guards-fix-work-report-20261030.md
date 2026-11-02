# 629 事件处理器取消状态检查修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- 8 个 `BlockEvent.BreakEvent` 处理器增加 `event.isCanceled()` 早退；
- 覆盖小麦/谷物、TFC 灌木、A macadamia、香料种子、草莓种子/废枝、野坚果；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,921,825 bytes
SHA-256 1093B0206CF7CC7BF73586FEB7D09B7407810D8C21F866DD3EDF436361A05041
```

## 3. 未做

- 未实机；
- 未验证事件优先级组合。
