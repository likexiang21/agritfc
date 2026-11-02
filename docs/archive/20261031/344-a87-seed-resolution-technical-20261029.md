# 344 A 87 全量种子解析 P0-AB 技术分析

> 日期：2026-10-29
> 目标：不再让 A 作物的种子解析依赖“是否有 crop_waste”名单，覆盖 A 全部 87 个作物方块。
> 约束：不推送；不伪造；未实机。

## 1. 原问题

旧 `CropBItemResolver.seedForCropBlock` 对 A 作物要求：

```text
CropWasteCrops.cropFromBlockId(...) != null
```

而 `CropWasteCrops` 只有 82 条；A 中无废枝叶的 5 类作物不会被统一 handler 处理，也不会进入种子解析。

## 2. 修正

对 `tfcfarmingplus:crop/<crop>`：

- 直接从方块 ID 路径取 `<crop>`；
- 解析 `tfcfarmingplus:seeds/<crop>`；
- 不再依赖 `CropWasteCrops` 名单。

`ACropSeedReturnHandler` 同样改成路径解析，覆盖 A 87。

## 3. 结果

- A 87 个作物都有种子解析入口；
- 无废枝叶的 A 作物仍走统一收获：原 loot + 种子；
- 有废枝叶的 A/TFC 作物继续原 loot + 种子 + waste；
- TFC 29 和 B 香料路径不变。

## 4. 测试

```text
PASS: 300 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
```

## 5. 风险

- 未实机；
- A 作物种子 ID 必须与方块 ID 路径完全一致，需实机核对；
- 有些 A 作物可能是特殊种子 ID；
- 没有逐作物 87 条实际收获回归。
