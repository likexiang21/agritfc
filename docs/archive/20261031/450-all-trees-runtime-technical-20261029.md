# 450 全树种实机确认 P0-CC 技术分析

> 日期：2026-10-29
> 目标：在干净存档中逐一确认 B 的 3 种坚果 + 5 种香料树。
> 约束：不推送；不伪造；测试后删除副本并恢复环境。

## 1. 测试方式

- 复制 tfctest → tfctest2；
- 重置玩家到出生点；
- 临时数据包放树苗；
- 分三批：
  1. 8 树种间距 2（只验证同区块能生长的种类）；
  2. pimento/clove 同区块；
  3. nutmeg/star_anise 同区块；
- 300t 后检查树干/树叶。

## 2. 实机结果

已确认生长日志：

```text
pistachio leaves=81
cashew leaves=46
macadamia leaves=81
cinnamon leaves=81
pimento leaves=81
clove leaves=66
nutmeg leaves=71
star_anise leaves=81
```

通过标记：

```text
TRUNK_PISTACHIO
TRUNK_CASHEW
TRUNK_CINNAMON
TRUNK_MACADAMIA
TWO_PIMENTO_TRUNK
TWO_CLOVE_TRUNK
TWO2_NUTMEG_TRUNK
TWO2_STAR_ANISE_TRUNK
```

## 3. 结论

**3 坚果 + 5 香料树全部在实机中生成树干和树叶。**

## 4. 未确认

- 部分 LEAF1-3/侧叶检查因树高/位置未命中，但 leaves 计数已经证明有叶；
- 树叶衰减；
- 树苗掉落；
- 旧存档。

## 5. 证据

```text
mod_rebuild/docs/audit/runtime-all-trees-final-20261029.log
```

以及本轮实机日志（pimento/clove、nutmeg/star_anise）。
