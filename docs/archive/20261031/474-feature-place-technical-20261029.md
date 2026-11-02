# 474 蘑菇 worldgen feature 执行验证 P0-CO 技术分析

> 日期：2026-10-29
> 目标：用 `/place feature` 验证 B 野生蘑菇 placed/configured feature 可执行。
> 约束：不推送；不伪造；测试后恢复环境。

## 1. 测试

干净存档，玩家旁放 grass block，执行：

```text
place feature tfcagricultureplus:wild_mushroom_oyster ~2 ~ ~
place feature tfcagricultureplus:wild_mushroom_button ~4 ~ ~
place feature tfcagricultureplus:wild_mushroom_chanterelle ~6 ~ ~
```

20t 后检查方块。

## 2. 结果

```text
FEATURE_OYSTER_OK
FEATURE_BUTTON_OK
FEATURE_CHANTERELLE_OK

FEATURE_OYSTER_STILL
FEATURE_BUTTON_STILL
FEATURE_CHANTERELLE_STILL
```

## 3. 结论

三个野生蘑菇 feature 能在实机执行并放置对应 B 方块，方块保持存在。

## 4. 未确认

- 自然世界生成/群系分布；
- 全部 15 个蘑菇 feature；
- 生成数量/概率；
- 自然生成后的采集。

## 5. 证据

```text
mod_rebuild/docs/audit/runtime-feature-place-20261029.log
```
