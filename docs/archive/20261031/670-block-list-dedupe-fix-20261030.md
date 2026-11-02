# 670 代码筛查：方块全量列表重复 drying rack

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`AgricultureBlocks.all()` / `allIds()`：

```java
var result = new ArrayList<>(ALL.values());
result.addAll(DRYING_RACKS.values());
result.addAll(TimberBlocks.ALL.values());
```

但 `registerVariant` 已经把 drying rack 写入 `ALL`：

```java
final DeferredHolder<Block, Block> holder = BLOCKS.register(name, factory);
AgricultureItems.ITEMS.registerSimpleBlockItem(name, holder);
into.put(name, holder);
ALL.put(name, holder);
```

因此：

- `all()` 中每台 drying rack 出现两次；
- 客户端渲染层自检计数被放大；
- `allIds()` 台账重复。

## 2. 修复

不再追加 `DRYING_RACKS`：

```java
var result = new ArrayList<>(ALL.values());
result.addAll(TimberBlocks.ALL.values());
```

`allIds()` 同理，只追加独立注册在 `TimberBlocks.ALL` 的原木件。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,926,105 bytes
SHA-256 E83EDC52ED0A393C2CCCB3DD579147A3FF1601AEFA4831E77DD46AC69C46C8D8
```

## 4. 未完成

- 未实机；
- 未验证客户端自检计数。
