# 452 树叶衰减测试 P0-CD 技术分析

> 日期：2026-10-29
> 目标：验证 B 坚果/香料树叶的 persistent 与衰减行为。
> 约束：不推送；不伪造；测试后恢复环境。

## 1. 测试

干净存档中放：

- `nut_leaves/pistachio`（默认 persistent=false）；
- `nut_leaves/pistachio[persistent=true]`；
- `spice_leaves/cinnamon`；
- `spice_leaves/cinnamon[persistent=true]`；
- randomTickSpeed=1000；
- 300t 后检查。

## 2. 结果

```text
LEAF_NUT_PERSISTENT_PLACED
LEAF_SPICE_PERSISTENT_PLACED
...
LEAF_NUT_PERSISTENT_STILL
LEAF_SPICE_PERSISTENT_STILL
```

- persistent=true 树叶保留；
- 非 persistent 树叶既没有 `DECAYED` 也没有 `STILL` 标记。

## 3. 判断

- persistent 行为正常；
- 非 persistent 行为未能通过 `if block air` 确认；
- 可能是测试相对坐标/方块状态/检查方式问题；
- 不能据此判衰减失败。

## 4. 结论

- 没有完整衰减证据；
- 没有树苗掉落证据；
- 需要更可靠的检查方式。
