from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
text = p.read_text(encoding="utf-8")

extra = r'''

## OPEN-003 厨房家具全是同一套皮容器，无功能差异（用户 2026-10-29 第二个问题）

**状态：recorded / 未处理**

### 证据

- `KitchenStorageBlock.StorageKind` 有 6 种：
  `counter_cabinet / half_cabinet / sink_cabinet / spice_rack / food_display / fruit_bowl`
- 全部使用同一个：
  - `KitchenStorageBlockEntity`
  - `KitchenStorageMenu`
  - `KitchenStorageScreen`
- 差异只有：
  - 方块高度；
  - 名称；
  - 模型/贴图。
- 没有各自独立的：
  - 槽位规则；
  - 存储类别；
  - 交互逻辑；
  - 自动化接口；
  - 食物展示/调味/水槽功能。

结论：6 种家具本质上都是同一种“容器”，只是换皮；确认用户描述属实。

## OPEN-004 全部工作方块没有合成表，家具只有低质量占位配方（用户 2026-10-29 第三个问题）

**状态：recorded / 未处理**

### 工作方块

静态检查 B 的 recipe 输出 ID：

- `log_cutting_board/*`
- `cutting_board/*`
- `knife_block/*`
- `mortar/*`
- `drying_rack/*`
- `cooking_pan`
- `lumber_pile`
- `silkworm_rack`
- `log_pile`

均**没有找到对应 `result.id` 的合成/制作配方**。
只有 `butter_block / jelly_block / sugar_block / whole_cheese / whole_pie` 等 5 个产物有配方。

### 家具

`recipe/kitchen/`：

- 6 类 × 34 木材 = **204 个配方**；
- 全部是简单 `crafting_shaped`，例如 `counter_cabinet/oak`：
  ```json
  pattern: ["PPP", "PPP", "   "]
  key: { "P": { "item": "tfc:wood/planks/oak" } }
  result: { "id": "tfcagricultureplus:counter_cabinet/oak", "count": 1 }
  ```
- 仅覆盖 TFC/AFC 木材；无五金、无工具、无加工设备参与。

结论：工作方块无法合成；家具配方确为低质量占位。

## OPEN-005 农业内容名称差、不可读且有未翻译片段（用户 2026-10-29 第四个问题）

**状态：recorded / 未处理**

### 证据：截图

`mod_rebuild/docs/audit/open-issue-004-crop-waste-names.png`

### 证据：资源

- `crop_waste` 的本地 item model 有 82 个；
- 所有这些 model 的 `layer0` 只有 **1 个贴图**：`tfc:item/straw`；
- zh_cn 名称统一为：
  ```text
  作物废枝叶（spinach）
  作物废枝叶（lettuce）
  ...
  ```
- 即：
  - 全部同一占位贴图；
  - 名称只是“中文类别 + 原始 ID”；
  - 无物种可读中文名；
  - 未翻译 ID 直接暴露在 tooltip。

同类问题也存在于：
- grain bundles：`谷物捆（millet）` 等；
- spice：`香料（basil）` 等；
- nuts：`坚果（pistachio）` 等；
- tree saplings：`坚果树苗（pistachio）` 等。

结论：用户对名称可读性的批评属实。

## OPEN-006 陶盘/碗配方冲突且未参考陶罐流程（用户 2026-10-29 第五个问题）

**状态：recorded / 未处理**

### 碗

`bowl_ceramic.json`：

```json
{
  "type": "minecraft:crafting_shapeless",
  "ingredients": [{ "item": "tfc:ceramic/bowl" }],
  "result": { "id": "tfcagricultureplus:bowl/ceramic", "count": 1 }
}
```

- 把 TFC 已有陶瓷碗直接转换为 B 的重复碗；
- `bowl_wood.json` 用 2 个 TFC lumber 直接做木碗，也与 TFC `tfc:wooden_bowl` 重复。

### 陶盘

- `knapping/ceramic/unfired_plate.json` → `ceramic/unfired_plate`
- `heating/ceramic/unfired_plate.json` → `plate/ceramic`
- 15 个 `plate_ceramic_*.json` 是对 `plate/ceramic_white` 的染色彩盘配方；
- 但 `plate_ceramic_white` 本身没有直接配方文件，实际基底依赖 `plate/ceramic` 命名与加热路径，和 TFC 陶罐的“黏土揉捏/制坯/烧制/上色”流程并不一致。

结论：碗是重复物品替代；陶盘流程与 TFC 陶罐实现不一致，且与碗的简化配方形成冲突。

## OPEN-007 农业育种/培育流程未按技术文档（用户 2026-10-29 第六个问题）

**状态：recorded / 未处理**

### 现状

- 代码提供：
  - `DirectSeedPlantingGate`：取消 A/B 种子直接播种；
  - `nursery_tray` + `seedling` + `SeedlingItem`；
  - `SEED_TREATMENT` DataComponent。
- 但 291 计划中的逐物种繁殖方式（种子/匍匐茎/分株/冠芽/种薯/种球/扦插等）没有逐项实现；
- 目前所有 A/B 种子统一走“育苗盘→seedling→移栽”；
- 没有按物种区分：
  - 哪些可以直播；
  - 哪些必须育苗；
  - 哪些用匍匐茎/分株/冠芽；
  - 哪些是种薯/种球/种瓣。

结论：用户“育种流程胡写、无视技术文档”的批评有静态依据。

## OPEN-008 帕秋莉手册不可读（用户 2026-10-29 第七个问题）

**状态：recorded / 未处理**

### 静态检查

在 B 的 `src/main/resources` 中未找到：

- `assets/tfcagricultureplus/patchouli_books/**`
- `data/tfcagricultureplus/patchouli_books/**`

B 自身没有专属 Patchouli 书页资源；现有手册内容来自外部/前置模组或缺失。

结论：需要确认书 ID，并补 B 自己的可读书页；当前不可读问题成立。

## OPEN-009 重复木碗与陶碗（用户 2026-10-29 第八个问题）

**状态：recorded / 未处理**

### TFC 已有

- `block.tfc.wooden_bowl` → Bowl
- `item.tfc.ceramic.bowl` → Bowl
- `item.tfc.ceramic.unfired_bowl` → Unfired Bowl

### B 新增

- `tfcagricultureplus:bowl/wood`
- `tfcagricultureplus:bowl/ceramic`

且 B 的陶瓷碗配方只是把 `tfc:ceramic/bowl` 转换过来。

结论：重复物品问题属实；应改用 TFC 原碗，或明确替代关系/迁移方案。

## OPEN-010 金属罐交互/液体显示失效（用户 2026-10-29 第九个问题）

**状态：recorded / 未处理**

### 现状

- `MetalCanItem extends FluidContainerItem`，容量 500 mB；
- 使用 TFC fluid tag `tfcagricultureplus:metal_can_fluids`；
- 但 B 的 metal can item model 是：
  ```json
  {"parent":"item/generated","textures":{"layer0":"tfc:item/metal/sheet/copper"}}
  ```
- 没有：
  - fluid overlay model；
  - item property/component 显示液体；
  - 与 TFC 陶罐一致的 fluid render/交互层。

结论：用户关于“物品无法反映装入液体、交互几乎失效”的描述有静态依据。

## OPEN-011 木工内容移植不尊重原有内容和配方（用户 2026-10-29 第十个问题）

**状态：recorded / 未处理**

### 现状

- B 有 `TimberBlocks` / `TimberPieceBlock` / `LumberPileBlock` 等木工内容；
- 目前静态审计只能确认这些类/资源存在；
- 未建立与 A/TFC 原木工内容的逐项对照表；
- 配方、尺寸、木材覆盖和原版 TFC 木工流程是否一致尚未审计。

结论：作为高优先级待审计项记录，不能声称已复原原作。

## OPEN-012 JEI 可读性差且未表现新增加工（用户 2026-10-29 第十一个问题）

**状态：recorded / 未处理**

### 现状

B 的 JEI 插件只有三个 category：

- `MortarRecipeCategory`
- `CuttingBoardRecipeCategory`
- `InWorldRecipeCategory`

未覆盖/未完整展示：

- 陶盘/碗/陶器流程；
- 烤箱/锅/搅拌碗；
- 金属罐液体；
- 木工 in-world 加工；
- 育苗盘/菌包/树木生长链；
- 多数 A/TFC 联动配方。

结论：用户对 JEI 可读性和覆盖面的批评有静态依据。

## 动态日志更新（2026-10-29 18:48 后）

- 新 jar 已在 mods 并成功加载；
- 世界加载完成；
- 日志停在 `Saving and pausing game...`；
- 当前 open issues 均来自用户实机截图/静态审查，尚未修改代码。
'''

p.write_text(text + extra, encoding="utf-8")
print("appended issues 003-012")
