# 430 近玩家树木随机刻诊断 P0-BS 技术分析

> 日期：2026-10-29
> 目标：在玩家旁测试树苗，确认是否 random tick 推进 stage。
> 约束：不推送；不伪造；测试后恢复环境。

## 1. 测试

临时数据包 `runtime-tree-near`：

- `randomTickSpeed=1000`；
- 玩家转 spectator；
- 玩家旁 dirt + nut/spice sapling；
- 300 tick 后 check。

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

- 树苗保留；
- stage 仍 0；
- 没有 trunk 标记；
- canopy4 不能归因，可能是既有方块。

## 3. 判断

树苗**没有 random tick 推进**。可能：

- spectator 区块不进行随机刻；
- gamerule 未生效；
- 树苗 randomTick 未被调用；
- 测试环境 tick 暂停。

## 4. 必需对照

同一测试中加一个 basil 作物：

- 若 basil 成熟而 sapling 仍 stage0 → 树苗 randomTick 实现问题；
- 若 basil 也不长 → 测试环境/random tick 问题；
- 再用非 spectator 模式复测。

## 5. 结论

- 没有树生成证据；
- 不能断言树代码失败；
- 测试环境仍不可靠。
