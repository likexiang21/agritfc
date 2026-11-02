# 585 OPEN-007 静态覆盖评估：繁殖方式 / 种子处理 / 气候接口

> 日期：2026-10-30
> 状态：**静态覆盖；母株性状仍缺；未实机**
> 约束：不实机、不推送。

## 1. 已实现

### 繁殖方式

- `CropPropagation` 8 种：
  `SEED_DIRECT / NURSERY / RUNNER / TUBER / RHIZOME / CORM / CROWN / DIVISION`；
- 82 个 crop-waste 作物全部显式分类；
- 21 个 `propagation_stock/<species>` 物品；
- 产品 1→2 合成；
- 耕地/水源放置；
- 水生作物使用 `getStateForPlacement` 保留 fluid 属性。

### 种子处理（农艺管理的一部分）

`SeedTreatments`：

```text
SOAKED → GERMINATED → DRESSED
```

- 湿草副手右键种子推进阶段；
- 育苗盘时间 1200 → 600 tick；
- 种植后按阶段给 1/2/3 次 `BonemealableBlock` 生长推进；
- 处理阶段存入 `SEED_TREATMENT` component，随幼苗传递。

### 温湿度

- 菌包使用 TFC `Climate.getAverageTemperature`；
- `Climate.fromVanilla` 做温度换算；
- 没有自定义气候系统。

## 2. 仍缺

- **母株性状**：没有 DataComponent 记录亲本产量/抗性/生长势；
- **温湿度扩展**：菌包只判温度，不判湿度；
- **完整农艺**：间苗、培土、搭架、打顶、除草、施肥没有逐项实现；
- **种子处理原料**：目前只有湿草，未接入堆肥/石灰/灰。

## 3. 结论

OPEN-007 不能标记为完成：

- 繁殖物品链和种子处理已经落地；
- 母株性状/完整农艺仍缺；
- 未实机。
