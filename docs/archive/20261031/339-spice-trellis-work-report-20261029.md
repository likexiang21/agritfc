# 339 香料支架与藤本支撑 P0-Y 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：spice_trellis + vine 香料支撑约束；完整攀爬藤本未完成。

## 1. 完成内容

- `spice_trellis` 方块；
- 物品、blockstate、block/item model、loot；
- 木棍/木板配方；
- 创造页；
- `SpiceCropBlocks.Vine.canSurvive` 要求四水平方向有支架；
- 2 个 vine 香料（vanilla / black_pepper）现在需要支架才能存活/移栽。

## 2. 验证

```text
gradle compileJava
BUILD SUCCESSFUL
PASS: spice trellis resources
```

## 3. 边界

- **未实机验证**；
- 不是完整多格攀爬藤本；
- 支架只是临时木板模型；
- canSurvive 在放置/更新/拆除时的行为未验证；
- 可能影响现有藤本香料种子直接移栽。

## 4. 下一批

1. 实机验证支架/藤本；
2. 多格攀爬藤本；
3. 香料树/球茎；
4. 全量实机测试。
