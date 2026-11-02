# 448 香料树实机确认 P0-CB 技术分析

> 日期：2026-10-29
> 目标：干净存档中验证 spice tree（cinnamon/pimento）树干+树叶。
> 约束：不推送；不伪造；测试后删除副本并恢复环境。

## 1. 测试方式

- 复制 tfctest → tfctest2；
- 重置玩家到出生点；
- 数据包 runtime-spice-clean：
  - randomTickSpeed=1000；
  - 玩家旁放 cinnamon/pimento 树苗；
  - 300t 检查。

## 2. 结果

```text
SPICE_CINNAMON_PLACED
SPICE_PIMENTO_PLACED

grew cinnamon ... leaves=81
grew pimento ... leaves=47

SPICE_CINNAMON_TRUNK
SPICE_CINNAMON_LEAF4
SPICE_CINNAMON_SIDE
SPICE_PIMENTO_TRUNK
SPICE_PIMENTO_SIDE
```

- 两棵 spice tree 都生成树干；
- 树叶分别 81/47 片；
- 树干与侧面树叶通过。

## 3. 结论

B 的 spice tree 生成与树叶代码在干净存档中实机生效。

## 4. 未确认

- LEAF1-3 检查未通过（树高/位置差异，不是必然缺叶）；
- 完整树冠遍历未做；
- 树叶衰减/树苗掉落未验证；
- 旧存档未验证。

## 5. 证据

```text
mod_rebuild/docs/audit/runtime-spice-clean-20261029.log
```
