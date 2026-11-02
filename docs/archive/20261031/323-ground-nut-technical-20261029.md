# 323 坚果初加工 P0-R 技术分析

> 日期：2026-10-29
> 目标：为 8 种 B 坚果建立“坚果 → 坚果粉”的初加工链。
> 约束：不推送；不伪造；贴图暂时指向 TFC。

## 1. 范围

- 8 个 `ground_nut/<nut>` 物品：
  acorn · chestnut · pine_nut · hickory_nut · pistachio · cashew · macadamia · beechnut
- 8 条石臼配方：
  `tfcagricultureplus:<nut>` → `tfcagricultureplus:ground_nut/<nut>`；
  `grind_time: 4`
- 8 个 item model；
- en/zh 各 8 个 key；
- 创造页加入。

尚未实现：

- 坚果壳/油/烤制；
- 新树（pistachio/cashew/macadamia）；
- 食物/营养数据；
- 实机验证。

## 2. 测试

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

资源：

```text
PASS: 99 item models, 2 lang files, 17 recipes, 102 crop_waste,
      10 bush_waste, 15 wild mushrooms, 4-stage bag, 79 nut leaf states,
      20 spice crops, 20 ground spices, 8 ground nuts, tags valid
```

纯 Java：

```text
PASS: 282 crop P0 checks
```

## 3. 风险

- 未实机验证配方加载；
- 坚果粉没有营养/烹饪用途；
- 8 个坚果中只有部分有树/掉落来源；
- 贴图仍为 TFC 临时资源。
