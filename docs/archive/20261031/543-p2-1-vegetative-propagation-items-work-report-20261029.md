# 543 P2-1 扩展：无性繁殖物品链工作报告

> 日期：2026-10-29
> 状态：**静态实现；未实机**
> 范围：OPEN-007。

## 1. 完成

- 新增 21 个 `propagation_stock/<species>` 物品；
- 覆盖 CORM/TUBER/RHIZOME/CROWN/DIVISION/RUNNER；
- 每个由对应作物产品 1→2 合成；
- 新 item 使用现有作物纹理，不新增贴图；
- `PropagationStockItem` 在耕地放置对应作物 age0；
- 加入创造页。

## 2. 校验

```text
product refs bad 0
crop block refs bad 0
json 6484 / bad 0
item_models 943
final_static_audit problems 0
validate_crop_p0a PASS
gradle build BUILD SUCCESSFUL
```

## 3. 未做

- `hops` 无 food 产品，未纳入；
- 水生作物水田放置；
- 母株性状/育苗/缓苗；
- 实机；
- 视觉。
