# 342 蘑菇菌包物种时间 P0-AA 技术分析

> 日期：2026-10-29
> 目标：把菌包固定 1200 tick 改为 11 种可栽培蘑菇各自的实际殖民时间。
> 约束：不推送；不伪造；未实机。

## 1. 数据

`MushroomSpecies.cultivationTicks()`：

| 物种 | tick |
|---|---:|
| oyster | 1200 |
| shiitake | 1600 |
| button | 1800 |
| enoki | 1400 |
| wood_ear | 1300 |
| reishi | 2400 |
| lions_mane | 2000 |
| maitake | 2200 |
| king_oyster | 1800 |
| shimeji | 1500 |
| turkey_tail | 2000 |

自然专用 4 种返回 0：

```text
porcini · morel · chanterelle · black_truffle
```

## 2. 代码

- `MushroomSpecies` 使用 `Map.ofEntries` 保存 11 条时间；
- `MushroomBagBlockEntity` 使用 `species.cultivationTicks()`，不再用固定常量；
- 自然专用物种在菌包交互层仍会被拒绝，不会进入殖民阶段。

## 3. 测试

纯 Java：

```text
PASS: 300 crop P0 checks
```

新增：

- 11 种可栽培；
- 4 种自然专用；
- 11 种 time > 0；
- 4 种自然专用 time = 0。

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

## 4. 风险

- 未实机；
- 时间数值未平衡；
- 没有温度/湿度/光照差异；
- 没有按物种改变产出数量；
- 自然专用 4 种仍未提供任何栽培替代路径。
