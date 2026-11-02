# 405 树形香料形态拆分 P0-BG 技术分析

> 日期：2026-10-29
> 目标：把 5 个 tree form 香料从普通 CropBlock 形态拆出，只保留树形态，消除双形态并存。
> 约束：不推送；不伪造；未实机。

## 1. 拆分

tree form：

```text
pimento · cinnamon · clove · nutmeg · star_anise
```

`AgricultureSpices` 不再注册：

- `spice_crop/<tree>`；
- `spice_seed/<tree>`。

仍注册：

- `spice/<tree>` 产物；
- `spice_waste/<tree>` 废枝叶；
- `ground_spice/<tree>`；
- 树 sapling/leaves（P0-AS）。

## 2. 结果

B 20 香料：

```text
15 作物形态（herb/shrub/root/vine/corm）
5 树形态
```

树叶 loot 新增：

- 5% 香料产物；
- 5% 树苗；
- 5% spice_waste。

## 3. 验证

```text
PASS: 15 spice crops, 5 spice trees, 20 ground spices
PASS: 393 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
processResources BUILD SUCCESSFUL
```

## 4. 风险

- 未实机；
- 旧 `spice_crop/<tree>`/seed 资源仍留在 resources，成为未使用文件；
- 树只在树叶 loot/配方/世界生成中出现；
- 树产物只从树叶/树苗链获得；
- 没有删除旧资源（避免误删）。
