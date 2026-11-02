# 420 实机树木生长验证 P0-BN 技术分析

> 日期：2026-10-29
> 目标：验证 B 坚果/香料树苗在真实客户端中从 stage 0 长成树干+树冠。
> 约束：不推送；不伪造；测试后恢复环境。

## 1. 测试方式

临时数据包 `runtime-tree-growth`：

- load：`randomTickSpeed 1000`，5s 后 place；
- place：
  - `minecraft:dirt` + `nut_sapling/pistachio`；
  - `minecraft:dirt` + `spice_sapling/cinnamon`；
- 300 tick 后 check：
  - `~2 ~ ~ tfc:wood/log/oak`；
  - `~4 ~ ~ tfc:wood/log/oak`；
  - `~2 ~4 ~ nut_leaves/pistachio`；
  - `~4 ~4 ~ spice_leaves/cinnamon`；
- cleanup 恢复 randomTickSpeed。

## 2. 结果

check 函数执行：

```text
RUNTIME_TREE_CHECK
```

但没有：

```text
OK_NUT_TREE_TRUNK
OK_SPICE_TREE_TRUNK
OK_NUT_TREE_CANOPY
OK_SPICE_TREE_CANOPY
```

所以本轮**没有树生长证据**。

## 3. 解释边界

- 不能据此判定树生成失败；
- 检查位置/树高/树苗是否被移除都未确认；
- 需要立即 `execute if block` 检查树苗是否还在；
- 需要更长/多次检查；
- 本轮只确认 load/place/check 调度本身能执行。

## 4. 证据

```text
mod_rebuild/docs/audit/runtime-tree-growth-20261029.log
```

## 5. 风险

- 15s/randomTickSpeed 1000 对树生成可能仍不足；
- 树苗可能因 canSurvive/区块状态被移除；
- 坐标假设可能错误；
- 测试后已恢复旧 jar/options、删除数据包。
