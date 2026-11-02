# 700 其他功能严格评估 P2 修复：掉落上下文与锅自动化

> 日期：2026-10-31
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 餐盘/可放置食物掉落读取时机的确定性修复

严格评估指出：`ServingPlateBlock` / `PlaceableFoodBlock` 的 `getDrops` 在
`params.getLevel().getBlockEntity(pos)` 里读 BE，而 vanilla 在 `playerDestroy/getDrops`
之前已经执行 `removeBlock`；若 BE 已被移除，会丢失盘子/整块食物。

修复：改用 loot 上下文自带的、破坏前捕获的 BlockEntity：

```java
params.getOptionalParameter(LootContextParams.BLOCK_ENTITY)
```

- `ServingPlateBlock.getDrops`：从捕获的 `ServingPlateBlockEntity` 返回完整盘子栈；
- `PlaceableFoodBlock.getDrops`：从捕获的 `PlaceableFoodBlockEntity` 判断 `isFull()`，
  满份返回方块物品，部分份仍由 `onRemove` 掉切片；
- 不再依赖方块被移除后的 level 查找。

## 2. 烹饪锅自动化输入

原 `automationView = inventory`：漏斗/自动化只把食材写入 `inventory`，
不会创建 `entries`，而 `serve` 只看 `entries`，这些食材既不烹饪也不产出。

修复：`automationView` 改为委托 `IItemHandler`：

- `insertItem` 调用 `addIngredient`；
- 插入前检查热量、油、食物/腐烂、空槽；
- `extractItem` 继续使用 inventory；
- 每次自动化插入一个食材并创建对应 `PanCookingEntry`。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
json 6535 / models 3709 / blockstates 539 / item_models 957
lang 1107 / 1107 / missing 0 / extra 0
final_static_audit problems 0
check_loot_worldgen_tags problems 0
check_model_textures missing 0
```

当前 jar：

```text
2,954,689 bytes
SHA-256 9CAA9D331665B567C14FF283C7C45022FCF0F9F9A22CB81671B246B2629A106A
```

## 4. 仍未完成

- 未实机；
- 菌包破坏丢进度、锅/水槽流体掉落、部分设备无 BER、KitchStorage 共用 9 槽 GUI；
- P1-5/P1-6 的坚果叶 overlay、香料树贴图；
- 14 个 Firmalife 废枝叶图标/中文名、香料/草莓 age 模型、AFC 树叶资产。
