# 689 取消 TFC/Firmalife 作物与植物豁免工作报告

> 日期：2026-10-31
> 状态：**代码/数据已修改；静态构建通过；未实机**

## 1. 完成内容

- 移除 `DirectSeedPlantingGate` 对 `tfc:` 种子的提前返回；
- `CropPropagation` 现在把 `tfc:seeds/<species>` 解析为裸 `<species>` 并真正查表；TFC 谷类/工业作物显式归入 `SEED_DIRECT`；
- `NurseryTrayBlockEntity.canAccept` 不再拒绝 TFC 种子，改为 `SeedlingItem.canResolveSeed`；
- `SeedlingItem` 对非 BlockItem 的 TFC/A 种子解析作物方块：
  - `tfc:seeds/<sp>` → `tfc:crop/<sp>`；
  - `tfcfarmingplus:seeds/<sp>` → `tfcfarmingplus:crop/<sp>`；
  - `age` 设为 0；
- 新增 `FirmalifePlantWasteHandler`：
  - 8 个香草：刀具门槛 + `spice_waste/<species>`；
  - 其余 12 个 `plant/*` + 2 个 `grape_string_plant_*`：新增 14 个 `crop_waste/*`；
  - 详见 docs/694；
- 对未知外部种子（包括 Firmalife）不再静默取消，避免 B 误拦其它模组的种植规则。

## 2. 验证

```text
gradle compileJava BUILD SUCCESSFUL
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,954,689 bytes
SHA-256 9CAA9D331665B567C14FF283C7C45022FCF0F9F9A22CB81671B246B2629A106A
```

## 3. 边界

- 未实机；
- Firmalife 果树（fig/cocoa）、葡萄、菠萝/夜影灌木仍由 Firmalife 处理，B 没有对应废枝叶物品可追加；
- TFC/Firmalife 的逐项矩阵验收表尚未完成。

## 4. 说明

本报告记录的是代码层“取消豁免”的动作；运行期是否按预期仍无法由静态审查证明。
