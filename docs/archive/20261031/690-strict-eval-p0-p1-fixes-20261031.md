# 690 严格全量评估 P0/P1 修复

> 日期：2026-10-31
> 状态：**代码已修复；静态构建通过；未实机**
> 来源：独立评估报告（P0-1、P1-1、P1-3、P1-4、P1-5）

## 1. P0：成熟 A/TFC 非谷类作物主产物 0 掉落

评估证据链：

- `UnifiedCropHarvestHandler` 取消 `BlockEvent.BreakEvent` 后自行补掉落；
- 调用 `Block.getDrops(..., null, ...)` 时第 4 参 BlockEntity 为 `null`；
- TFC `CropYieldProvider` 在 LootContext 没有 `BLOCK_ENTITY` 时直接返回 `min`；
- A 86/86、TFC 25 个作物的 `crop_yield_uniform.min` 为 0；
- NeoForge `ServerPlayerGameMode.destroyBlock` 在事件取消后直接返回，不会再补原版掉落。

修复：

```java
// UnifiedCropHarvestHandler
final List<ItemStack> original = Block.getDrops(state, level, event.getPos(),
    level.getBlockEntity(event.getPos()), event.getPlayer(),
    event.getPlayer() == null ? ItemStack.EMPTY : event.getPlayer().getMainHandItem());
```

该参数使 TFC `CropYieldProvider` 能读到 `CropBlockEntity` 并返回真实 `crop_yield_uniform` 产量。

## 2. P1-1：TFC 不再是前缀豁免

- 删除 `CropPropagation.of()` 对 `tfc:` 的提前返回；
- `speciesFromSeedId("tfc:seeds/<sp>")` 返回裸 `<sp>`，与其他命名空间一致；
- 把 TFC 谷类/工业作物加入 `SEED_DIRECT`：barley、oat、rice、rye、wheat、maize、alfalfa、canola、jute、papyrus、sugarcane；
- 把此前漏掉的 A 纤维/油料作物加入显式分类：agave、cotton、flax、hemp、ramie、safflower、sesame、sisal、sunflower、wild_rice_stem；
- TFC 共享物种（cabbage/tomato/potato/garlic/cassava 等）现在真正使用表中分类，而不是被 `tfc:` 前缀短路。

## 3. P1-3：TFC 植物副产物补漏

- `BushSpecies.fromTfcBushBlockId` 识别 `*_bush_cane`，4 个 cane 形式现在能映射到对应灌木废枝；
- `StrawberryWasteHandler` 移除“仅 FRUITING 给废枝叶”的限制，非结实期破坏也按同一规则给 `crop_waste/strawberry`；
- `CropWasteCrops.cropFromBlockId` 接受 `tfc:wild_crop/` 与 `tfcfarmingplus:wild_crop/`，野外作物不再被排除。

## 4. P1-4：播种门提示

`DirectSeedPlantingGate` 取消种植时显示：

```text
message.tfcagricultureplus.seed_requires_nursery
```

en_us/zh_cn 已同时添加该键。

## 5. P1-5：Firmalife 香草重复产物与刀具门槛

- 不再额外掉落 B 的 `spice/<species>`，避免与 `firmalife:spice/*` 重复；
- `FirmalifePlantWasteHandler` 只在主手为 `TFCTags.Items.TOOLS_KNIFE` 时追加 `spice_waste/<species>`，与 Firmalife 自己的刀具门槛一致；
- Firmalife 自己的香料产物仍由 Firmalife 的 drying/crafting 配方提供，不是由 B 废枝叶补上。

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

- 未实机；P0 修复只证明参数正确，不证明 95 个物种的实际产量数字；
- Firmalife 其余 12+2 个植物方块已由 694/695 接入 B 废枝叶；
- 文档 682 的旧计数已修正为 36/43/3，见 [682](682-compost-tags-full-audit-20261031.md)。
