# 325 作物系统代码阶段审计（目标未完成）

> 日期：2026-10-29
> 目的：在第 12 个目标轮次结束时，给出**已落地代码**与**未完成计划**的诚实清单，避免把部分实现当成计划完成。
> 结论：**目标未完成**，不标记完成；未推送、未提交远程。

## 1. 已落地并编译/静态校验的代码

| 模块 | 代码 | 证据 |
|---|---|---|
| 产量账本 | `CropYieldLedger` | 纯 Java 校验 |
| 16 谷物映射 | `GrainCrop` | 16 条、maxAge/seed/crop block |
| wet_grass + 16 bundle | `AgricultureItems.WET_GRASS/GRAIN_BUNDLES` | 17 item models |
| 谷物捆脱粒 | 16 条 `crafting/grain_bundle_*.json` | 输出 A/TFC 真实谷粒 |
| 湿草干燥 | `drying/wet_grass.json` | Firmalife drying |
| 成熟谷物处理 | `GrainHarvestHandler` | 取消原破坏 + bundle + seed |
| 82 A/TFC crop_waste | `CropWasteCrops` + `CropWasteHandler` | 82 个物品/模型/tag |
| 20 香料 waste | `AgricultureSpices.WASTES` + handler | 102 crop_waste |
| 10 TFC bush waste | `BushSpecies/AgricultureShrubs/BushWasteHandler` | 10 物品 |
| TFC 灌木采收 | `BushHarvestHandler` | SeasonalPlantBlock 采收 |
| 15 野蘑菇 | `WildMushroomBlock/AgricultureBlocks.WILD_MUSHROOMS` | 15 blockstates/worldgen |
| 蘑菇 worldgen | configured/placed/biome modifier | 15 features |
| 4 阶段菌包 | `MushroomBagBlock/BE` | 自然专用拒绝 |
| TFC/AFC 叶 nut_state | `TFCLeavesNutStateMixin` + 79 blockstates | 5 坚果组 |
| 8 坚果物品 | `AgricultureItems.NUTS` | 4 个已接树 |
| 8 坚果粉 | `GROUND_NUTS` + mortar | 8 配方 |
| 20 香料作物骨架 | `SpiceSpecies/AgricultureSpices` | 20 CropBlock |
| 20 香料粉 | `GROUND_SPICES` + mortar | 20 配方 |
| 种子处理 | `SEED_TREATMENT` + handler | 3 阶段 |
| 种子处理生长 | `SeedTreatmentGrowthHandler` | Bonemealable 1/2/3 |
| 育苗盘 | `NurseryTrayBlock/BE` | 3 stage + seedling |
| 幼苗移栽 | `SeedlingItem` | BlockItem 目标 |
| TFC 种子返还 | `TfcSeedReturnHandler` | 29 物种，6 谷物除外 |

## 2. 验证证据

```text
gradle compileJava --rerun-tasks
BUILD SUCCESSFUL

PASS: 99 item models, 2 lang files, 17 recipes, 102 crop_waste,
      10 bush_waste, 15 wild mushrooms, 4-stage bag, 79 nut leaf states,
      20 spice crops, 20 ground spices, 8 ground nuts, tags valid

PASS: nursery tray + seedling resources
PASS: 282 crop P0 checks
```

注意：PowerShell 因既有 deprecation 警告出现非零退出码，但 Gradle 构建成功；没有把它当作成功指标。

## 3. 仍未完成的目标项

### 3.1 TFC 29 完整流程

- 已做：成熟收获事件、种子返还、谷物 bundle、crop_waste。
- 未做：**替换 TFC 原种植流程**；没有 B 种子处理后的 TFC 专属种植状态；没有 29 作物完整 blockstate/model/种植/移栽/农艺覆盖。

### 3.2 A 87 完整生产/培育链

- 现有 A 资源，但没有逐作物六环节行为、育苗/移栽/农艺、加工配方全部落地；当前只覆盖湿草/废枝叶/种子处理/育苗骨架。

### 3.3 TFC 10 灌木

- 已做：废枝 + 破坏采收替换。
- 未做：原右键采摘替换、B 灌木方块/育苗/扦插。

### 3.4 B 43

- 香料：有骨架/粉，但树/藤/球茎形态未实现；
- 坚果：有物品/叶状态/粉，但 pistachio/cashew/macadamia 无树；无壳/油/烤制；
- 蘑菇：有野生/菌包，但 11 种可栽培的完整配方/环境/产出平衡未完成。

### 3.5 通用

- 未实机验证；
- 大多数贴图仍是 TFC 临时路径；
- 没有完整 159 条逐作物验收；
- 没有最终资源/行为全量回归。

## 4. 结论

本轮目标轮次结束时，代码已经覆盖了计划中的多个关键垂直切片，但**没有完成 291/292 的全部要求**。

因此：

- **不标记目标完成**；
- 不写“全部完成”；
- 不推送。

下一步必须继续：
1. TFC 29 种植替换；
2. A/B 完整六环节；
3. 香料形态、坚果树、蘑菇平衡；
4. 全量实机回归。
