# 356 藏红花球茎 P0-AH 技术分析

> 日期：2026-10-29
> 目标：为 corm 形态的藏红花增加一个可种植的球茎物品，而不是只用种子/形状模拟。
> 约束：不推送；不伪造；未实机。

## 1. 新增

- 物品 `tfcagricultureplus:spice_corm/saffron`；
- `CormItem`：
  - 右键目标位置；
  - 通过 `AgricultureSpices.CROPS` 找到 saffron 作物；
  - 检查 `canSurvive`；
  - 放置 age=0 作物；
  - 消耗 1。
- 收获：
  - `UnifiedCropHarvestHandler` 对 corm 形态额外掉 1 个球茎；
  - 种子返还仍为 2。

## 2. 资源

- `models/item/spice_corm/saffron.json`；
- en/zh 语言；
- 创造页。

## 3. 测试

```text
PASS: 343 crop P0 checks
PASS: spice corm resources
gradle compileJava
BUILD SUCCESSFUL
```

## 4. 风险

- 未实机；
- 只有藏红花一个 corm；
- 球茎没有分级/大小；
- 右键放置不检查 farmland 类型，只依赖作物 canSurvive；
- 球茎与种子同时掉落的数值未平衡。
