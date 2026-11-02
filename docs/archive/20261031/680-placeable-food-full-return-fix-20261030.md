# 680 代码筛查：满份摆盘食物不返还整块

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

OPEN-042 把 `PlaceableFoodBlock.getDrops` 改为空列表，避免整块 + 切片双掉。
副作用是：**未吃过的满份派/蛋糕**被破坏时也只掉剩余切片，而不是整块物品。

## 2. 修复

- `PlaceableFoodBlockEntity` 增加：

```java
public boolean isFull() { return servings >= maxServings(); }
public int maxServings()
```

- `PlaceableFoodBlock.getDrops`：
  - 从 loot 上下文取 `ORIGIN` 与 `level`；
  - 若该位置 BE 为 `PlaceableFoodBlockEntity` 且 `isFull()`，返回一个方块物品；
  - 否则返回空，由 `onRemove` 掉切片；
- `PlaceableFoodBlock.onRemove`：
  - 只在 `!pie.isFull()` 时调用 `dropContents()`；
  - 满份时由 `getDrops` 掉整块，避免双掉。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,927,122 bytes
SHA-256 AF14CE68AB82CDE93290AEC322A1F9ABF08233439632EE5C72307B552DBAE61D
```

## 4. 未完成

- 未实机；
- 未验证活塞/命令替换满份食物的边界。
