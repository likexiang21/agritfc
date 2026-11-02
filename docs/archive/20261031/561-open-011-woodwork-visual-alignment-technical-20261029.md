# 561 OPEN-011 木工视觉对齐 TFCW 原版技术分析

> 日期：2026-10-29
> 状态：**静态视觉对齐完成（TFC 20 木材）；AFC 为扩展；未实机**
> 约束：视觉可用，但不做大面积贴图重绘。

## 1. 实现方式

不复刻、不重绘：

- 直接复用 TFC Woodworking 1.2.4 的 **MIT** 资源：
  - 3 个共享 block model；
  - 60 个 per-wood block model；
  - 60 个 blockstate；
  - 60 个 item model；
  - 60 个 item 图标 PNG；
  - 20 个 `log_inner` PNG。
- 命名空间替换：`tfcwoodwork:` → `tfcagricultureplus:`。

## 2. 代码/状态对齐

`TimberPieceBlock` 改为：

- `debarked_log`：无 `facing`；
- `debarked_half` / `debarked_quarter`：保留 `facing` 四向；
- 形状：
  - log：`1..15`
  - half：`1..15 × 5..11`
  - quarter：`5..11`
- 与 TFCW 原 blockstate 对齐。

## 3. 对照结果

脚本：`compare_woodwork_models.py`

TFC 20 木材 ×3 类型：

```text
rows 60
blockstate key differences   0
item parent differences      0
model parent differences     60（仅命名空间）
texture differences          40（仅 inner 命名空间）
```

即：

- blockstate variants 完全一致；
- item model parent 完全一致；
- block model parent 仅从 `tfcwoodwork:` 换成 B 命名空间；
- half/quarter 的 `inner` 纹理仅命名空间替换；
- 其余纹理与 TFCW 原版相同。

## 4. AFC 扩展

AFC 14 木材没有 TFCW 原资源：

- block model 使用 `afc:block/wood/sheet` / `log_top`；
- 没有 AFC 专用 debarked item 图标，item model 暂用 block parent；
- 因此 **不是原版对齐**，只是风格一致扩展。

## 5. 校验

```text
gradle build BUILD SUCCESSFUL
blockstates 539 / models 3689 / textures 151
final_static_audit problems 0
static_resource_audit problems 0
```

## 6. 未完成

- 未实机查看渲染/朝向；
- AFC item 图标仍缺；
- 未做 TFCW 交互/音效逐项对照。
