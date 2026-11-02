# 368 双格作物上下部清理 P0-AN 技术分析

> 日期：2026-10-29
> 目标：修复统一收获取消底部方块后，顶部方块可能残留在原地的问题。
> 约束：不推送；不伪造；未实机。

## 1. 问题

`UnifiedCropHarvestHandler` 对 `part=bottom` 的成熟作物：

- 取消破坏；
- 掉原 loot；
- `removeBlock(bottom)`。

但顶部方块没有同时移除，可能：

- 留在原地；
- 之后被单独破坏；
- 产生额外掉落/视觉残留。

## 2. 修复

在移除底部后：

```java
if ("bottom".equalsIgnoreCase(propertyText(state, "part"))) {
    BlockPos above = pos.above();
    if (level.getBlockState(above).is(state.getBlock())) {
        level.removeBlock(above, false);
    }
}
```

不额外掉顶部 loot，因为底部原 loot 已生成。

## 3. 测试

```text
gradle compileJava
BUILD SUCCESSFUL
PASS: 363 crop P0 checks
```

## 4. 风险

- 未实机；
- 只处理同方块顶部；
- 原 loot 是否已包含顶部产物未逐项验证；
- 可能影响依赖顶部方块的第三方逻辑。
