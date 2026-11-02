# 395 创造模式收获修复 P0-BB 技术分析

> 日期：2026-10-29
> 目标：统一收获替换在创造模式下不再生成物品掉落。
> 约束：不推送；不伪造；未实机。

## 1. 问题

`UnifiedCropHarvestHandler` 取消原破坏后，无论玩家是否创造模式都会：

- 生成原 loot；
- 补种子；
- 补废枝叶；
- 移除方块。

创造模式原本不应产生掉落。

## 2. 修复

在 `event.setCanceled(true)` 后增加：

```java
if (player != null && player.isCreative()) {
    removeBlock(pos);
    if (part == bottom) removeBlock(above);
    return;
}
```

- 创造模式只移除方块；
- 不生成任何物品；
- 双格仍清理上下部。

## 3. 测试

```text
PASS: 393 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
```

## 4. 风险

- 未实机；
- 创造模式是否还应对某些方块给物品未逐项验证；
- 只处理本 handler；
- 可能影响依赖原掉落的创造建筑流程。
