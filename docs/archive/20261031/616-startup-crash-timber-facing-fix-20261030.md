# 616 启动崩溃修复：木工朝向属性注册（OPEN-014）

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**
> 日志：`crash-reports/crash-2026-10-30_09.33.00-fml.txt`、`logs/latest.log`

## 1. 崩溃

最新日志：

```text
java.lang.IllegalArgumentException: Cannot set property
DirectionProperty{name=facing, clazz=class net.minecraft.core.Direction,
values=[north, south, west, east]}
as it does not exist in Block{[unregistered]}
```

栈：

```text
TimberPieceBlock.<init>(TimberPieceBlock.java:22)
TimberBlocks.lambda$static$1(TimberBlocks.java:42)
```

## 2. 根因

上一轮为了让 TFCW 原版 `debarked_log` 没有 `facing`，把 `TimberPieceBlock` 改成：

```java
this.directional = pieceKind != 0;
if (directional) {
    registerDefaultState(stateDefinition.any().setValue(FACING, NORTH));
}
```

但 `createBlockStateDefinition` 在 `super(properties)` 构造期间就被调用，
此时子类字段 `directional` 还没有赋值（Java 子类字段在 super 之后初始化），
实际读到的是默认 `false`，所以状态定义里没有 `facing`；
随后构造函数再 `setValue(FACING)` 就抛出：

```text
facing ... does not exist
```

这是**本模组代码问题**，不是用户、不是其它模组。

## 3. 修复

拆成两个类，避免在 `super` 构造期间依赖未初始化字段：

- `TimberPieceBlock`
  - 无 `FACING`；
  - 只用于 `debarked_log`（kind 0）；
  - 形状固定 1..15。
- `DirectionalTimberPieceBlock`
  - 有 `FACING`；
  - 用于 `debarked_half` / `debarked_quarter`（kind 1/2）；
  - 形状按朝向。
- `TimberBlocks` 按 `part` 选择类；
- `weight()` 同时识别两种类；
- `canSurvive` 通过 `isTimberPiece` 同时识别两种类。

## 4. 日志中的次级 NPE

崩溃还列出：

```text
Trying to access unbound value:
tfcagricultureplus:debarked_half/acacia
```

以及：

```text
Trying to access unbound value:
tfcagricultureplus:serving_plate
```

这是因为首个方块注册异常使整个注册事件失败，后续 deferred holder 自然未绑定；
在修复首个异常后应消失，但**仍需启动验证**。

## 5. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar 已迁移到 `mods/`。

## 6. 未完成

- 没有 Java 21 / PCL 可用环境，未实机启动确认；
- 需要用户用 PCL 启动一次，确认无 `Mod loading failures`。
