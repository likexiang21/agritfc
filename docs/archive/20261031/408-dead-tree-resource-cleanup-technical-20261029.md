# 408 失效树形作物资源清理 P0-BH 技术分析

> 日期：2026-10-29
> 目标：清理 P0-BG 拆分后不再注册的 5 个 tree form 旧 crop/seed 资源。
> 约束：不删除仍注册/使用的代码；删除后执行 `clean build`。

## 1. 删除范围

5 个 tree form：

```text
pimento · cinnamon · clove · nutmeg · star_anise
```

每项删除：

- `blockstates/spice_crop/<tree>.json`；
- `models/block/spice_crop/<tree>.json`；
- `models/item/spice_seed/<tree>.json`；
- `loot_table/blocks/spice_crop/<tree>.json`。

共 20 个文件。

语言键同步移除：

- `block.tfcagricultureplus.spice_crop.<tree>`；
- `item.tfcagricultureplus.spice_seed.<tree>`。

## 2. 为什么安全

- `AgricultureSpices` 已对 tree form 跳过 crop/seed 注册；
- 没有代码再引用这些 block/item/loot；
- 树形态走 `spice_leaves` / `spice_sapling`。

## 3. 验证

```text
gradle clean build
BUILD SUCCESSFUL

PASS: 99 item models ... 15 spice crops, 5 spice trees ...
BAD_REFS 0
```

## 4. 风险

- 删除后无法恢复，已确认无注册引用；
- 旧存档中若存在这些方块 ID，会变成缺失方块；
- 没有实机验证旧存档兼容。
