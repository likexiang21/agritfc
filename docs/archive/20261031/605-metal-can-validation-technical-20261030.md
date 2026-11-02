# 605 金属罐静态验证脚本技术分析

> 日期：2026-10-30
> 状态：**静态验证 PASS；未实机**
> 约束：不实机、不推送。

## 1. 目的

为 OPEN-010 的 19 个金属罐建立可重复静态验证。

## 2. 检查项

`validate_metal_cans.py`：

- 19 个 `models/item/metal_can/*.json`；
- loader = `tfc:fluid_container`；
- `base` = `tfc:item/metal/sheet/<metal>`；
- `fluid` = `tfc:item/metal/bucket/overlay`；
- base / overlay 贴图在 TFC jar 中存在；
- 中英语言均有：
  - `item.tfcagricultureplus.metal_can.<metal>`
  - `item.tfcagricultureplus.metal_can.<metal>.filled`
- 流体标签 `data/tfcagricultureplus/tags/fluid/metal_can_fluids.json` 存在。

## 3. 结果

```text
metal can models 19
tag values 2
problems 0
PASS: metal can models
```

## 4. 边界

- 只验证模型/语言/贴图引用；
- 不验证实际装入/倒出/图标变化；
- 未实机。
