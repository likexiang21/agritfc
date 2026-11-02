# 688 取消 TFC/Firmalife 作物与植物豁免

> 日期：2026-10-31
> 状态：**代码/数据已修复；静态构建通过；未实机**

## 1. 发现

旧代码把 TFC 当成例外：

```java
if (itemId.startsWith("tfc:")) {
    return; // TFC seeds keep their original direct sowing
}
```

`NurseryTrayBlockEntity.canAccept` 也直接拒绝 `tfc:` 种子。Firmalife 的植物更没有进入 B 的作物链：

- `firmalife:plant/{basil,bay_laurel,cardamom,cilantro,cumin,oregano,pimento,vanilla}` 与 B 的 20 种香料重复；
- B 的 `spice_waste/*` 只由 B 自己的香料作物产生；
- Firmalife 植物被完全排除在副产物链之外。

## 2. 修复

### 2.1 TFC 不再豁免

- `CropPropagation.speciesFromSeedId` 识别 `tfc:seeds/<species>`，返回裸 `<species>`；
- `CropPropagation` 不再对 `tfc:` 前缀短路，TFC 种子真正查表；TFC 谷类/工业作物显式归入 `SEED_DIRECT`；
- `DirectSeedPlantingGate` 不再有 `startsWith("tfc:")` 的提前返回，TFC 种子走同一张传播表；
- `NurseryTrayBlockEntity.canAccept` 不再拒绝 TFC 种子，改为判断 `SeedlingItem.canResolveSeed(id)`；
- `SeedlingItem.cropStateForSeed` 对非 BlockItem 的 TFC 种子解析 `tfc:crop/<species>` 方块，并把 `age` 设为 0；
- 因此 TFC 种子现在既能直种（同一传播表分类为 direct），也能进育苗盘并移栽。

### 2.2 Firmalife 植物不再完全排除

- 新增 `FirmalifePlantWasteHandler`：
  - 监听 `firmalife:plant/<species>` 破坏；
  - 8 个香草只在主手为 `TFCTags.Items.TOOLS_KNIFE` 时追加 `spice_waste/<species>`，与 Firmalife 自己的刀具门槛一致；不额外掉 B `spice/<species>`；
  - 其余 12 个 `firmalife:plant/*` 与 2 个 `firmalife:grape_string_plant_*` 追加 14 个新增 `crop_waste/*`，详见 docs/694；
  - 因此 Firmalife 的 20 个非 potted `plant/*` + 2 个葡萄种植方块全部有 B 副产物出口；
- `DirectSeedPlantingGate` 对无法识别的外部种子不再静默取消，避免 B 误拦 Firmalife 的种植规则；
- 未知外部种子不会被当成 A/B 种子处理，但也不会被 B 的 gate 破坏。

## 3. 校验

```text
gradle compileJava BUILD SUCCESSFUL
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,954,689 bytes
SHA-256 9CAA9D331665B567C14FF283C7C45022FCF0F9F9A22CB81671B246B2629A106A
```

## 4. 未完成

- 未实机；
- Firmalife 的果树（fig/cocoa）、葡萄、菠萝/夜影灌木仍由 Firmalife 自己处理，B 没有对应的 `crop_waste` 物品可追加；
- TFC/Firmalife 的完整逐作物矩阵尚未写成新的 159 行验收表。
