# 354 蘑菇菌包产出范围 P0-AG 技术分析

> 日期：2026-10-29
> 目标：把菌包固定 `2 + random(3)` 的产出改为按 11 种可栽培蘑菇区分的最小/最大产量。
> 约束：不推送；不伪造；未实机。

## 1. 数据

| 物种 | min | max |
|---|---:|---:|
| oyster | 3 | 4 |
| shiitake | 2 | 3 |
| button | 3 | 4 |
| enoki | 3 | 4 |
| wood_ear | 2 | 3 |
| reishi | 1 | 2 |
| lions_mane | 1 | 2 |
| maitake | 2 | 3 |
| king_oyster | 2 | 3 |
| shimeji | 3 | 4 |
| turkey_tail | 1 | 2 |

## 2. 代码

- `MushroomSpecies.bagMinYield()/bagMaxYield()`；
- `MushroomBagBlock.harvest` 使用：

```text
min + random(max - min + 1)
```

- 自然专用 4 种不会进入 harvest 路径。

## 3. 测试

```text
PASS: 342 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
```

新增 11 组 min>0、max>=min 校验。

## 4. 风险

- 未实机；
- 数值未平衡；
- 没有环境/物种产出上限；
- 自然专用仍无替代；
- 不能宣称蘑菇链完成。
