# 383 蘑菇菌包温度约束 P0-AV 技术分析

> 日期：2026-10-29
> 目标：菌包不再在任意温度下都推进殖民，增加物种适宜温度范围。
> 约束：不推送；不伪造；未实机。

## 1. 数据

`MushroomSpecies.preferredTemperature()`：

| 物种 | 温度 |
|---|---:|
| enoki | 0.30 |
| button / lions_mane / maitake / shimeji | 0.40 |
| oyster / shiitake / king_oyster | 0.50 |
| wood_ear / reishi / turkey_tail | 0.60 |
| 自然专用 4 种 | 0.00 |

容忍范围：

```text
abs(biomeTemperature - preferred) <= 0.25
```

## 2. 行为

`MushroomBagBlockEntity` stage=1：

- 读取 `level.getBiome(pos).value().getBaseTemperature()`；
- 不适宜时直接返回，不推进 progress；
- 适宜时继续殖民计时。

## 3. 测试

```text
PASS: 393 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
```

新增 11 条 preferred temperature 自校验。

## 4. 风险

- 未实机；
- 用 vanilla biome base temperature，不是 TFC 完整气候；
- ±0.25 未平衡；
- 极端群系下菌包可能永远不推进；
- 没有提示玩家温度不适。
