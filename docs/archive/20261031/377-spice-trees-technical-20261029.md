# 377 香料树 P0-AS 技术分析

> 日期：2026-10-29
> 目标：为 5 个 tree form 香料增加真实树方块（B leaves + sapling + tree growth），不再只是 CropBlock 形状差。
> 约束：不推送；不伪造；未实机。

## 1. 范围

5 个 tree form：

```text
pimento · cinnamon · clove · nutmeg · star_anise
```

每种新增：

- `spice_leaves/<spice>`；
- `spice_sapling/<spice>`；
- 树苗 BlockItem；
- 树叶 loot：香料产物/树苗各 5%；
- 树苗 loot；
- 树苗配方：香料产物 + dirt。

## 2. 树叶

`SpiceTreeLeavesBlock extends LeavesBlock`：

- 只保留 vanilla `persistent/distance`；
- 秋季 3% 掉对应香料产物；
- 每种 8 个 blockstate variants（persistent + distance）。

## 3. 树苗

`SpiceTreeSaplingBlock extends BushBlock`：

- stage 0..2；
- 成熟后构建：
  - TFC oak log 树干 4–5；
  - B spice leaves 冠层；
- 移除树苗。

## 4. 与 CropBlock 的关系

原有 `spice_crop/<spice>` 仍保留；tree form 现在同时有：

- 作物形态（8 龄 CropBlock）；
- 树形态（B leaves/sapling）。

两者暂未合并为唯一形态。

## 5. 测试

```text
PASS: 381 crop P0 checks
PASS: spice tree resources
gradle compileJava
BUILD SUCCESSFUL
processResources BUILD SUCCESSFUL
```

## 6. 风险

- 未实机；
- 树干是 TFC oak log；
- 没有世界生成（树苗靠树叶/配方）；
- 树与作物双形态并存；
- 香料产物叶子掉落未平衡；
- 不能宣称香料树最终完成。
