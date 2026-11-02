# 668 代码筛查：晾架自动化插入直接别名调用方物品栈

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`DryingRackBlockEntity.RackItemHandler.insertItem` 原来把调用方传入的 `ItemStack` 直接交给内部 `ItemStackHandler`：

```java
final ItemStack remainder = inventory.insertItem(0, stack, simulate);
```

NeoForge `ItemStackHandler.insertItem` 在目标槽为空且未模拟时可能直接把该 stack 放入内部槽位（而不是复制）。于是：

- 自动化/漏斗持有的 stack 与晾架内部 stack 成为同一个引用；
- 后续调用方修改自己持有的 stack 时，会同时改到晾架内容；
- 属于 ItemHandler 边界/别名问题。

## 2. 修复

先复制再插入：

```java
final ItemStack input = stack.copy();
final ItemStack remainder = inventory.insertItem(0, input, simulate);
```

返回值仍是 remainder，调用方语义不变。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,926,133 bytes
SHA-256 3CA3DCD0AD3B97C672FB4875300CCB7FDD27D80A990BE2CF9F70E6E83E8D5924
```

## 4. 未完成

- 未实机；
- 未验证所有自动化调用方的 stack 生命周期。
