# 321 TFC 种子返还 P0-Q 技术分析

> 日期：2026-10-29
> 目标：为 29 种 TFC 作物建立“成熟收获至少返还 1 个种子”的兜底。
> 约束：不推送；不伪造；不取消原掉落。

## 1. 设计

新增 `TfcCropSpecies`：

- 29 个 TFC 作物 ID；
- `tfc:crop/<id>`；
- `tfc:seeds/<id>`；
- 6 个谷物标记为 `alreadyHandledByGrainBundle`。

新增 `TfcSeedReturnHandler`：

- 监听 `BlockEvent.BreakEvent`；
- 只处理 `tfc:crop/<id>`；
- 跳过 6 个谷物（由 GrainHarvestHandler 负责）；
- 跳过已取消事件；
- 跳过双格 top；
- 只有达到该方块真实最大 age 才追加 1 个种子；
- 不取消原方块破坏，原 TFC 掉落保留。

## 2. 为什么

- TFC 作物收获后必须能回到种子循环；
- 部分作物原掉落不稳定/不保证种子；
- 与 GrainHarvestHandler 分工，避免谷物重复；
- 不替换 TFC loot，降低风险。

## 3. 测试

纯 Java：

```text
PASS: 282 crop P0 checks
```

新增：

- 29 个 TFC 作物；
- tomato 映射；
- wheat 标记为 grain；
- tomato 不标记 grain。

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

## 4. 风险

- 未实机；
- 可能和 TFC 原有种子掉落重复；
- 只追加种子，不是完整替换 TFC 收获；
- 某些 TFC 种子 ID 需实机核对；
- 双格 top/bottom 处理需实机确认。
