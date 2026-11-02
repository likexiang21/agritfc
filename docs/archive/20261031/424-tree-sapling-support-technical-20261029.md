# 424 树苗支撑与生长定位 P0-BP 技术分析

> 日期：2026-10-29
> 目标：解释玩家区块树苗测试中树苗消失的原因，并修正支撑判定。
> 约束：不推送；不伪造；未完成树生长复测。

## 1. 观察

玩家区块测试：

```text
OK_PLAYER_CHUNK_NUT_PLACED
OK_PLAYER_CHUNK_SPICE_PLACED
RUNTIME_TREE_PLAYER_CHECK
```

check 中没有：

```text
PLAYER_NUT_SAPLING_STILL
PLAYER_NUT_STAGE0/1/2
PLAYER_NUT_TRUNK
PLAYER_NUT_CANOPY3/4
```

说明树苗在 15 秒后已不在原位置。

## 2. 代码审查

`NutTreeSaplingBlock` / `SpiceTreeSaplingBlock` 的 `mayPlaceOn`：

```java
return state.is(BlockTags.DIRT) || super.mayPlaceOn(state, level, pos);
```

原测试支撑是 `minecraft:dirt`。

即使理论上 `BlockTags.DIRT` 应包含 dirt，实际运行时树苗仍被移除；优先怀疑：

- datapack tag 覆盖；
- `BlockTags.DIRT` 在该环境中的绑定；
- `canSurvive` 更新时序。

## 3. 修复

显式加入：

```java
state.is(Blocks.DIRT) || state.is(Blocks.GRASS_BLOCK)
```

与原有 `BlockTags.DIRT`/`super` 并列。

## 4. 测试状态

- 修复已编译（build 成功）；
- **尚未复测**；
- 不能据此宣称树生长完成。

## 5. 风险

- 若是随机刻/树生成代码问题，这个修复不会解决；
- 放宽支撑可能允许更多地面；
- 仍需玩家区块复测。
