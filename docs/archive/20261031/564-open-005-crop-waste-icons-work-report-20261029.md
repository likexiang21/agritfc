# 564 OPEN-005 扩展：作物废枝叶图标差异工作报告

> 日期：2026-10-29
> 状态：**静态视觉映射完成；未实机**

## 1. 完成

- 82 个 `crop_waste` item model 不再共用 `tfc:item/straw`；
- 按物种映射到已有 A/TFC 作物贴图；
- 无新增/重绘 PNG；
- `gradle build` 成功。

## 2. 校验

```text
mapped 82 / missing 0
json 6483 / bad 0
final_static_audit problems 0
static_resource_audit problems 0
```

## 3. 未做

- 未实机；
- 未专门绘制废枝叶图标；
- 未处理视觉细节。
