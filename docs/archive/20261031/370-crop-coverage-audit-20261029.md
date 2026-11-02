# 370 作物覆盖审计 P0-AO

> 日期：2026-10-29
> 目标：用真实 jar 资源计数核对 A 87、TFC 29、B 43 的代码/资源覆盖，而不是只凭声明。
> 约束：不推送；不伪造。

## 1. A 87

真实资源：

```text
A crop blockstates: 86
B strawberry crop: 1
合计：87
```

校验脚本逐项核对：

- 86 个 `assets/tfcfarmingplus/blockstates/crop/*.json`；
- 对应 86 个 `assets/tfcfarmingplus/models/item/seeds/*.json`；
- B strawberry 的 blockstate/seed/loot 存在。

```text
PASS: A 86 crops + B strawberry = 87; TFC 29 crops/seed models
```

## 2. TFC 29

```text
TFC crop blockstates: 29
TFC seed item models: 29
```

逐项核对通过。

## 3. B 43

| 类别 | 数量 |
|---|---:|
| 香料 | 20 |
| 坚果 | 8 |
| 蘑菇 | 15 |
| 合计 | 43 |

已存在：

- 20 香料 crop/seed/product/waste/ground；
- 8 坚果 nut/shell/ground；
- 15 wild mushroom block/worldgen；
- 菌包 11 可栽培 + 4 自然专用拒绝。

## 4. 其他计数

```text
102 crop_waste
10 bush_waste
15 wild mushrooms
79 nut leaf states
20 spice crops
20 ground spices
8 ground nuts
8 nut shells
```

## 5. 结论

这次审计只能证明**资源/代码覆盖存在**，不能证明：

- 实机行为正确；
- loot 数量平衡；
- TFC/A 原方块全部被替换；
- 香料树/坚果专属树已完成；
- 159 条逐作物验收。

目标仍未完成，继续推进。
