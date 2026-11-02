# 660 代码筛查：锅的油勺只模拟不转移

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`PanInteractions.scoopOil` 原来：

```java
final FluidStack moved = FluidUtil.tryFluidTransfer(
    handler, pan.oilTank(), CookingPanBlockEntity.OIL_REQUIRED, false);
return !moved.isEmpty();
```

`tryFluidTransfer` 第 4 个参数是 `doTransfer`：

- `false` = 只模拟，不真正转移；
- `true` = 实际转移。

因此使用锅铲从副手油容器“取油”时：

- 模拟返回非空，函数返回成功；
- 玩家油容器没有减少；
- 锅的油罐没有增加。

造成无消耗反复触发、油料实际不进入锅。

## 2. 修复

```java
final FluidStack moved = FluidUtil.tryFluidTransfer(
    handler, pan.oilTank(), CookingPanBlockEntity.OIL_REQUIRED, true);
```

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,925,998 bytes
SHA-256 997E6C69AE6E836CD356AB7F31386B758162CD274D97625EDF1F4314F52F3A84
```

## 4. 未完成

- 未实机；
- 未验证不同油容器/油量边界。
