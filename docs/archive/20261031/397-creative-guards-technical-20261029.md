# 397 全事件创造模式保护 P0-BC 技术分析

> 日期：2026-10-29
> 目标：让所有作物副产/种子返还事件在创造模式下不再掉落物品，保持与统一收获 handler 一致。
> 约束：不推送；不伪造；未实机。

## 1. 新增

`CreativeGuards`：

```java
isCreative(BlockEvent.BreakEvent)
isCreative(PlayerInteractEvent)
```

## 2. 覆盖

已加保护：

- GrainHarvestHandler；
- BushHarvestHandler；
- BushRightClickHarvestHandler；
- BushWasteHandler；
- CropWasteHandler；
- MacadamiaDropHandler；
- WildNutDropHandler；
- SpiceSeedDropHandler；
- StrawberryWasteHandler；
- StrawberrySeedDropHandler；
- TfcSeedReturnHandler；
- ACropSeedReturnHandler；
- UnifiedCropHarvestHandler（已有内联创造分支）。

## 3. 行为

创造模式：

- 不追加作物副产；
- 不追加种子；
- 不追加废枝叶；
- 不追加树枝/坚果/香料种子；
- 统一收获只移除方块。

## 4. 测试

```text
PASS: 393 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
```

## 5. 风险

- 未实机；
- 只覆盖列出的 handler；
- 第三方事件仍可能掉落；
- 创造模式是否应保留某些方块掉落需逐项确认。
