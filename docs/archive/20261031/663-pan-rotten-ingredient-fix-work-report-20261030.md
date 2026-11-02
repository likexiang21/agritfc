# 663 锅腐烂食材拒绝修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- `CookingPanBlockEntity.addIngredient` 增加 `FoodCapability.isRotten` 检查；
- 玩家右键路径不再能加入腐烂食材；
- `isItemValid` 的约束在交互路径生效；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,925,999 bytes
SHA-256 DB732F09968AE49D1EF97EC076EE59DBA789C902005E2778E0F1BE491E3030D3
```

## 3. 未做

- 未实机；
- 未验证自动化路径。
