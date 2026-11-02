# 465 未成熟作物掉落修复 P0-CJ 工作报告

> 日期：2026-10-29
> 状态：**修复并实机确认；未推送、未提交远程**
> 范围：15 香料 + 草莓战利品表 age=7 条件。

## 1. 完成内容

- 定位未成熟仍掉产品；
- 修改 16 个 loot table；
- 构建/资源校验通过；
- 实机复测：
  - immature basil/strawberry 无掉落；
  - mature basil 正常掉 waste/product/seed；
- 恢复环境。

## 2. 结果

```text
IMMATURE_BASIL_GONE
IMMATURE_STRAWBERRY_GONE
MATURE_BASIL_GONE
dropped spice_waste/basil
dropped spice/basil
dropped spice_seed/basil
```

## 3. 未完成

- 其他香料物种逐一；
- 概率/数量；
- creative；
- 旧存档。

## 4. 风险

- 修改了全部 16 个 loot table，需要后续全量采样；
- debug 命令仍需移除/加开关。
