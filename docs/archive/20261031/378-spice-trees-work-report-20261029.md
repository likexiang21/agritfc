# 378 香料树 P0-AS 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：5 个 tree form 香料的树方块；世界生成/实机未完成。

## 1. 完成内容

- `SpiceTreeSpecies` 5 条；
- `SpiceTreeLeavesBlock`；
- `SpiceTreeSaplingBlock`；
- 5 种树叶 blockstate（8 variants/种）；
- 5 种树苗 blockstate（3 stage）；
- 树叶 loot：产物/树苗各 5%；
- 树苗 loot；
- 树苗配方；
- 语言/模型/创造页。

## 2. 验证

```text
PASS: 381 crop P0 checks
PASS: spice tree resources
gradle compileJava
BUILD SUCCESSFUL
processResources BUILD SUCCESSFUL
```

## 3. 边界

- **未实机**；
- 树干是 TFC oak log；
- 没有世界生成；
- 树与 crop 双形态并存；
- 产物掉落未平衡；
- 不能宣称香料树最终验收。

## 4. 下一批

1. 实机香料树；
2. worldgen；
3. 树/作物形态统一；
4. 全量实机测试。
