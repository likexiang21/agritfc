# 544 OPEN-011 木工模型/方块状态逐项对照技术分析

> 日期：2026-10-29
> 状态：**静态对照完成；需要视觉/几何重做才能对齐**
> 约束：用户明确不处理视觉；本轮不改模型/贴图。

## 1. 对照范围

TFC Woodworking 1.2.4：

- 20 个 TFC 木材；
- `debarked_log` / `debarked_half` / `debarked_quarter`；
- 每个 3 类资源：
  - blockstate；
  - block model；
  - item model。

共 20 × 3 × 3 = **180 个资源对照点**，实际比较 60 组（3 类 × 20 木材）。

## 2. 对照结果

| 项目 | 不同数量 |
|---|---:|
| blockstate variants | 20 / 20 |
| block model parent | 60 / 60 |
| block model textures | 60 / 60 |
| item model parent | 60 / 60 |

### 典型差异

B `debarked_log/acacia`：

```json
"variants": {
  "facing=north": ..., "facing=east": ..., ...
}
```

TFCW 原版：

```json
"variants": { "": { "model": "tfcwoodwork:block/debarked_log/acacia" } }
```

B 多出 `facing` 四向。

B block model：

```json
"parent": "tfcagricultureplus:block/timber/debarked_log",
"textures": {
  "side": "tfc:block/wood/stripped_log/acacia",
  "top": "tfc:block/wood/stripped_log_top/acacia"
}
```

TFCW：

```json
"parent": "tfcwoodwork:block/debarked_log/debarked_log",
"textures": {
  "side": "tfc:block/wood/sheet/acacia",
  "top": "tfc:block/wood/log_top/acacia"
}
```

B item model 直接 parent 方块模型；TFCW 使用 `item/generated` 图标。

## 3. 结论

- **配方**：40 条原版配方结构一致（P2-2 已证）。
- **模型/贴图/朝向**：B 与 TFCW 原版存在系统性差异，用户“木工移植不尊重原内容”的批评在模型层面**成立**。
- 要对齐必须重做：
  - blockstate 朝向；
  - block model 父级与几何；
  - texture 选择（sheet/log_top vs stripped_log）；
  - item model 图标。
- 这些属于**视觉/几何**工作，本轮按用户约束不执行。

## 4. 未完成

- 模型/贴图/朝向对齐；
- 交互/音效逐项；
- 实机。
