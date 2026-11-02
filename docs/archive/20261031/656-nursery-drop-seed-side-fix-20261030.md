# 656 代码筛查：育苗盘客户端也会掉落种子

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`NurseryTrayBlock.onRemove` 在客户端/服务端都会调用：

```java
tray.dropSeed();
```

`NurseryTrayBlockEntity.dropSeed` 原来只检查：

```java
if (!seed.isEmpty() && level != null) { ... }
```

没有检查 `level.isClientSide()`。方块在客户端被移除时，客户端也会：

- `Containers.dropItemStack` 生成一个纯客户端物品实体；
- 清空客户端 BE 的 seed 字段。

造成客户端幽灵掉落、客户端状态与服务端不一致。

## 2. 修复

```java
if (level == null || level.isClientSide()) {
    return;
}
```

只由服务端负责掉落和清空。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,925,941 bytes
SHA-256 4C8E68A60A83DE603B408A17A17CED78049DD9B5D75CE878F8E98FE2D2D4CB7E
```

## 4. 未完成

- 未实机；
- 未验证育苗盘破坏/取出全路径。
