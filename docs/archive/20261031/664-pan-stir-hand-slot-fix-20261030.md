# 664 代码筛查：副手锅铲搅拌会损坏主手物品

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`CookingPanBlockEntity.stir` 原来：

```java
spatulaStack.hurtAndBreak(1, player, EquipmentSlot.MAINHAND);
```

无论玩家用**主手**还是**副手**拿锅铲，都固定扣主手装备槽。

`PanInteractions.interact` 允许副手锅铲触发搅拌，因此：

- 副手锅铲不消耗耐久；
- 主手物品（可能为空或另一把工具）被错误扣耐久。

## 2. 修复

`stir` 增加 `InteractionHand hand` 参数：

```java
public boolean stir(SpatulaItem spatula, ItemStack spatulaStack,
                    Player player, InteractionHand hand)
```

按实际手选择槽：

```java
final EquipmentSlot slot = hand == InteractionHand.MAIN_HAND
    ? EquipmentSlot.MAINHAND : EquipmentSlot.OFFHAND;
spatulaStack.hurtAndBreak(1, player, slot);
```

`PanInteractions` 传入实际 `hand`。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,926,094 bytes
SHA-256 1AF26FC740A7E17E3F0FD5CD8EC915EC175679118E327219E6BAEDDADFDA0ED7
```

## 4. 未完成

- 未实机；
- 未验证双持锅铲边界。
