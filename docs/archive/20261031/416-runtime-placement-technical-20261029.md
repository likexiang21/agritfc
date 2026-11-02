# 416 实机玩家支撑放置验证 P0-BL 技术分析

> 日期：2026-10-29
> 目标：用真实玩家坐标 + farmland/dirt 支撑，验证之前 setblock 失败的香料作物/树苗确实可放置。
> 约束：不推送；不伪造；测试后恢复环境。

## 1. 测试方式

临时数据包：

- load function 调度 5 秒后执行 `actions`；
- `actions` 使用 `execute as @a at @s` 在玩家脚边放置：
  - `minecraft:farmland` + `spice_crop/basil`；
  - `minecraft:farmland` + `spice_crop/cardamom`；
  - `minecraft:farmland` + `crop/strawberry`；
  - `minecraft:dirt` + `spice_sapling/cinnamon`；
  - `minecraft:dirt` + `nut_sapling/pistachio`；
- 立即 `execute if block` 验证并 `say`；
- 给玩家发 14 种 B 物品。

## 2. 结果

全部通过：

```text
OK_PLAYER_SPICE_BASIL
OK_PLAYER_SPICE_CARDAMOM
OK_PLAYER_STRAWBERRY
OK_PLAYER_SPICE_SAPLING
OK_PLAYER_NUT_SAPLING
RUNTIME_ACTION_DONE
```

日志：

```text
mod_rebuild/docs/audit/runtime-placement-20261029.log
```

## 3. 结论

之前 load function 在固定 y=200 坐标的失败是测试位置/支撑问题，不是注册问题。

真实玩家坐标 + 正确 farmland/dirt 下：

- 香料作物可放；
- 草莓作物可放；
- 香料树苗可放；
- 坚果幼苗可放。

## 4. 边界

- 只验证放置；
- 没有验证生长/成熟/收获；
- 没有验证育苗盘/幼苗/菌包交互；
- 给物品命令没有逐项检查背包；
- 测试后已恢复旧 jar/options 并删除数据包。
