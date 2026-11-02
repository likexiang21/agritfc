# 696 严格评估 P1 收尾：放置覆盖、boost 目标校验与 growth 语义

> 日期：2026-10-31
> 状态：**代码已修复；静态构建通过；未实机**
> 来源：严格评估 P1-1/P1-2/P1-3

## 1. P1-1：SeedlingItem / CormItem / SpiceRootItem 覆盖已有方块

三个物品只检查 `canSurvive`（只验证下方耕地/光照），然后直接
`level.setBlockAndUpdate(pos, cropState)`；目标位置已有作物、树苗、火把等非满方块时会被覆盖且无掉落。

修复：

```java
if (!level.getBlockState(pos).canBeReplaced()) {
    return InteractionResult.PASS;
}
```

- `SeedlingItem`：返回 PASS；
- `CormItem` / `SpiceRootItem`：返回 PASS；
- 与 `PropagationStockItem` 已有的 `isEmptyBlock` 检查保持一致。

## 2. P1-2：SeedTreatmentGrowthHandler 目标校验与双重 boost

修复：

- 只对 `SeedTreatments.isSeedItemId(itemId)` 的**种子**生效；`seedling` 不再进入该 handler，
  消除“育苗盘复制 treatment + SeedlingItem 自带 boost”的双重提升；
- 若物种不是 `SEED_DIRECT`（会被播种门取消，走育苗），不调度 boost；
- 目标位置在点击时必须 `canBeReplaced()`，不会对已有作物重复叠加；
- `applyBoost` 仍保留 BE 分支，但改为真实 growth step（见 P1-3）。

## 3. P1-3：growth 语义

此前直接 `crop.setGrowth(growth + 0.12F*boost)`：

- 不补 `yield`，最终产量反而少；
- 可越过 `growthLimit`；
- 不同步 blockstate age。

修复为调用 TFC 的真实增长步：

```java
long now = Calendars.SERVER.getTicks();
CropHelpers.growthTickStep(level, pos, state, level.random,
    now - CropHelpers.UPDATE_INTERVAL * boost, now, crop);
```

`growthTickStep` 会同时处理 growth、yield、expiry、养分、气候上限，并在正常路径刷新 blockstate；
`SeedTreatmentGrowthHandler` 与 `SeedlingItem.applyBoost` 都改为该路径。

## 4. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,954,689 bytes
SHA-256 9CAA9D331665B567C14FF283C7C45022FCF0F9F9A22CB81671B246B2629A106A
```

## 5. 仍未完成

- 未实机；`growthTickStep` 的实际产量/气候行为未验证；
- 14 个新 Firmalife 废枝叶图标仍是 `tfc:item/straw` 占位，zh_cn 名称未完全本地化；
- Firmalife `potted/*`、`grape_string_red/white`（非 `grape_string_plant_*`）未接入；
- `FirmalifePlantWasteHandler` 缺 `CreativeGuards`；
- 香料/草莓 8 age 仍单一模型。
