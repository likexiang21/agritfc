# 375 澳洲坚果专属树 P0-AR 技术分析

> 日期：2026-10-29
> 目标：把 macadamia 也纳入 B 专属坚果树叶状态/树苗/世界生成，使 8 种坚果都有 B 树或既有树叶映射。
> 约束：不推送；不伪造；未实机。

## 1. 新增

`NutTreeSpecies` 增加：

```text
MACADAMIA
```

自动获得：

- `nut_leaves/macadamia`；
- `nut_sapling/macadamia`；
- 32 variants 树叶；
- 3 stage 树苗；
- 树叶 loot（nut/shell/sapling 各 5%）；
- 树苗 loot；
- 树苗配方（macadamia + dirt）；
- worldgen configured/placed；
- biome modifier 第 3 个 feature。

## 2. 现在 8 种坚果

| 坚果 | 来源 |
|---|---|
| acorn | TFC/AFC oak 类树叶 |
| chestnut | TFC/AFC chestnut 类 |
| pine_nut | TFC/AFC pine 类 |
| hickory_nut | TFC/AFC hickory 类 |
| beechnut | AFC beech 类 |
| pistachio | B 专属树 |
| cashew | B 专属树 |
| macadamia | B 专属树 + A 树叶临时来源 |

## 3. 测试

```text
PASS: 370 crop P0 checks
PASS: pistachio/cashew/macadamia tree resources
PASS: pistachio/cashew/macadamia tree worldgen resources
gradle compileJava
BUILD SUCCESSFUL
processResources BUILD SUCCESSFUL
```

## 4. 风险

- 未实机；
- 树干仍为 TFC oak log；
- 不是 TFC 果树/嫁接体系；
- A macadamia 树叶来源仍并存；
- worldgen 群系复用蘑菇标签；
- 不能宣称坚果生态最终验收。
