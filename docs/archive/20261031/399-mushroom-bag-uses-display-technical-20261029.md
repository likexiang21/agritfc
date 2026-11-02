# 399 菌包使用次数显示 P0-BD 技术分析

> 日期：2026-10-29
> 目标：在菌包温度适宜提示中显示已使用次数/上限。
> 约束：不推送；不伪造；未实机。

## 1. 修改

`MushroomBagBlock.useWithoutItem` 的 growing 消息：

```java
Component.translatable("message...growing")
    .append(Component.literal(" (" + bag.uses() + "/" + MAX_USES + ")"))
```

显示示例：

```text
Colonising at a suitable temperature (0/3)
温度适宜，正在定殖 (0/3)
```

## 2. 测试

```text
PASS: 393 crop P0 checks
PASS: B data item refs 0
gradle compileJava
BUILD SUCCESSFUL
```

## 3. 风险

- 未实机；
- 只在空手右键时显示；
- 没有 tooltip；
- 次数文本未本地化（数字/斜杠）。
