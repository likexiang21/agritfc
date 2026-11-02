# 412 实机注册烟测 P0-BJ 技术分析

> 日期：2026-10-29
> 目标：在真实客户端进入世界后，用数据包 load function 验证 B 方块/物品注册是否可被命令系统识别。
> 约束：不推送；不伪造；测试后删除测试数据包并恢复游戏环境。

## 1. 测试方式

在 `saves/tfctest/datapacks/runtime-crop-test` 放临时数据包：

- `pack.mcmeta`；
- `data/minecraft/tags/function/load.json`；
- `data/runtime_crop_test/function/load.mcfunction`。

load function 执行：

- `setblock` 各种 B 方块；
- `execute if block ... run say OK_...`；
- `summon minecraft:item` 各种 B 物品；
- `say RUNTIME_CROP_TEST_START/DONE`。

数据包自动加载，命令输出进入服务器日志。

## 2. 烟测结果

成功识别并 `say`：

```text
OK_BLOCK_NURSERY
OK_BLOCK_STRAWBERRY
OK_BLOCK_NUT_LEAVES
OK_BLOCK_SPICE_LEAVES
OK_BLOCK_WILD_MUSHROOM
OK_BLOCK_TRELLIS
OK_BLOCK_NUT_SAPLING
OK_BLOCK_MUSHROOM_BAG
OK_BLOCK_SAFFRON
```

这些覆盖：

- 育苗盘；
- 草莓普通作物；
- 坚果/香料树叶；
- 野生蘑菇；
- 香料支架；
- 坚果幼苗；
- 菌包；
- saffron 作物。

## 3. 未确认项

以下 setblock 未通过 `execute if block`：

- `spice_crop/basil`；
- `spice_crop/cardamom`；
- `spice_sapling/cinnamon`。

这不是“注册失败”的结论：这些方块有 `canSurvive`，而测试位置/支撑方块在 load function 里可能是无效的。需要后续用正确的 farmland/dirt 支撑再测。

## 4. 其他证据

- 世界加载成功；
- 无 Registry loading errors；
- 无 B recipe parse error；
- 测试日志：

```text
mod_rebuild/docs/audit/runtime-smoke-20261029.log
```

## 5. 风险

- smoke test 只覆盖 setblock/execute；
- 支撑方块测试不可靠；
- 没有真实种植/生长/收获；
- 测试数据包已删除；
- 游戏环境已恢复。
