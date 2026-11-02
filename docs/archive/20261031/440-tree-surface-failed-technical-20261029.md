# 440 地表树冠测试未完成 P0-BX 技术分析

> 日期：2026-10-29
> 目标：玩家传送到地表并清空上方空间，验证树干+树冠。
> 约束：不推送；不伪造；测试后恢复环境。

## 1. 测试

临时数据包 `runtime-tree-surface`：

- 20s 后 `tp` 玩家到 `0 151 0`；
- 放 stone 平台；
- `fill` 清空玩家上方；
- 放 nut/spice 树苗；
- 300t 后检查。

## 2. 结果

```text
SURFACE_NUT_PLACED
SURFACE_SPICE_PLACED
RUNTIME_SURFACE_CHECK
```

但**没有**：

```text
grew ... at ...
SURFACE_*_TRUNK
```

## 3. 判断

- 树苗放置成功；
- 本轮 scheduled tick 没有产生树干；
- `tp`/`fill` 或玩家位置变化可能让 scheduled tick 不可靠；
- 不能据此判树冠/树代码失败。

## 4. 结论

- 树冠仍未验证；
- 测试环境仍然不可靠；
- 不再重复同类不可靠测试，改用真实玩家放置/正常世界。
