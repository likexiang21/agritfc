# 512 P0-1 陶盘 knapping 唯一化技术分析

> 日期：2026-10-29
> 状态：**静态修复完成；未实机**
> 约束：不实机、不处理视觉、不推送。

## 1. 问题

B `unfired_plate` 与 TFC `unfired_bowl`：

- 同 `tfc:clay`；
- 同 5×5 pattern：
  ```text
  "#   #"
  " ### "
  "     "
  "#   #"
  " ### "
  ```

TFC bowl 输出 4 个未烧制碗，B plate 输出 1 个未烧制盘；
`tfc:knapping` 的 `matches` 只检查 knapping_type + pattern + 可选 ingredient，两个配方会冲突。

## 2. 新 pattern

```json
"pattern": [
  " ### ",
  "#####",
  " ### ",
  "     ",
  "     "
]
```

- 仍为 `tfc:clay`；
- 仍为一次陶盘坯；
- 形状更接近平盘；
- 结果保持 `tfcagricultureplus:ceramic/unfired_plate` ×1。

## 3. 冲突验证

使用 `find_knapping_collisions.py` 扫描：

- B 本地 knapping；
- TFC jar；
- A jar（若存在）。

新 pattern 在所有 `tfc:clay` pattern 中无碰撞。

剩余碰撞：

- B 7 个 pestle 共用 `tfc:rock` pattern（ingredient 不同，OPEN-013）；
- TFC 自身岩石工具重复 pattern（有 ingredient 区分）。

## 4. 构建

```text
gradle build BUILD SUCCESSFUL
```

## 5. 未完成

- 未实机验证盘/碗配方选择；
- 未处理重复碗（OPEN-009）；
- 未处理陶盘流程与陶罐参考（OPEN-006 的流程部分）；
- 视觉不改。
