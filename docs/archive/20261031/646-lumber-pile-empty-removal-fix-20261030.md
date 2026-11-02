# 646 代码筛查：木料堆取空后仍残留空方块

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`LumberPileBlockEntity.updateState` 原来：

```java
final int count = Math.max(1, Math.min(64, lumberCount()));
```

`lumberCount() == 0` 时被强制写成 `COUNT=1`，于是玩家从堆里取走最后一块木料后：

- 方块仍在世界中；
- 内部库存为空；
- 显示成一块最低高度的空木堆；
- 破坏后没有任何掉落（方块本身没有 item）。

这是“没有独立方块物品的容器”残留空方块的逻辑问题。

## 2. 修复

`updateState` 在库存为 0 时直接移除方块：

```java
if (lumberCount() == 0) {
    level.removeBlock(worldPosition, false);
    return;
}
```

- `extract()` 取走最后一块后触发移除；
- `onLoadAdditional()` 读到空库存也会清理；
- `onRemove` 的 `dropContents()` 在库存已空时无操作，不会重复掉落。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,926,135 bytes
SHA-256 ED226F53654E48452C19C25280F37D902E48C349B1F6F79681A5748C9AD05C63
```

## 4. 未完成

- 未实机；
- 未验证堆叠/取空操作的客户端同步。
