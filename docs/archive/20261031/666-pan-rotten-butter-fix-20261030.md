# 666 代码筛查：锅可加入腐烂黄油作油

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`CookingPanBlockEntity.addSolidOil` 只检查：

```java
if (level == null || level.isClientSide() || hasOil() || stack.isEmpty()) return false;
final var key = ...;
if (!namespace firmalife || !path food/butter) return false;
```

没有检查 `FoodCapability.isRotten(stack)`。

Firmalife 黄油是食物，会腐烂；腐烂黄油仍可作为固态油放进锅。

## 2. 修复

```java
if (FoodCapability.isRotten(stack)) return false;
```

与 `isItemValid` / `addIngredient` 的腐烂食物拒绝保持一致。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,926,100 bytes
SHA-256 E5CE3F97B9B7D3FA8BEBDC01B90A030AF49AE8FFAA580C81BB41A36F54F71AFE
```

## 4. 未完成

- 未实机；
- 未验证其它固态油来源。
