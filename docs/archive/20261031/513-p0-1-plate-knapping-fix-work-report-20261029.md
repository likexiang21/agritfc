# 513 P0-1 陶盘 knapping 唯一化工作报告

> 日期：2026-10-29
> 状态：**knapping 冲突静态修复；未实机**
> 范围：P0-1。

## 1. 完成

- 将 `unfired_plate.json` 改为唯一 5×5 clay pattern；
- 碰撞扫描确认 `tfc:clay` 无重复；
- `gradle build` 成功。

## 2. 证据

- `recipe/knapping/ceramic/unfired_plate.json`
- `find_knapping_collisions.py`
- 构建成功

## 3. 未完成

- 碗重复（OPEN-009）；
- 工作方块配方（OPEN-004）；
- 名称（OPEN-005）；
- 实机（不执行）。
