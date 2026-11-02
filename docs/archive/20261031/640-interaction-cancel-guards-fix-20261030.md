# 640 代码筛查：右键/左键处理器未检查已取消事件

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

以下交互处理器在事件已被其它模组/保护逻辑取消后，仍会继续处理：

- `BushRightClickHarvestHandler`
- `DirectSeedPlantingGate`
- `CuttingBoardLeftClickHandler`
- `InWorldRecipeHandler`

共同问题：只检查了 hand / 物品 / 方块，没有检查：

```java
event.isCanceled()
```

## 2. 后果

- 保护区域或其它模组取消右键后，本模组仍可能收获灌木、取消种子种植、处理案板或执行世界内配方；
- 多个处理器叠加时可能产生重复掉落或越权交互。

`InWorldRecipeHandler` 还会在已取消的事件上执行 `setCanceled(true)` / 改方块，影响其它模组的结果。

## 3. 修复

统一在方法开头加入：

```java
if (event.isCanceled()) {
    return;
}
```

覆盖上述 4 个交互入口。

## 4. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,923,366 bytes
SHA-256 15937590B833CC387333E6DA743F57894FCCA22425C2F2E5EE06F89AD3B1A952
```

## 5. 未完成

- 未实机；
- 未验证其它右键交互入口。
