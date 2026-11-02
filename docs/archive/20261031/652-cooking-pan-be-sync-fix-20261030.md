# 652 代码筛查：锅方块实体渲染内容不同步

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`CookingPanBlockEntity` 的 `sync()` 原来只：

```java
setChanged();
level.sendBlockUpdated(worldPosition, state, state, Block.UPDATE_CLIENTS);
```

`sendBlockUpdated` 只同步**方块状态**，不发送 BlockEntity 自定义数据。

而 `CookingPanBlockEntityRenderer` 依赖服务端字段：

```java
be.renderStack(slot) // entries
```

客户端没有收到 `entries`，渲染器看到空列表，**锅里已放的食材不可见**。

## 2. 修复

`CookingPanBlockEntity` 继承自 TFC 的 `TickableInventoryBlockEntity` → `TFCBlockEntity`，使用其同步方法：

```java
private void sync() {
    markForSync();
}
```

`TFCBlockEntity.markForSync()` 会发送 `ClientboundBlockEntityDataPacket` 并 `setChanged()`，`getUpdateTag()` 通过 `saveCustomOnly` 携带 `entries`、`oil`、`solid_oil`、`oil_type`。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,925,928 bytes
SHA-256 85071E106AA81B19988A28C2487434BE5FE16CB37FCD8A8E02166FE48F024946
```

## 4. 未完成

- 未实机；
- 未验证锅盖/油/食材全路径同步。
