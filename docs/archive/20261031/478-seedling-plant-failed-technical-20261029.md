# 478 育苗移栽尝试 P0-CQ 技术分析

> 日期：2026-10-29
> 目标：把育苗盘产出的 seedling 放到耕地。
> 约束：不推送；不伪造；测试后恢复环境。

## 1. 测试

- 育苗盘 stage2 + strawberry seed；
- use 育苗盘产出 seedling；
- 调试 `tfcplusdebug_plant_seedling ~4 ~ ~`（目标写成了耕地**上方空气**）；
- 检查 `~4 ~`。

## 2. 结果

```text
SEEDLING_PLANT_AIR
inventory tfcagricultureplus:seedling x1（多个）
```

移栽目标位置仍是空气；seedling 还在背包。

## 3. 判断

`useItemOn` 的 hit 目标是空气，不是下方耕地，所以 `SeedlingItem.useOn` 没有放置作物。

这是**测试目标坐标错误**，不是 seedling 代码失败。

## 4. 下一步

- 目标改为耕地 `~4 ~-1 ~`；
- 再检查上方是否出现 `crop/strawberry`。

## 5. 边界

- 本轮没有移栽证据；
- 没有修改正式代码。
