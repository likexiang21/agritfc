# 381 豆蔻根茎 P0-AU 技术分析

> 日期：2026-10-29
> 目标：给 root form 香料（cardamom）增加可种植根茎，形成“收获 → 根茎 → 再种”的闭环。
> 约束：不推送；不伪造；未实机。

## 1. 新增

- 物品 `tfcagricultureplus:spice_root/cardamom`；
- `SpiceRootItem`：
  - 右键目标位置；
  - 通过 `AgricultureSpices.CROPS` 找 cardamom 作物；
  - 检查 `canSurvive`；
  - 放置 age=0 作物；
  - 消耗 1。
- 收获：
  - `UnifiedCropHarvestHandler` 对 root form 额外掉 1 个根茎；
  - `productYield` 仍为 2。

## 2. 资源

- item model；
- en/zh；
- 创造页。

## 3. 测试

```text
PASS: 382 crop P0 checks
PASS: spice root resources
gradle compileJava
BUILD SUCCESSFUL
processResources BUILD SUCCESSFUL
```

## 4. 风险

- 未实机；
- 只有 cardamom 一个 root；
- 根茎无分级；
- 放置不额外检查 farmland；
- 未平衡根茎/种子/产物数量。
