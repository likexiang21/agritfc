# 305 B 香料作物 P0-H 技术分析

> 日期：2026-10-28
> 目标：为 20 种 B 香料建立真实的作物/种子/产物注册与种植-生长-收获骨架。
> 约束：不推送；不伪造；贴图暂时指向 TFC。

## 1. 范围

本轮实现：

- `SpiceSpecies` 20 条：
  - 香料名、形态（herb/shrub/tree/vine/root/corm 数据）；
  - crop/seed/product 路径；
- `AgricultureSpices`：
  - 独立 `DeferredRegister.Blocks` / `DeferredRegister.Items`；
  - 20 个 `spice_crop/<id>` CropBlock；
  - 20 个 `spice_seed/<id>` BlockItem（可种植）；
  - 20 个 `spice/<id>` 产物；
- 20 套 blockstate（age 0..7）/block model/loot table；
- 40 个 item model；
- 40 个语言 key；
- 创造页加入 seeds/products；
- 客户端渲染层加入 spice crops。

**未实现**：树/藤/球茎的专属方块形态；当前 20 种都用普通 CropBlock。形态数据已记录，后续必须按 form 细分，不能把这个骨架当作最终形态完成。

## 2. 设计

- `SpiceSpecies` 纯数据，不依赖 Minecraft，便于原型测试；
- `AgricultureSpices` 独立注册，避免和 `AgricultureItems` 的静态初始化顺序冲突；
- `CropBlock` 使用原版 8 龄；
- 种子物品是 `BlockItem`，放置 CropBlock；
- loot table 掉 1 产物 + 1 种子；
- 临时模型 `minecraft:block/cross` + `tfc:block/crop/wheat_7`；
- 临时物品贴图 `tfc:item/straw`。

## 3. 测试

纯 Java：

```text
PASS: 222 crop P0 checks
```

新增：

- 20 个 species；
- form 非空；
- crop/seed/product 路径正确。

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

资源：

```text
PASS: 99 item models, 2 lang files, 17 recipes, 82 crop_waste,
      15 wild mushrooms, 4-stage bag, 79 nut leaf states, 20 spice crops, tags valid
```

## 4. 风险/未验证

- **未实机验证**种植/生长/收获/loot；
- 20 种作物都使用普通 CropBlock，树/藤/球茎形态未实现；
- 种子/产物暂时只有临时贴图；
- 没有香料专属配方/加工链；
- 没有补 20 条 spice crop_waste；
- B 香料仍未完成“每种作物独立流程”的最终目标。

## 5. 下一步

1. 按 form 拆分 tree/vine/corm 方块；
2. 香料初加工/配方；
3. spice crop_waste 20 条，补齐 102；
4. 实机验证；
5. TFC 29 剩余覆盖。

## 6. P0-I：20 条 spice crop_waste（追加）

已实现：

- 20 个 `spice_waste/<spice>` 物品；
- 20 个 item model + en/zh 语言；
- 9 个草本香料废料进 `compost_greens/high`，11 个其余香料进 `medium`；
- `CropWasteHandler` 增加 `tfcagricultureplus:spice_crop/<id>` 分支：
  - 只在该 CropBlock 最大 age 时掉落；
  - 不取消原作物破坏；
  - 原产物/种子仍按 loot table 掉落；
- 总 crop_waste：82（A/TFC）+ 20（B 香料）= **102**。

校验：

```text
PASS: 242 crop P0 checks
PASS: 99 item models, 2 lang files, 17 recipes, 102 crop_waste,
      15 wild mushrooms, 4-stage bag, 79 nut leaf states, 20 spice crops, tags valid
```

边界：香料仍是普通 CropBlock，树/藤/球茎形态未实现；未实机。

