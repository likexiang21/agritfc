# 338 香料支架与藤本支撑 P0-Y 技术分析

> 日期：2026-10-29
> 目标：给 form=vine 的香料一个真实支撑方块，而不是只有形状差。
> 约束：不推送；不伪造；未实机。

## 1. 新增

- 方块 `tfcagricultureplus:spice_trellis`
- 物品/blockstate/model/loot
- 配方：

```text
S S
PPP
S S
S=stick, P=oak_planks -> 2 spice_trellis
```

- 加入创造页。

## 2. 藤本约束

`SpiceCropBlocks.Vine.canSurvive`：

- 先调用父类 CropBlock.canSurvive；
- 再要求四水平方向至少一个 `spice_trellis`；
- 没有支架的藤本香料不能存活/移栽；
- 支架是独立方块，可拆除，拆除后作物下次 canSurvive 检查失败。

## 3. 为什么

- 之前 2 个 vine 香料只是形状 5..11 的普通 CropBlock；
- 现在至少具备“需要支架”的真实差异；
- 仍然不是攀爬/多格藤本，但不再是纯视觉占位。

## 4. 测试

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

资源：

```text
PASS: spice trellis resources
PASS: 99 item models, 2 lang files, 17 recipes, 102 crop_waste,
      10 bush_waste, 15 wild mushrooms, 4-stage bag, 79 nut leaf states,
      20 spice crops, 20 ground spices, 8 ground nuts, 8 nut shells, tags valid
```

## 5. 风险

- 未实机；
- 支撑要求可能导致玩家无法直接种藤本，需要先放支架；
- 不是完整攀爬/多格藤本；
- 支架模型只是临时木板；
- 未验证 canSurvive 在放置/更新时的行为。
