# 494 蘑菇自然专用/灌木覆盖静态审计 P0-CY 技术分析

> 日期：2026-10-29
> 目标：核对 292-#9（自然专用 4 种禁止菌包）与 292-#13（TFC 10 灌木覆盖采收）。
> 约束：不推送；不伪造。

## 1. 蘑菇自然专用

`MushroomSpecies`：

```text
PORCINI / MOREL / CHANTERELLE / BLACK_TRUFFLE -> naturalOnly=true
```

`MushroomBagBlock`：

```java
if (species == null || species.naturalOnly()) {
    if (species != null && species.naturalOnly()) {
        message ...mushroom_bag.natural_only
    }
    return ItemInteractionResult.FAIL;
}
```

- 4 种自然专用无法装入菌包；
- 菌包配方只有一个通用 `mushroom_bag.json`，没有按物种配方；
- 11 种可栽培 species 有 cultivationTicks。

## 2. TFC 10 灌木

`BushHarvestHandler` 注释/实现：

- 只处理 `BushSpecies.fromTfcBushBlockId` 命中的 TFC 灌木；
- 用 `SeasonalPlantBlock` 的 product/stateAfterPicking；
- 取消破坏、保留灌木并进入采收后状态；
- 非结果/非 10 种灌木保持 TFC 原行为；
- 不触碰 A 灌木或 strawberry。

## 3. 结论

两项计划要求在代码层满足；仍需实机逐物种验证。

## 4. 未验证

- 4 种自然专用用菌包右键的实机 FAIL/消息；
- 10 种 TFC 灌木逐一采收；
- 自然世界生成。
