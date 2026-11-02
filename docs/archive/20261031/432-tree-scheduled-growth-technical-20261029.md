# 432 树苗定时生长 P0-BT 技术分析

> 日期：2026-10-29
> 目标：树苗不再只依赖 random tick；放置后主动调度稳定生长。
> 约束：不推送；不伪造；未复测。

## 1. 问题

实机测试中：

- 树苗保留；
- stage 仍为 0；
- randomTickSpeed=1000 下 15 秒未推进。

## 2. 修复

`NutTreeSaplingBlock` / `SpiceTreeSaplingBlock` 增加：

```java
@Override
public void onPlace(...) {
    super.onPlace(...);
    if (!level.isClientSide()) {
        level.scheduleTick(pos, this, 20);
    }
}

@Override
public void tick(BlockState state, ServerLevel level, BlockPos pos, RandomSource random) {
    int stage = state.getValue(STAGE);
    if (stage < 2) {
        level.setBlock(pos, state.setValue(STAGE, stage + 1), Block.UPDATE_CLIENTS);
        level.scheduleTick(pos, this, 20);
        return;
    }
    growTree(level, pos, random);
}
```

保留原 `randomTick` 作为补充。

## 3. 结果

```text
gradle compileJava
BUILD SUCCESSFUL
gradle build
BUILD SUCCESSFUL
```

## 4. 未验证

- 没有实机复测 scheduled tick；
- 没有确认树冠/树干；
- 没有确认旧存档树苗；
- 不能宣称树生长完成。
