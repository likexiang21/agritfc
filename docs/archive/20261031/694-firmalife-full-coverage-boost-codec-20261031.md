# 694 严格评估收尾：Firmalife 全覆盖、种子处理 BE 与 codec

> 日期：2026-10-31
> 状态：**代码/数据已修改；静态构建通过；未实机**
> 来源：严格评估 P1-A、P1-B、P2-2

## 1. P1-A：Firmalife 剩余 14 个植物方块接入 B 废枝叶

严格评估指出：B 之前只覆盖 8 个 Firmalife 香草，剩余 12 个 `firmalife:plant/*`
和 2 个 `firmalife:grape_string_plant_*` 完全没有 B 侧钩子。

本轮新增 14 个 B 废枝叶物品：

```text
crop_waste/cocoa_branch
crop_waste/cocoa_growing_branch
crop_waste/cocoa_leaves
crop_waste/cocoa_sapling
crop_waste/fig_branch
crop_waste/fig_growing_branch
crop_waste/fig_leaves
crop_waste/fig_sapling
crop_waste/nightshade_bush
crop_waste/pineapple_bush
crop_waste/wild_red_grapes
crop_waste/wild_white_grapes
crop_waste/grape_string_red
crop_waste/grape_string_white
```

- `FirmalifePlantWasteHandler` 现在匹配全部 `firmalife:plant/*` 与
  `firmalife:grape_string_plant_*`；
- 8 个香草保持原有 `spice_waste` + 刀具门槛；
- 其余 14 个方块掉对应 `crop_waste`；
- 14 个物品均生成 item model、en_us/zh_cn 语言键，并追加到
  `tfc:compost_greens/medium`。

因此 Firmalife 的 20 个 `plant/*` 非 potted 方块 + 2 个葡萄种植方块全部进入 B 的副产物链，
不再有完全未接入的 Firmalife 植物。

## 2. P1-B：种子处理 boost 对 A/TFC 作物

严格评估指出：`SeedTreatmentGrowthHandler` 与 `SeedlingItem.applyBoost` 调用
vanilla `BonemealableBlock`，而 A/TFC 作物由 `CropBlockEntity` 的 growth 驱动。

修复：

```java
if (level.getBlockEntity(pos) instanceof CropBlockEntity crop) {
    final long now = Calendars.SERVER.getTicks();
    CropHelpers.growthTickStep(level, pos, state, level.random,
        now - CropHelpers.UPDATE_INTERVAL * boost, now, crop);
    return;
}
```

- 两处（播种后 boost、育苗移栽后 boost）都改为真实 TFC growth step；
- 该路径同时处理 growth、yield、expiry、养分与气候上限，避免 setGrowth 的产量下降/越限/age 不同步；
- B 香料/草莓仍是 vanilla CropBlock，继续走 bonemeal 路径。

## 3. P2-2：TfcFarmlandCropBlock codec

新增：

```java
@Override
public MapCodec<? extends CropBlock> codec() {
    return simpleCodec(TfcFarmlandCropBlock::new);
}
```

避免 codec 重建 vanilla CropBlock 而丢失 TFC 耕地兼容。

## 4. 校验

```text
gradle build BUILD SUCCESSFUL
json 6530 / models 3704 / blockstates 539 / item_models 957
lang en_us 1107 / zh_cn 1107 / missing 0 / extra 0
final_static_audit problems 0
```

当前 jar：

```text
2,954,689 bytes
SHA-256 9CAA9D331665B567C14FF283C7C45022FCF0F9F9A22CB81671B246B2629A106A
```

## 5. 仍需确认

- 未实机；
- 播种门现在在 TFC 耕地真实生效，A 38 个物种 + TFC 10 个物种 + B 草莓不能直播；这是“不豁免”的直接后果，需要用户确认是否接受；
- 香料/草莓仍是单一临时模型，8 个 age 无视觉生长差异；
- AFC 树叶 `nut_state` 资产缺口未处理。
