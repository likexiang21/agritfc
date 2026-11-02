# 521 P1-1 金属罐液体显示工作报告

> 日期：2026-10-29
> 状态：**静态显示修复完成；未实机**
> 范围：P1-1。

## 1. 完成

- 19 个 metal can item model 改用 `tfc:fluid_container`；
- 新增 19 × 2 个 `.filled` 名称键；
- 未改容量/capability/tag；
- `gradle build` 成功。

## 2. 校验

```text
lang 1080 / 1080
missing 0 / extra 0
json 6425 / bad 0
final_static_audit problems 0
```

## 3. 未做

- 未实机验证装入/倒出；
- 未改占位贴图（视觉问题）；
- 未扩流体 tag；
- 未检查 TFC loader 在客户端实际渲染。
