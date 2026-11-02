# 393 自然专用蘑菇提示 P0-BA 技术分析

> 日期：2026-10-29
> 目标：把“自然专用蘑菇不可栽培”从静默失败改成玩家可见提示。
> 约束：不推送；不伪造；未实机。

## 1. 行为

`MushroomBagBlock.useItemOn`：

- 放入的野生蘑菇方块解析为 `MushroomSpecies`；
- `species == null`：保持静默失败；
- `species.naturalOnly()`：
  - 显示 `message.tfcagricultureplus.mushroom_bag.natural_only`；
  - 返回 FAIL；
  - 不消耗物品。

## 2. 语言

```text
This mushroom is natural-only and cannot be cultivated
该蘑菇只能自然生成，无法人工栽培
```

## 3. 测试

```text
PASS: 393 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
processResources BUILD SUCCESSFUL
```

## 4. 风险

- 未实机；
- 只 actionbar 提示；
- 没有区分 4 个自然专用物种；
- 可能被其他右键逻辑抢事件；
- 不改变“不可栽培”的规则。
