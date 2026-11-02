# 612 废枝叶图标静态验证脚本技术分析

> 日期：2026-10-30
> 状态：**静态验证 PASS；未实机**
> 约束：不实机、不推送。

## 1. 目的

为 OPEN-005 的 crop_waste/bush_waste 图标映射建立可重复验证，防止退回
`tfc:item/straw`。

## 2. 检查项

`validate_waste_icons.py`：

- `models/item/crop_waste/*.json` 82 个；
- `models/item/bush_waste/*.json` 10 个；
- 每个 `layer0`：
  - 不能是 `tfc:item/straw`；
  - 必须带命名空间；
  - 命名空间必须是 TFC/A；
  - 贴图必须存在于对应 jar。

## 3. 结果

```text
crop_waste 82
bush_waste 10
problems 0
PASS: crop/bush waste icons
```

## 4. 边界

- 只验证图标引用；
- 不验证美术质量/实机显示。
