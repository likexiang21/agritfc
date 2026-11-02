# 387 菌包温度提示 P0-AX 技术分析

> 日期：2026-10-29
> 目标：菌包在温度不适宜时给玩家可见反馈，而不是静默不推进。
> 约束：不推送；不伪造；未实机。

## 1. 行为

`MushroomBagBlock.useWithoutItem`：

- 空手右键 stage=1 的菌包；
- 读 `MushroomBagBlockEntity.species()`；
- 用 TFC `Climate.getAverageTemperature` + `Climate.fromVanilla` 判断；
- 温度偏低：
  `message.tfcagricultureplus.mushroom_bag.too_cold`；
- 温度偏高：
  `...too_hot`；
- 适宜：
  `...growing`。

三种消息只在服务端发送，actionbar 显示。

## 2. 语言

```text
Too cold for this mushroom
Too hot for this mushroom
Colonising at a suitable temperature

温度太低，蘑菇无法生长
温度太高，蘑菇无法生长
温度适宜，正在定殖
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
- 只空手右键触发；
- 温度映射未实机核对；
- 没有 GUI 状态条；
- 可能被其他右键逻辑抢事件。
