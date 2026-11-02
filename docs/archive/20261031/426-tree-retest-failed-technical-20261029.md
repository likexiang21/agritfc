# 426 树木复测失败分析 P0-BQ 技术分析

> 日期：2026-10-29
> 目标：复测树苗支撑修复后的树生长。
> 约束：不推送；不伪造；测试后恢复环境。

## 1. 测试

临时数据包 `runtime-tree-retest`：

- load：`randomTickSpeed=1000`，`forceload add 1000 1000`，20s 后 place；
- place：玩家平台、dirt 支撑、nut/spice 树苗；
- 300 tick 后 check；
- check 中添加：
  - 树苗是否仍在；
  - stage 0/1/2；
  - dirt 支撑是否仍在；
  - 树干/树冠。

## 2. 结果

```text
RETEST_NUT_PLACED
RETEST_SPICE_PLACED
RUNTIME_TREE_RETEST_CHECK
```

但 check 中连：

```text
RETEST_NUT_DIRT
RETEST_NUT_STILL
RETEST_SPICE_STILL
```

都没有。

## 3. 判断

这不是“树苗被 canSurvive 移除”的证据，因为 **连 dirt 支撑都读不到**。

更可能是：

- `forceload` 目标区块在 check 时不在预期位置/未加载；
- load/place/check 的区块加载时序；
- 测试坐标/维度差异；
- `forceload add 1000 1000` 的坐标语义误用。

## 4. 结论

- 本轮没有树生长证据；
- 不能判定树苗/树代码失败；
- 测试环境本身不可靠；
- 需要改用玩家当前位置 + 同一 `at @s` 的立即检查/延迟检查。

## 5. 证据

```text
mod_rebuild/docs/audit/runtime-tree-retest2-20261029.log
```
