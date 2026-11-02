# 446 干净存档树冠实机确认 P0-CA 技术分析

> 日期：2026-10-29
> 目标：用干净存档副本 + 重置玩家到出生点，避开之前测试环境干扰，验证树冠。
> 约束：不推送；不伪造；测试后删除副本并恢复环境。

## 1. 测试方式

- 复制 `tfctest` 为 `tfctest2`（176MB）；
- 用 nbtlib 把 `Player.Pos` 改到出生点 `(-767.5, 66, 528.5)`；
- 数据包 `runtime-tree-clean`：
  - `randomTickSpeed=1000`；
  - 10s 后玩家旁放 nut/spice 树苗；
  - 300t 检查。

## 2. 实机结果

```text
CLEAN_NUT_PLACED
CLEAN_SPICE_PLACED

[TFC Agriculture Plus] grew pistachio at BlockPos{x=-765, y=65, z=528}, leaves=81

CLEAN_NUT_TRUNK
CLEAN_NUT_SIDE
```

- nut 树生成树干；
- **树叶 81 片**；
- 树干/侧面树叶检查通过。

## 3. 结论

- scheduled tick 树生长在干净存档中生效；
- 树叶生成代码正常；
- 之前 leaves=0 是测试地点固体/玩家位置问题；
- 树代码不再只是“未验证”。

## 4. 未确认

- spice tree 本轮无 `grew` 日志；
- 未检查完整树冠所有位置；
- 树叶衰减/树苗掉落未验证；
- 旧存档未验证。

## 5. 证据

```text
mod_rebuild/docs/audit/runtime-tree-clean-20261029.log
```
