# 672 代码筛查：种子处理生长 boost 未限制在农田

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`SeedTreatmentGrowthHandler.onRightClickBlock` 只检查：

- 事件未取消；
- 服务端；
- 手持种子有 `SEED_TREATMENT`；
- boost > 0。

随后直接调度：

```java
final BlockPos target = event.getPos().relative(event.getFace());
level.getServer().execute(() -> applyBoost(level, target, boost));
```

没有检查：

- 点击的方块是否为农田；
- 目标位置是否真的是新放置的作物。

因此对**非农田方块**右键（或右键已有作物/其它可催熟方块）时，也可能触发一次 `applyBoost`，造成意外生长。

## 2. 修复

增加农田判定：

```java
final BlockState clicked = level.getBlockState(event.getPos());
final String clickedId = BuiltInRegistries.BLOCK.getKey(clicked.getBlock()).toString();
if (!(clicked.getBlock() instanceof FarmBlock) && !clickedId.endsWith("farmland")) {
    return;
}
```

兼容 vanilla `FarmBlock` 与 TFC/A 的 `farmland` 命名方块。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,926,339 bytes
SHA-256 F79E9CA3B05B2245A2D224FB9CCB5DDD59BA821311C23F92B652E53735DB52B8
```

## 4. 未完成

- 未实机；
- 未验证所有 TFC/A 农田类型。
