# 454 绝对坐标树叶衰减测试 P0-CE 技术分析

> 日期：2026-10-29
> 目标：用绝对坐标避免相对坐标漂移，验证 B 树叶衰减/掉落。
> 约束：不推送；不伪造；测试后恢复环境。

## 1. 测试

干净存档出生点区块，绝对坐标放：

- `-766 66 528`：nut 普通叶；
- `-764 66 528`：nut persistent 叶；
- `-762 66 528`：spice 普通叶；
- `-760 66 528`：spice persistent 叶；
- randomTickSpeed=1000；
- 300t 后绝对坐标检查 + item 实体检查。

## 2. 结果

```text
ABSLEAF_NUT_PERSISTENT_STILL
ABSLEAF_SPICE_PERSISTENT_STILL
ABSLEAF_NUT_DROP
```

- persistent 叶保留；
- nut 叶附近发现 item 实体；
- 普通叶的 `air`/`still` 方块检查仍未命中；
- spice 普通叶无 drop。

## 3. 判断

- nut 叶有掉落物证据，疑似衰减产出；
- 掉落物 ID 未读取；
- spice 普通叶未观察到衰减；
- 方块检查方式仍需用 `data get block` 复核。

## 4. 结论

- 不能宣称树叶衰减全部完成；
- persistent 行为正常；
- nut 有掉落线索。

## 5. 证据

```text
mod_rebuild/docs/audit/runtime-leaf-abs-20261029.log
```
