# 436 树冠生成日志定位 P0-BV 技术分析

> 日期：2026-10-29
> 目标：用运行时日志确认 `growTree` 是否生成树叶。
> 约束：不推送；不伪造；测试后恢复环境。

## 1. 新增日志

`NutTreeSaplingBlock` / `SpiceTreeSaplingBlock` 在 `growTree` 末尾：

```java
TFCAgriculturePlus.LOGGER.info(
    "[TFC Agriculture Plus] grew {} at {}, leaves={}",
    species.id(), pos, leavesPlaced);
```

## 2. 实机结果

```text
grew cinnamon at BlockPos{x=-1018, y=88, z=13489}, leaves=0
grew pistachio at BlockPos{x=-1020, y=88, z=13489}, leaves=0
```

树干生成，但**树叶放置数为 0**。

## 3. 原因

`growTree` 只对：

```java
level.isEmptyBlock(leafPos) || level.getBlockState(leafPos).canBeReplaced()
```

的位置放树叶。

测试地点 y=88 在山体/固体地形内，树冠位置几乎全被固体方块占据，因此 0 片叶子可放。

这不是树叶注册失败，也不是树代码必然失败；是**测试地点没有空间**。

## 4. 代码行为

当前逻辑：

- 树干直接 `setBlockAndUpdate`，可覆盖固体；
- 树叶只填空位/可替换方块，避免把山体全换成树叶。

这是设计选择，但意味着树长在山体里时可能只有树干没有树冠。

## 5. 未验证

- 开阔地树冠；
- 树叶衰减；
- 树苗掉落；
- 旧存档。

## 6. 证据

```text
mod_rebuild/docs/audit/runtime-tree-canopy-log-20261029.log
```
