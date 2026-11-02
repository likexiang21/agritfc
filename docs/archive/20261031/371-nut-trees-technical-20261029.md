# 371 开心果/腰果专属树 P0-AP 技术分析

> 日期：2026-10-29
> 目标：给最后两种无树坚果补专属树，而不是停在野草临时来源。
> 约束：不推送；不伪造；未实机。

## 1. 新增

每种树：

- `nut_leaves/<tree>`；
- `nut_sapling/<tree>`；
- 树苗 BlockItem；
- 树叶 4 个 `nut_state`；
- 树叶 loot：坚果/壳/树苗各 5%；
- 树苗 loot；
- 树苗配方：坚果 + dirt → 树苗。

## 2. 树叶

`NutLeavesBlock extends LeavesBlock`：

- 保留 vanilla `persistent/distance`；
- 新增 `nut_state 0..3`；
- 季节：春 1、夏 2、秋 3、冬 0；
- 秋熟且 3% 随机掉坚果 + 壳；
- blockstate 覆盖：
  - `persistent=true` × 4；
  - `persistent=false,distance=1..7` × 4 = 28；
  - 共 32 variants/树。

## 3. 树苗

`NutTreeSaplingBlock extends BushBlock`：

- stage 0..2 随机生长；
- 成熟后生成：
  - TFC oak log 树干 4–5 高；
  - 顶部 B nut leaves 冠层；
- 生成后移除树苗。

## 4. 测试

```text
PASS: 368 crop P0 checks
PASS: pistachio/cashew tree resources
gradle compileJava
BUILD SUCCESSFUL
processResources BUILD SUCCESSFUL
```

## 5. 风险

- 未实机；
- 树干是 TFC oak log，不是专属木材；
- 不是 TFC 果树/嫁接体系；
- 没有世界生成；
- 树苗只能靠树叶或配方获得；
- 冠层/衰减行为未验证。
