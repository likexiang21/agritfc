# 678 代码筛查：摆盘食物破坏时整块与切片同时掉落

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`PlaceableFoodBlock` 的 7 种食物方块都有 loot table：

```json
{
  "type": "minecraft:block",
  "pools": [{"entries": [{"name": "tfcagricultureplus:whole_pie"}]}]
}
```

同时 `PlaceableFoodBlock.onRemove` 会调用：

```java
pie.dropContents();
```

`PlaceableFoodBlockEntity.dropContents` 按剩余 `servings` 掉落切片。

因此破坏一块**已经吃过几口**的派/蛋糕时：

- loot table 掉落一个完整的 `whole_pie` / cake 方块物品；
- `onRemove` 又掉落剩余切片。

造成整块食物 + 切片重复掉落。

## 2. 修复

`PlaceableFoodBlock` 覆盖 `getDrops`：

```java
@Override public List<ItemStack> getDrops(BlockState state, LootParams.Builder params) {
    return List.of();
}
```

剩余食物只由 `PlaceableFoodBlockEntity.onRemove → dropContents()` 负责，避免整块与切片双掉。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,926,691 bytes
SHA-256 FD0C3C2AC27D78E863BC3B5B5494C93EEFC96E3DC6D8BACB328C7516CF5AB6F9
```

## 4. 未完成

- 未实机；
- 未验证爆炸/活塞/精准采集边界。
