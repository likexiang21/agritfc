# 676 代码筛查：创造模式吃盘仍消耗/改份数

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`DishEating` 的两个食用入口：

```java
eatFromPlateBlock(...)
finishItemUse(...)
```

都没有检查创造模式。

`consumeOne` 内部虽然判断了 `instabuild` 不调用 `player.eat`，但外层仍然：

- 盘子方块：扣 servings / 清空盘；
- 手持盘子：`shrink(1)` / 改 dish 份数。

结果创造模式吃菜仍会消耗/改份数，与其它入口（锅、食材）的创造模式处理不一致。

## 2. 修复

两个入口在确认 dish 合法后：

```java
if (player.getAbilities().instabuild) {
    return stack; // finishItemUse
}
if (player.getAbilities().instabuild) {
    return true; // eatFromPlateBlock，不改盘
}
```

腐烂判断仍在前面，创造模式也不能吃腐烂菜。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,926,551 bytes
SHA-256 A3D670B82563E0CBA7347DF46DDFEAD915461A160B7570318D25F7CD1A0D9A70
```

## 4. 未完成

- 未实机；
- 未验证创造/生存切换边界。
