# 385 蘑菇菌包 TFC 气候温度 P0-AW 技术分析

> 日期：2026-10-29
> 目标：把菌包温度判断从 vanilla biome base temperature 改为 TFC 气候温度。
> 约束：不推送；不伪造；未实机。

## 1. 修正

原实现：

```java
level.getBiome(pos).value().getBaseTemperature()
```

新实现：

```java
Climate.getAverageTemperature(level, pos)
Climate.fromVanilla(species.preferredTemperature())
Climate.fromVanilla(0.25F)
```

比较：

```text
abs(tfcTemp - fromVanilla(preferred)) <= fromVanilla(0.25)
```

## 2. 为什么

- TFC 有自己的温度尺度；
- vanilla biome base temperature 不能代表 TFC 季节/海拔/气候模型；
- `Climate.fromVanilla` 用于把原 0.30–0.60 偏好映射到 TFC 尺度。

## 3. 测试

```text
PASS: 393 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
```

## 4. 风险

- 未实机；
- `Climate.fromVanilla` 的映射/尺度未实机核对；
- 0.25 容差映射后可能过宽/过窄；
- 极端 TFC 气候仍可能不推进；
- 没有玩家提示。
