# 428 近玩家树木测试 P0-BR 技术分析

> 日期：2026-10-29
> 目标：在玩家当前位置测试树苗生长，避免绝对坐标区块问题。
> 约束：不推送；不伪造；测试后恢复环境。

## 1. 测试

临时数据包 `runtime-tree-near`：

- load：randomTickSpeed=1000，15s 后 place；
- place：
  - 玩家转 spectator；
  - dirt + nut/spice sapling 放在玩家旁；
- 300 tick 后 check：
  - sapling 是否仍在/stage；
  - 树干/树冠。

## 2. 结果

```text
NEAR_NUT_PLACED
NEAR_SPICE_PLACED
NEAR_NUT_STILL
NEAR_NUT_STAGE0
NEAR_NUT_CANOPY4
NEAR_SPICE_STILL
NEAR_SPICE_CANOPY4
```

树苗仍在，且 **stage0**，说明 15 秒内没有 random tick 推进。

`CANOPY4` 很可能是玩家附近既有的树叶/旧测试残留，而不是本次树生成。

## 3. 关键怀疑

- **gamemode spectator 可能让所在区块不进行正常随机刻**；
- 或 randomTickSpeed 在该会话未生效；
- 或树苗 `randomTick` 没被调用。

## 4. 下一步

- 同一测试里放一个 basil 作为随机刻对照；
- 不用 spectator，改用 adventure/survival + 不移动；
- 检查树苗 stage 0/1/2；
- 再看树冠。

## 5. 结论

- 本轮没有树生成证据；
- 但确认树苗**保留**，不是 canSurvive 立即移除；
- 不能断言树代码失败，也不能完成。
