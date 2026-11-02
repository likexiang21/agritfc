# 462 多作物收获实机验证 P0-CI 技术分析

> 日期：2026-10-29
> 目标：同一测试中验证 TFC / A / B 作物的玩家破坏掉落。
> 约束：不推送；不伪造；调试命令为临时测试入口。

## 1. 测试

干净存档：

- `tfc:farmland/mollisol` + `tfc:crop/wheat[age=7]`；
- `tfc:farmland/mollisol` + `tfcfarmingplus:crop/napa_cabbage[age=5]`；
- `minecraft:farmland` + B `spice_crop/basil[age=0]`；
- `minecraft:farmland` + B `crop/strawberry[age=7]`；
- 玩家生存；
- 100t 后 `tfcplusdebug_harvest` 全部破坏；
- 80t 后 `tfcplusdebug_drops` 读取 ItemEntity。

## 2. 实机掉落

```text
tfcagricultureplus:spice/basil x1
tfcagricultureplus:spice_seed/basil x1
tfcagricultureplus:grain_bundle/wheat x1
tfc:seeds/wheat x1
tfcfarmingplus:seeds/napa_cabbage x1
tfcagricultureplus:crop_waste/napa_cabbage x1
```

## 3. 结论

- TFC 小麦：TFC 种子 + **B grain_bundle/wheat**；
- A napa：A 种子 + **B crop_waste/napa_cabbage**；
- B basil：B 种子 + B 产品；
- 四个测试作物方块都被移除。

## 4. 异常/未确认

- 本轮 strawberry 没有出现在掉落日志；上一轮曾确认 strawberry 掉落；
- B immature basil 被移除但没有掉落日志；
- 未确认未成熟保护逻辑；
- 掉落概率/数量未全量核对。

## 5. 证据

```text
mod_rebuild/docs/audit/runtime-harvest-multi-20261029.log
```
