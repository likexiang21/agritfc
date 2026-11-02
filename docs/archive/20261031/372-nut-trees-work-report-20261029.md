# 372 开心果/腰果专属树 P0-AP 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：pistachio/cashew 树苗 + 树叶 + 树生成；世界生成/实机未完成。

## 1. 完成内容

- `NutTreeSpecies` 2 条；
- `NutLeavesBlock`；
- `NutTreeSaplingBlock`；
- 2 种树叶 blockstate（32 variants/种）；
- 2 种树苗 blockstate（stage 0..2）；
- 树叶 loot：nut/shell/sapling 各 5%；
- 树苗 loot；
- 树苗配方：nut + dirt；
- 语言、模型、创造页。

## 2. 验证

```text
PASS: 368 crop P0 checks
PASS: pistachio/cashew tree resources
gradle compileJava
BUILD SUCCESSFUL
processResources BUILD SUCCESSFUL
```

## 3. 边界

- **未实机**；
- 树干是 TFC oak log，不是专属木材；
- 不是 TFC 果树/嫁接机制；
- 没有世界生成；
- 树苗靠树叶/配方；
- 冠层/衰减行为未验证；
- 不能宣称坚果专属树最终验收。
