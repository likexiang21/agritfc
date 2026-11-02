# 346 球茎香料繁殖 P0-AC 技术分析

> 日期：2026-10-29
> 目标：让 `form=corm` 的香料（saffron）在收获时稳定多返还 1 个种子，体现球茎无性繁殖。
> 约束：不推送；不伪造；未实机。

## 1. 实现

`SpiceSpecies.seedYield()`：

- `corm` → 2；
- 其他 → 1。

`CropBItemResolver.seedCountForCropBlock`：

- 对 `tfcagricultureplus:spice_crop/<spice>` 返回对应 `seedYield`；
- 非香料返回 1。

`UnifiedCropHarvestHandler`：

- 计算原 loot 中已有种子数量；
- 补足到请求数量；
- 不再固定只补 1 个。

## 2. 结果

- saffron（corm）收获至少 2 个种子；
- 其他香料仍为 1；
- 原 loot 中的种子计入，不重复超发。

## 3. 测试

```text
PASS: 320 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
```

新增 20 条 seedYield 校验。

## 4. 风险

- 未实机；
- saffron 的 form 字符串必须确为 `corm`；
- 球茎繁殖没有独立物品/模型；
- 原 loot 可能已含 2 个种子，补足后仍按请求数控制；
- 不是完整球茎机制。
