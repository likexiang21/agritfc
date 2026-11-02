# 650 代码筛查：盘子方块实体没有客户端同步

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`ServingPlateBlockEntity` 直接继承 `BlockEntity`，而盘子渲染器 `ServingPlateBlockEntityRenderer` 依赖：

```java
final PanDishData dish = PanDishData.read(be.plateStack());
```

`setPlateStack` 只调用：

```java
setChanged();
level.sendBlockUpdated(...);
```

- `setChanged` 只标记保存；
- `sendBlockUpdated` 只同步方块状态；
- 没有 `getUpdatePacket` / `getUpdateTag`，客户端不会收到 `plateStack`。

结果：服务端盘子上有菜，客户端渲染器读到空 `plateStack`，菜肴不可见。

## 2. 修复

改为继承 TFC 的 `TFCBlockEntity`：

```java
public final class ServingPlateBlockEntity extends TFCBlockEntity
```

`TFCBlockEntity` 提供：

- `getUpdatePacket()`；
- `getUpdateTag()`，内部 `saveCustomOnly`；
- `markForSync()`。

`setPlateStack` / `clearPlate` 改为 `markForSync()`，不再手动 `sendBlockUpdated`。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,926,030 bytes
SHA-256 3128FA41B9A30EEECB2B39CE22084F76656DB5CF41AF8540BCC9978CC549EC39
```

## 4. 未完成

- 未实机；
- 未验证盘子重载、破坏、换菜全路径。
