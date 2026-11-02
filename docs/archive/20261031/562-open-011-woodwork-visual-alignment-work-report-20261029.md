# 562 OPEN-011 木工视觉对齐 TFCW 原版工作报告

> 日期：2026-10-29
> 状态：**静态视觉对齐完成（TFC 20 木材）；AFC 为扩展；未实机**

## 1. 完成

- 复用 TFCW 原版共享模型/blockstate/item model；
- 复制 TFCW item 图标与 log_inner 纹理；
- `TimberPieceBlock` 恢复 TFCW 的 facing 规则；
- TFC 20 木材的 blockstate/item parent 差异为 0；
- AFC 14 木材使用 AFC sheet/log_top 风格扩展。

## 2. 校验

```text
blockstate key differences 0
item parent differences 0
model parent/texture differences 仅命名空间
final_static_audit problems 0
static_resource_audit problems 0
gradle build BUILD SUCCESSFUL
```

## 3. 未做

- 未实机；
- AFC item 图标缺失；
- TFCW 交互/音效未逐项对照。
