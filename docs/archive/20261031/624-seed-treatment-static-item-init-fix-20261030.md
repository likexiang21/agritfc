# 624 代码筛查：种子处理静态物品初始化缺陷（OPEN-016）

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`SeedTreatmentHandler` 原来：

```java
private static final Item COMPOST =
    BuiltInRegistries.ITEM.get(ResourceLocation.fromNamespaceAndPath("tfc", "compost"));
private static final Item WOOD_ASH = ...;
private static final Item LIME = ...;
```

该类的 `onRightClickItem` 方法引用在 `TFCAgriculturePlus` 构造期间被注册：

```java
NeoForge.EVENT_BUS.addListener(SeedTreatmentHandler::onRightClickItem);
```

这会在**模组构造阶段**触发类初始化，而物品注册表此时尚未完成。
`BuiltInRegistries.ITEM.get(...)` 很可能返回 `minecraft:air`，并被永久保存在静态字段中。

### 后果

- 湿草处理能生效；
- `tfc:compost`、`tfc:powder/wood_ash`、`tfc:powder/lime` 可能永远匹配不到；
- 属于本模组代码问题，不是玩家/其它模组问题。

## 2. 修复

删除静态 `Item` 字段，在 `onRightClickItem` 内按实际事件时间解析：

```java
final Item compost = BuiltInRegistries.ITEM.get(
    ResourceLocation.fromNamespaceAndPath("tfc", "compost"));
final Item woodAsh = ...;
final Item lime = ...;
```

这样只在玩家实际右键、注册表已经完成后解析物品。

## 3. 扫描

全项目扫描：

```text
static final Item  → 0
static final Block → 0
```

未发现其它同类静态注册对象。

## 4. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,921,535 bytes
SHA-256 14C986E224FD43F2FF862C7D07C40F0A40FAFF744071A9FCED0E657B2598832D
```
