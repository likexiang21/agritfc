# 460 收获掉落物 ID 实机验证 P0-CH 技术分析

> 日期：2026-10-29
> 目标：读取玩家破坏成熟作物后的实际掉落物 ID/数量。
> 约束：不推送；不伪造；调试命令为临时测试入口。

## 1. 测试

干净存档：

- farmland + `spice_crop/basil[age=7]`；
- farmland + `crop/strawberry[age=7]`；
- 玩家生存；
- `tfcplusdebug_harvest` 破坏；
- 80t 后 `tfcplusdebug_drops` 遍历附近 ItemEntity 并写日志。

## 2. 实机掉落

```text
dropped tfcagricultureplus:seeds/strawberry x1
dropped tfcagricultureplus:spice/basil x1
dropped tfcagricultureplus:spice_seed/basil x1
dropped tfc:food/strawberry x1
dropped tfcagricultureplus:crop_waste/strawberry x1
```

同时：

```text
DROPS_BASIL_GONE
DROPS_STRAWBERRY_GONE
```

## 3. 结论

玩家破坏路径实际产出：

- strawberry：种子 + TFC 草莓食品 + B crop_waste；
- basil：B spice_seed + B spice 产品；
- 两个作物方块都被移除。

## 4. 未确认

- 是否每次数量/概率都正确；
- 是否缺少 basil 对应的 waste；
- 全部物种；
- 未成熟保护/creative 分支。

## 5. 证据

```text
mod_rebuild/docs/audit/runtime-harvest-drops-20261029.log
```
