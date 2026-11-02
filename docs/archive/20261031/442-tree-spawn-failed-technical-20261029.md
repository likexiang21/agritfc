# 442 出生点树冠测试未完成 P0-BY 技术分析

> 日期：2026-10-29
> 目标：把玩家传送到存档出生点（-768,66,528）后验证树干/树冠。
> 约束：不推送；不伪造；测试后恢复环境。

## 1. 测试

临时数据包 `runtime-tree-spawn`：

- 10s 后 `tp` 到出生点；
- 放 nut/spice 树苗；
- 300t 后检查。

## 2. 结果

```text
SPAWN_NUT_PLACED
SPAWN_SPICE_PLACED
SPAWN_AIR_BELOW
RUNTIME_SPAWN_CHECK
```

但没有：

```text
grew ... at ...
SPAWN_*_TRUNK / LEAF
```

## 3. 判断

- 树苗放置成功；
- 本轮 scheduled tick 未产生生长日志；
- 之前 P0-BU 已成功一次树干；
- 当前测试流程（tp/位置变化）与 scheduled tick 不稳定相关。

## 4. 结论

- 树冠仍未验证；
- 不能据此判树代码失败；
- 不再重复同类 tp/清空测试；
- 需要真实玩家正常种植。
