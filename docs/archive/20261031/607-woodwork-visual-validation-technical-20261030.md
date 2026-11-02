# 607 木工视觉对齐静态验证脚本技术分析

> 日期：2026-10-30
> 状态：**静态验证 PASS；未实机**
> 约束：不实机、不推送。

## 1. 目的

为 OPEN-011 的 TFC 20 木材视觉对齐建立可重复验证。

## 2. 检查项

`validate_woodwork_visuals.py`：

- 3 个共享模型（log/half/quarter）的 `elements` 与 `credit` 必须与 TFCW 原版完全一致；
- 20 木材 ×3 类型 = 60 行：
  - blockstate variants 键集合一致；
  - item model parent 一致；
  - per-wood model 的每个 texture 值，按 `tfcwoodwork:` → `tfcagricultureplus:` 归一化后一致。

## 3. 结果

```text
rows 60
problems 0
PASS: TFC woodwork visual parity
```

## 4. 边界

- 只验证 TFC 20 木材；
- AFC 14 木材仍是风格扩展；
- 不验证实机渲染/交互/音效。
