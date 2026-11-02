# 391 菌包使用次数上限 P0-AZ 技术分析

> 日期：2026-10-29
> 目标：可复用菌包增加 3 次使用上限，避免无限产出。
> 约束：不推送；不伪造；未实机。

## 1. 数据

`MushroomBagBlockEntity.MAX_USES = 3`。

字段：

- `uses`；
- `markSpent` 时自增；
- `maxed()`；
- 存档保存/读取 `uses`。

## 2. 行为

- stage 0 接种不增加 uses；
- 每次收获 `markSpent` +1；
- stage 3 重新接种前检查：
  - `maxed()` 时拒绝；
  - 显示 `message.tfcagricultureplus.mushroom_bag.spent`；
  - 不消耗物品。
- 未达上限仍可复用。

## 3. 测试

```text
PASS: 393 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
processResources BUILD SUCCESSFUL
```

## 4. 风险

- 未实机；
- 上限 3 未平衡；
- 没有工具提示显示剩余次数；
- 耗尽后只能破坏/丢弃；
- 自然专用仍拒绝。
