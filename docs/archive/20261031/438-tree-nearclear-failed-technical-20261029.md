# 438 开阔区树冠测试未完成 P0-BW 技术分析

> 日期：2026-10-29
> 目标：在玩家附近清空树冠空间，验证树叶生成。
> 约束：不推送；不伪造；测试后恢复环境。

## 1. 测试

临时数据包 `runtime-tree-nearclear`：

- 玩家旁 `fill` 清空 y+1..y+12；
- 放 nut/spice 树苗；
- 300t 后检查树干/树冠。

## 2. 结果

```text
NEARCLEAR_NUT_PLACED
NEARCLEAR_SPICE_PLACED
RUNTIME_NEARCLEAR_CHECK
```

但没有：

```text
grew ... at ...
NEARCLEAR_*_TRUNK
```

树苗放置成功，但本轮连 scheduled tick 树干都没有出现。

## 3. 判断

- 不能据此判树冠失败；
- 清空/玩家位置/区块 tick 可能让 scheduled tick 再次不可靠；
- 需要更简单的开阔地测试；
- 之前 P0-BU 已在玩家旁确认过树干生成。

## 4. 结论

- 本轮没有树冠证据；
- 测试环境仍影响 scheduled tick；
- 不修改代码。
