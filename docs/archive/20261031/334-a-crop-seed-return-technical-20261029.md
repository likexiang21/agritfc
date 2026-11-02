# 334 A 作物种子返还 P0-W 技术分析

> 日期：2026-10-29
> 目标：为 A 的 87 作物补齐“成熟收获至少返还 1 个种子”的兜底。
> 约束：不推送；不伪造；additive。

## 1. 设计

`ACropSeedReturnHandler`：

- 只处理 `tfcfarmingplus:crop/<crop>`；
- 复用 `CropWasteCrops.cropFromBlockId` 的精确反向查找；
- 跳过 `GrainCrop` 中已由 bundle 处理的 A 谷物；
- 达到方块真实最大 age 才返还 `tfcfarmingplus:seeds/<crop>` 1 个；
- 不取消原破坏；
- 原 A loot 保留。

## 2. 与 TFC 版本的区别

- 方块 ID 前缀不同：`tfcfarmingplus:crop/`；
- 种子 ID：`tfcfarmingplus:seeds/<crop>`；
- 同样跳过谷物；
- 不处理 B 香料（B 香料有独立 `spice_seed/`）。

## 3. 测试

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

已有：

```text
PASS: 283 crop P0 checks
```

## 4. 风险

- 未实机；
- 可能与 A 原种子掉落重复；
- A 作物 max age 必须来自真实 blockstate；
- 双格/特殊作物未单独处理；
- 不是完整收获替换。
