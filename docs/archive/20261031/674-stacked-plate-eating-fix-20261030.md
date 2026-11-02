# 674 代码筛查：堆叠盘子食用会丢盘/状态串改

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`DishEating.finishItemUse` 原来：

```java
if (dish.servings() <= 1) {
    PanDishData.clear(stack);
    stack.setCount(1);
    return stack;
}
final PanDishData rest = ...;
PanDishData.write(stack, rest);
stack.setCount(1);
return stack;
```

问题：

1. `ServingPlateItem` 的 `stacksTo(16)`，同一道菜可堆叠；
2. 堆叠多个盘子食用时，`stack.setCount(1)` 会把整堆**直接压成 1 个**，其余盘子丢失；
3. `PanDishData.write(stack, rest)` 会改写**整堆**的 dish 组件，而不是只改被吃的那一个盘子，导致所有剩余盘子份数一起减少。

## 2. 修复

`finishItemUse` 区分单个/堆叠：

- 单个盘子：在原 stack 上清空 dish 或写入 `servings - 1`；
- 堆叠盘子：
  - `copyWithCount(1)` 取出一只盘子；
  - 原 stack `shrink(1)`，保留其余盘子及原组件；
  - 对取出的单盘清空 dish 或写入 `servings - 1`；
  - 放回玩家背包，满则掉落。

这样不再丢盘，也不会把整堆盘子的份数一起改掉。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,926,532 bytes
SHA-256 73E06DAF486E81958B26F44FB6E581DD9317AB667B3E9C375C3D267429094F38
```

## 4. 未完成

- 未实机；
- 未验证堆叠同菜/不同菜、背包满、创造模式全路径。
