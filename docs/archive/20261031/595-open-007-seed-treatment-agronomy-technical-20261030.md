# 595 OPEN-007 扩展：种子处理接入堆肥/木灰/石灰技术分析

> 日期：2026-10-30
> 状态：**静态实现；未实机**
> 约束：不实机、不推送。

## 1. 背景

`SeedTreatmentHandler` 原来只接受湿草：

```java
if (!offhand.is(WET_GRASS)) return;
next = SeedTreatments.next(current);
```

无法使用 TFC 的堆肥/木灰/石灰。

## 2. 实现

副手物品：

| 副手 | 结果 |
|---|---|
| `tfcagricultureplus:wet_grass` | 前进一阶段 |
| `tfc:compost` | 前进一阶段 |
| `tfc:powder/wood_ash` | 直接到 `DRESSED` |
| `tfc:powder/lime` | 直接到 `DRESSED` |

- 已到 `DRESSED` 时不再消耗；
- 处理结果仍写入 `SEED_TREATMENT` component；
- 育苗盘时间与种植后 Bonemeal 推进沿用 528/529 的机制；
- 没有新增 UI/弹窗。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
json 6484 / bad 0
final_static_audit problems 0
```

## 4. 未完成

- 未实机验证 TFC 物品 ID/右键优先级；
- 未做堆肥/石灰的剂量/次数限制；
- 母株性状仍未实现。
