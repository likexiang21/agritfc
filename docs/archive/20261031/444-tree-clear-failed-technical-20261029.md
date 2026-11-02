# 444 显式清空树冠测试未完成 P0-BZ 技术分析

> 日期：2026-10-29
> 目标：不用 tp/fill，用逐格 setblock 清空树冠空间，验证树叶。
> 约束：不推送；不伪造；测试后恢复环境。

## 1. 测试

临时数据包 `runtime-tree-clear`：

- 玩家旁放树苗；
- 20t 后执行 504 个 `setblock air`（y+1..+8，x-1..7，z-3..3）；
- 300t 检查。

## 2. 结果

```text
CLEAR_NUT_PLACED
CLEAR_SPICE_PLACED
RUNTIME_CLEAR_CLEAR
RUNTIME_CLEAR_CHECK
```

没有：

```text
grew ... at ...
CLEAR_*_TRUNK / LEAF
```

## 3. 判断

- 树苗放置成功；
- 清空函数执行；
- 但本轮 scheduled tick 仍没有生长日志；
- 测试环境/调度与清空操作关系仍未定位；
- 不能判树冠/树代码失败。

## 4. 结论

- 树冠仍未验证；
- 不再重复同类清空测试；
- 改用真实玩家正常种植。
