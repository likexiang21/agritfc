# 662 代码筛查：锅可直接加入腐烂食材

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`CookingPanBlockEntity.isItemValid` 已拒绝腐烂食物：

```java
return FoodCapability.has(stack) && !FoodCapability.isRotten(stack);
```

但玩家右键路径 `PanInteractions.interact` 调用的是：

```java
if (FoodCapability.has(held)) {
    if (pan.addIngredient(held)) { ... }
}
```

`CookingPanBlockEntity.addIngredient` 只检查 `FoodCapability.has`，没有检查 `isRotten`，绕过 `isItemValid`，可直接把腐烂食材放进锅。

## 2. 修复

`addIngredient` 增加：

```java
if (!FoodCapability.has(held) || FoodCapability.isRotten(held)) return false;
```

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,925,999 bytes
SHA-256 DB732F09968AE49D1EF97EC076EE59DBA789C902005E2778E0F1BE491E3030D3
```

## 4. 未完成

- 未实机；
- 未验证腐烂食材在自动化路径中的表现。
