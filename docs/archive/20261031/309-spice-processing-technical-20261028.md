# 309 香料初加工 P0-K 技术分析

> 日期：2026-10-28
> 目标：为 20 种 B 香料建立“作物产物 → 香料粉”的初加工链。
> 约束：不推送；不伪造；贴图暂时指向 TFC。

## 1. 范围

本轮实现：

- 20 个 `ground_spice/<spice>` 物品；
- 20 条 `tfcagricultureplus:mortar` 研磨配方：
  - `spice/<spice>` → `ground_spice/<spice>`；
  - `grind_time: 4`；
- 20 个 item model；
- 40 个语言 key（20 ground + 已有 spice 产物）。

不包含：

- 树/藤/球茎香料形态；
- 干燥/发酵/烘焙等加工；
- 香料粉的食物属性/烹饪效果；
- 实机验证。

## 2. 配方格式

沿用现有 B 石臼配方：

```json
{
  "type": "tfcagricultureplus:mortar",
  "ingredient": {"item": "tfcagricultureplus:spice/<spice>"},
  "result": {"id": "tfcagricultureplus:ground_spice/<spice>", "count": 1},
  "grind_time": 4
}
```

## 3. 校验

纯 Java：

```text
PASS: 265 crop P0 checks
```

新增 `groundPath` 对 20 个 SpiceSpecies 的验证。

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

资源：

```text
PASS: 99 item models, 2 lang files, 17 recipes, 102 crop_waste,
      10 bush_waste, 15 wild mushrooms, 4-stage bag, 79 nut leaf states,
      20 spice crops, 20 ground spices, tags valid
```

## 4. 风险/未验证

- 未实机验证石臼配方加载/研磨；
- 香料粉还没有食物/烹饪用途；
- 树/藤/球茎形态未实现；
- 贴图仍为 TFC 临时资源；
- 没有采种/育苗/移栽等完整香料培育链。

## 5. 下一步

1. 香料形态；
2. 香料粉烹饪用途；
3. TFC 29 剩余覆盖；
4. 全量实机测试。
