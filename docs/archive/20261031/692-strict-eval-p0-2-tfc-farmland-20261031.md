# 692 严格评估 P0-2：B 香料/草莓作物无法在 TFC 耕地存活

> 日期：2026-10-31
> 状态：**代码已修复；静态构建通过；未实机**
> 来源：第二轮独立严格评估（P0-2、P1-1、P1-2、P1-3）

## 1. P0-2

B 的 20 种香料作物与草莓作物直接继承原版 `CropBlock`：

- `SpiceCropBlocks` 的 6 个形态类；
- `AgricultureBlocks.STRAWBERRY_CROP`。

原版 `CropBlock.mayPlaceOn` 只接受 `minecraft:farmland`（vanilla `FarmBlock`）。
TFC 的耕地是 `tfc:farmland/{alfisol,andisol,aridisol,entisol,fluvisol,mollisol,oxisol,podzol}`，
是 TFC 的 `FarmlandBlock`，不是 vanilla `FarmBlock`，因此：

- 直种：`BlockItem.mustSurvive -> canSurvive` 失败；
- 育苗移栽：`SeedlingItem` 显式 `canSurvive` 失败；
- 结果：15 个非树香料、B 草莓的完整种植链在 TFC 生存中不可达。

## 2. 修复

新增 `common/block/TfcFarmlandCropBlock extends CropBlock`：

```java
@Override
protected boolean mayPlaceOn(BlockState state, BlockGetter level, BlockPos pos) {
    return state.getBlock() instanceof FarmBlock
        || state.is(TFCTags.Blocks.FARMLANDS);
}
```

- `SpiceCropBlocks` 的 6 个形态类全部改为继承该基类；
- `AgricultureBlocks.STRAWBERRY_CROP` 改为 `new TfcFarmlandCropBlock(...)`；
- 原版 `minecraft:farmland` 兼容保留；
- TFC 8 种耕地通过 `TFCTags.Blocks.FARMLANDS` 接受。

## 3. P1-1：耕地判定统一

- `DirectSeedPlantingGate` 与 `SeedTreatmentGrowthHandler` 不再使用
  `blockId.endsWith("farmland")`；
- 改为 `instanceof FarmBlock || state.is(TFCTags.Blocks.FARMLANDS)`；
- 因此 TFC 耕地上的播种门、育苗提示、种子处理成长 boost 才会真正生效。

## 4. P1-2：wild_crop 废枝叶

`CropWasteHandler` 原逻辑只读取整数 `age`；TFC/A 的 `wild_crop` 使用布尔 `mature`。

已增加分支：

```java
if (blockId.contains(":wild_crop/")) {
    if (readBoolean(state, "mature") != Boolean.TRUE) return;
    // drop crop_waste/<crop>
    return;
}
```

## 5. P1-3：wintergreen 方块 ID

TFC 实际方块是 `tfc:plant/wintergreen_berry_bush`，不是 `wintergreen_bush`。

`BushSpecies.tfcBushBlockId()` 对 `wintergreen` 特判为
`tfc:plant/wintergreen_berry_bush`，`bush_waste/wintergreen` 物品路径不变。

## 6. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,954,689 bytes
SHA-256 9CAA9D331665B567C14FF283C7C45022FCF0F9F9A22CB81671B246B2629A106A
```

## 7. 仍未完成

- 未实机；
- Firmalife 剩余 12+2 个植物方块已由 694/695 接入 B 废枝叶；
- 香料/草莓仍用单一临时模型，8 个 age 没有视觉生长差异。
