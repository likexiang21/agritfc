# OPEN-ISSUES 运行问题台账

> 日期：2026-10-29
> 来源：真实客户端动态日志/截图
> 规则：只记录，不伪造修复；状态变更必须写证据。

## OPEN-001 两种枯死灌木重复（用户 2026-10-29 首次报告）

**状态：reverted-by-user-direction（2026-10-29）/ 未实机**

- **本方案的 B 过滤已按用户指令撤销**；以下为历史记录。
- 曾新增 `neoforge:remove_features` biome modifier；
- 目标 `#minecraft:is_overworld` + 125 个 TFC biome；
- 移除 `tfc:plant/dead_bush` / `tfc:plant/dead_bush_patch`；
- A `dead_cane` 仍存在（没有 placed feature，无法用同一机制过滤）；
- 因此是“移除 TFC 枯死灌木、保留 A 枯死藤蔓”；若方向反了需回退；
- 未实机验证 schema/注入；
- 证据：docs/532、533。
- 用户 2026-10-29 指令：“枯死灌木读取 TFC 原版处理方式”；已删除 `remove_duplicate_dead_bush.json`，恢复 TFC 原版 worldgen；B 不再过滤（docs/555、556）。

### 现象

截图中相邻出现两种枯死的“灌木”：

- 一种显示为 **枯死的灌木**；
- 另一种也被称为 **枯死的藤蔓/灌木**；
- 两者都是枯褐色装饰植株，视觉上重复。

截图：

`mod_rebuild/docs/audit/open-issue-001-dead-bush.png`

### 可能来源

已检查客户端 jar：

- TFC：
  - `block.tfc.plant.dead_bush` → `枯死的灌木`
  - `block.tfc.plant.dead_berry_bush` → `枯死的灌木`
- A（TFCFarmingPlus）：
  - `block.tfcfarmingplus.plant.dead_cane` → 名称含“藤蔓”

B 自身没有注册 `dead_bush` / `dead_vine` / `dead_cane` 方块。

### 初步判断

- 这是 **TFC 与 A 的枯死装饰方块/世界生成并存**；
- 不是 B 新增的两种枯死灌木；
- 二者都自然生成在同一区域，造成重复观感。

### 可能处理方向（未执行）

1. B 侧数据包/biome modifier 过滤 A 的 `dead_cane` 世界生成；
2. 让 A 侧移除重复的 dead cane；
3. 统一命名/模型（但用户已说暂不处理视觉）；
4. 只保留 TFC dead bush / dead berry bush 的一种。

### 证据

- 截图：`open-issue-001-dead-bush.png`
- 客户端 jar 资源检查：TFC/A 名称与方块 ID
- 当前日志：未出现与枯死灌木相关的 B ERROR

## OPEN-002 客户端大量 `Unknown recipe category: tfcagricultureplus:in_world/...`

**状态：fixed-static / runtime-unverified（2026-10-29）**

- 根因：`ClientRecipeBook` 跳过 `isSpecial()=true` 的配方；`MortarRecipe`/`FoodMixingBowlRecipe` 未覆盖；
- 已为两者补 `isSpecial() = true`；
- 4 个自定义 Recipe 全部通过 `check_recipe_is_special.py`；
- 18:28 日志来自旧 jar；当前源码已覆盖；
- 未实机确认日志消失；
- 证据：docs/536、537。

### 现象

客户端 recipe book 对 B 的 `tfcagricultureplus:in_world/...` 配方输出：

```text
Unknown recipe category:
tfcagricultureplus:in_world/tfcagricultureplus:in_world/...
```

数量很多；不影响世界加载，但污染客户端日志。

### 判断

B 的 `InWorldRecipe` 是 `isSpecial()` 的自定义配方；客户端 recipe book 没有对应的分类。

### 可能处理方向

- 注册/映射 recipe book category；
- 或把这些配方从 recipe book 分类查询中排除；
- 需确认 1.21.1 的正确 API，不能静态猜。

## 动态日志状态（2026-10-29 18:36 后）

- 游戏 PID 36176（java）曾运行；
- 世界已加载：
  ```text
  Starting integrated minecraft server version 1.21.1
  Total time to load game and open world was 50.115597 seconds
  ```
- 18:36:36 日志显示 `Saving and pausing game...`，之后无新行；
- 当前运行的是已迁移的最终 jar：
  ```text
  spiceCrops=15, spiceTrees=5, cropWaste=82, wildMushrooms=15
  ```
- 实时 tail job：`pwsh-f4390ba7e5b34963`（仍运行，等待新日志）。


## OPEN-003 厨房家具全是同一套皮容器，无功能差异（用户 2026-10-29 第二个问题）

**状态：fixed-static-scope（P1-2 + sink；用户限定水槽仅取水，2026-10-30）/ 未实机**

- 6 种家具按 `StorageKind` 实施不同过滤/堆叠上限：
  - counter 任意/64；
  - half 任意/16；
  - sink 仅流体容器/1；
  - spice_rack 仅 `#tfcagricultureplus:spices`/64；
  - food_display 仅食物/64；
  - fruit_bowl 仅食物/1；
- 6 种独立显示名；
- 6 个共享模型已差异化（docs/559、560）；仍共用 9 格菜单/屏幕；sink 已有 4000 mB 水罐 capability，并支持手持容器装水/倒水；无 GUI/清洗/保鲜；
- 非 sink 家具支持潜行右击快速存/取（docs/589、590）。
- 未实机。
- 证据：docs/522、523、540、541、546、547、559、560、583、584、589、590、609、610。
- 2026-10-29 扩展：sink_cabinet 增加 4000 mB 水罐 + block capability（docs/540、541）。

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

**状态：fixed-static-recipes（P0-3 + P2-4，2026-10-29）/ 未实机**

- 工作方块已补 174 条配方 + 173 个有效 loot table（`lumber_pile` 无物品，已删除错误自掉落）；
- 204 条家具占位配方已重做为 6 种不同图案，使用 TFC/AFC lumber、rod、wrought iron sheet、glass；
- 本地 shaped 冲突 groups=347/347，旧的 food_display/sink_cabinet 冲突消失；
- 204 个家具 loot table 已复核存在（每个掉落自身）；家具功能仍 P1-2 部分分化；
- 未实机。
- 证据：docs/516、517、534、535、609、610。

- 证据：docs/516、517。

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

**状态：fixed-static（P0-4 names + icons，2026-10-29）/ 未实机**

- 246 个农业名称键/语言改为逐物种人工名称；
- 510 个木材/家具/木工名称键/语言改为“木材名+中文家具名”；
- 中英双语同步；
- 中文 item/block 名称中的 ASCII 原始 ID 为 0；
- 2026-10-29 扩展：82 个 crop_waste 图标映射到已有 A/TFC 作物贴图，不再全部共用 `tfc:item/straw`（docs/563、564）。
- 证据：docs/518、519、563、564、603、604、612、613、614、615。

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

## OPEN-006 陶盘 knapping 配方与 TFC 陶碗完全相同（用户 2026-10-29 第五个问题，已按用户澄清修正）

**状态：fixed-static（P0-1 + OPEN-006 review，2026-10-29）/ 未实机**

- 新 pattern：`[" ### ","#####"," ### ","     ","     "]`
- 碰撞扫描：B/TFC/A 无 `tfc:clay` 重复。
- 证据：docs/512、513。
- 链路复核：未烧盘→陶盘；白盘→烧制→15 色染料盘；旧碗转换配方已删除；
  `check_ceramic_plate_chain.py` problems 0（docs/538、539）。

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

- **直接冲突已确认**：

  B 的 `knapping/ceramic/unfired_plate.json`：

  ```json
  {
    "type": "tfc:knapping",
    "knapping_type": "tfc:clay",
    "pattern": ["#   #", " ### ", "     ", "#   #", " ### "],
    "result": { "count": 1, "id": "tfcagricultureplus:ceramic/unfired_plate" }
  }
  ```

  TFC 的 `data/tfc/recipe/knapping/ceramic/unfired_bowl.json`：

  ```json
  {
    "type": "tfc:knapping",
    "knapping_type": "tfc:clay",
    "pattern": ["#   #", " ### ", "     ", "#   #", " ### "],
    "result": { "count": 4, "id": "tfc:ceramic/unfired_bowl" }
  }
  ```

  两者 **knapping_type + pattern 完全相同**，只是输出不同；这是确定的配方冲突，不是“风格不一致”。

- 已经用静态扫描脚本确认：
  - `mod_rebuild/docs/audit/prototype/find_knapping_collisions.py`

## OPEN-013 7 个研钵 knapping 配方共用同一 `tfc:rock` pattern

**状态：resolved-static（2026-10-29）**

- 7 个 pestle 的 pattern 相同，但 `ingredient` 全部不同；
- TFC `KnappingRecipe.matches` 同时检查 `ingredient`；
- `check_pestle_disambiguation.py`：7/7 unique；
- 不存在实际配方冲突；未实机验证；
- 证据：docs/536、537。

### 证据

`find_knapping_collisions.py` 还发现 B 的 7 个 pestle：

```text
basalt_pestle
diorite_pestle
gabbro_pestle
granite_pestle
obsidian_pestle
quartzite_pestle
slate_pestle
```

全部使用：

```text
knapping_type = tfc:rock
pattern       = ["  #  ", "  #  ", "  #  ", " ### ", "  #  "]
```

每个结果不同，但 pattern 完全相同。

### 风险

- TFC 自身的 rock 配方也有一组 pattern 重复（例如不同岩石类别的刀头/标枪头），说明 TFC 可能按输入材料或其他规则消歧；
- 但 B 的 7 个 pestle 是否真的能按岩石区分，尚未验证；
- 当前至少是**配方选择语义不明**，属于必须通过 TFC `tfc:knapping` 规则确认的高风险项。

## OPEN-007 农业育种/培育流程未按技术文档（用户 2026-10-29 第六个问题）

**状态：partially-fixed-static（P2-1 + vegetative items，2026-10-29）/ 未实机**

- 新增 `CropPropagation`，8 种繁殖方式；
- 82 个 crop-waste 作物全部显式分类；
- 播种门改为：TFC 保持直播；A/B `SEED_DIRECT` 放行；其它方式取消并提示具体方法；
- 育苗盘仍是非直播物种的移栽路径；
- 已实现 21 个无性繁殖物品；水生作物已支持水源放置；种子处理接入湿草/堆肥/木灰/石灰；仍缺母株性状、完整农艺管理；
- 未实机。
- 证据：docs/528、529、542、543、550、551、585、586、595、596、599、600。
- 2026-10-29 扩展：新增 21 个 `propagation_stock/<species>`，覆盖 CORM/TUBER/RHIZOME/CROWN/DIVISION/RUNNER；产品 1→2 合成，耕地放置；水生作物已加水源放置路径；母株性状仍缺（docs/542、543、550、551）。

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

**状态：partially-fixed-static（P1-3，2026-10-29）/ 未实机**

- 新增作物分类 × 中英；
- 新增 7 个主题 × 中英 = 14 个 entry：
  - 收获/废枝叶
  - 种子与育苗
  - 谷物捆与湿草
  - 香料
  - 坚果与叶状态
  - 蘑菇与菌包
  - TFC 灌木
- 每页单主题、短段落/列表，不暴露原始 ID；
- 未实机检查分页/排版；
- 已增加 14 个 spotlight 页（中英）作为物品入口；厨房 intro 已增加 6 个 crafting 页 + 2 个 spotlight 页；养蚕 intro 已增加 1 个 crafting 页 + 3 个 spotlight 页；木工 intro 已增加 5 个 spotlight 页；没有图片；
- 证据：docs/524、525、548、549、567、568、569、570、571、572、601、602。

### 修正后的静态检查

上一版记录“B 没有任何 Patchouli 资源”是**错误**的，现修正：

B 实际有手册资源，但挂在 TFC 的 field guide 下：

```text
assets/tfc/patchouli_books/field_guide/
  en_us/categories/agriculture_plus_kitchen.json
  en_us/categories/agriculture_plus_silkworm.json
  en_us/categories/agriculture_plus_woodwork.json
  en_us/entries/agriculture_plus_kitchen/intro.json
  en_us/entries/agriculture_plus_silkworm/intro.json
  en_us/entries/agriculture_plus_woodwork/intro.json
  ... zh_cn 同名 6 个文件
```

即只有 **3 个旧主题**：厨房、养蚕、木工。

### 真正问题

1. **没有作物系统章节**：
   - 无 crop / 香料 / 坚果 / 蘑菇 / 育苗 / 菌包 / 树叶状态页面；
   - 用户无法从手册理解本次农业重做。
2. 现有 3 个条目是超长纯文本块（`patchouli:text` 连续多页），没有：
   - 配方页；
   - 图/表；
   - 分步骤；
   - 与 JEI/REI 的联动。
3. 部分条目图标/分类可能指向旧内容，容易被用户理解为“手册不可读”。

结论：手册不是“没有资源”，而是**内容覆盖严重不足、可读性差**；用户批评成立。

## OPEN-009 重复木碗与陶碗（用户 2026-10-29 第八个问题）

**状态：fixed-static（P0-2，2026-10-29）/ 未实机**

- 已删除 B 的 `bowl/wood`、`bowl/ceramic` 物品、2 个配方、item model、语言键、创造页入口；
- 移除 `DishEating.transferToBowl` 和 `ServingPlateBlock` 的碗交互；
- 盘装菜仍可直接食用，但不再分装到 B 碗；这是明确的功能缩减。
- 证据：docs/514、515。

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

**状态：partially-fixed-static（P1-1，2026-10-29）/ 未实机**

- 19 个 metal can item model 改为 `tfc:fluid_container`；
- 新增 19 × 2 个 `.filled` 名称键；
- capability/tag/容量未改；
- 未实机验证装入/倒出/图标变化；
- 已补 .filled 名称与 JEI 信息页；基础贴图仍借用 TFC 金属板/桶 overlay，属于视觉问题；
- 证据：docs/520、521、552、553、605、606。

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

**状态：fixed-static-tfc-parity（2026-10-29）/ AFC 扩展未对齐 / 未实机**

- 对照 TFC Woodworking 1.2.4 的 40 条 wood/stripped_wood 配方；
- B 的 40 条复制配方 type/pattern/result/key 结构一致（problems 0）；
- 发现 `lumber_pile` 没有方块物品，却错误补了自掉落表；已删除并修正 P0-3 的 174→173；
- AFC 14 木材 28 条为 B 扩展，不是原配方；
- 模型/blockstate 对照已完成；碰撞/交互/音效仍未逐项对照；未实机；
- 证据：docs/530、531。
- 历史模型对照：对齐前 blockstate variants 20/20 不同、model parent/texture/item parent 各 60/60 不同（docs/544、545）；该差异已由 561/562 修复。
- 2026-10-29 视觉对齐：TFC 20 木材复用 TFCW 原模型/blockstate/item model/图标；blockstate 差异 0、item parent 差异 0，model parent/inner 仅命名空间替换；AFC 14 木材为风格扩展，item 图标复用 AFC 原木图标（docs/561、562、565、566、607、608）。

### 现状

- B 有 `TimberBlocks` / `TimberPieceBlock` / `LumberPileBlock` 等木工内容；
- 目前静态审计只能确认这些类/资源存在；
- 未建立与 A/TFC 原木工内容的逐项对照表；
- 配方、尺寸、木材覆盖和原版 TFC 木工流程是否一致尚未审计。

结论：作为高优先级待审计项记录，不能声称已复原原作。

## OPEN-012 JEI 可读性差且未表现新增加工（用户 2026-10-29 第十一个问题）

**状态：fixed-static-coverage（P1-4，2026-10-29）/ 未实机**

- 34 个 B 晾架加入 Firmalife drying JEI catalyst；
- 10 个设备信息页（中英双语）：
  cooking_pan / nursery_tray / mushroom_bag / silkworm_rack / drying_rack /
  cutting_board / log_cutting_board / knife_block / mortar / kitchen_storage；
- 新增 20 个 JEI 信息语言键；
- 已新增金属罐/陶盘/繁殖材料信息页；已为 IN_WORLD 分类添加 axe/saw 催化剂；仍未新增 B 独立 recipe category；烹饪锅仍是动态组合；
- 未实机确认显示；
- 证据：docs/526、527、552、553、579、580、581、582。

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

## 动态日志更新（2026-10-29 18:49 后）

- 新 jar 已在 mods 并成功加载；
- 世界加载完成；
- 18:49:12 玩家退出；18:49:13 客户端正常 `Stopping!`；
- 没有 B 相关 fatal error；
- 当前 open issues 均来自用户实机截图/静态审查，尚未修改代码。


## OPEN-014 木工朝向属性初始化导致启动崩溃（2026-10-30 日志）

**状态：fixed-static / 待实机**

- 日志：`crash-2026-10-30_09.33.00-fml.txt`、`logs/latest.log`；
- 首个异常：`TimberPieceBlock.<init>` line 22 在状态定义中设置不存在的 `facing`；
- 根因：`createBlockStateDefinition` 在 `super()` 期间调用，子类 `directional` 字段尚未初始化；
- 修复：拆分为 `TimberPieceBlock`（无 facing）与 `DirectionalTimberPieceBlock`（有 facing），`TimberBlocks` 按 part 选择；
- 日志中的 `unbound value`（debarked_half/serving_plate）是首个注册异常导致的次级错误，需启动确认消失；
- 未实机（无 Java 21/PCL 环境）；
- 证据：docs/616、617。


## OPEN-015 二次崩溃：本模组 oven 配方触发 Firmalife JEI 绘制（2026-10-30）

**状态：fixed-static / 待实机**

- 日志：`crash-2026-10-30_22.13.48-client.txt`、`logs/latest.log`；
- 崩溃：`NoClassDefFoundError: net/dries007/tfc/config/TemperatureDisplayStyle` at Firmalife `OvenCategory.draw`；
- 本模组 15 条 `firmalife:oven` 配方把 B 的 raw 面团放进该 JEI 分类，触发绘制路径；
- 修复：15 条全部迁移为 `tfc:heating`（400°C，result_item 保持），删除 `recipe/oven/`；
- 校验：B 数据中 `firmalife:oven` 引用 0，heating 16 条，build 成功；
- 未实机；
- 证据：docs/618、619。
- 同日志附带修复：log_pile→lumber_pile 标签、plant_fiber_rope pattern→shapeless、Patchouli crop/strawberry→seeds/strawberry、icon 验证只认 item model（docs/620、621）。


## OPEN-016 种子处理静态 Item 初始化（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- SeedTreatmentHandler 静态字段在模组构造期读取 BuiltInRegistries.ITEM，可能拿到 AIR；
- 修复：改为事件触发时解析 compost/wood_ash/lime；
- 全项目扫描 static final Item/Block 为 0；
- build 成功；
- 证据：docs/624、625。


## OPEN-017 香料 herb 形态映射缺失（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `SpiceSpecies` 有 9 个 `herb` 形态；
- `AgricultureSpices.newSpiceCrop` 的 switch 没有 `case "herb"`，全部落入 vanilla `CropBlock`，`SpiceCropBlocks.Herb` 未使用；
- 修复：补 `case "herb"`；
- build 成功；
- 证据：docs/626、627。


## OPEN-018 事件处理器缺少取消状态检查（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- 8 个 BlockEvent.BreakEvent 处理器在事件取消后仍可能掉落/移除方块；
- 修复：统一增加 if (event.isCanceled()) return;；
- 覆盖 BushHarvest/BushWaste/GrainHarvest/Macadamia/SpiceSeed/StrawberrySeed/StrawberryWaste/WildNut；
- build 成功；
- 证据：docs/628、629。


## OPEN-019 育苗盘接受 TFC 种子但无法移栽（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `NurseryTrayBlockEntity.canAccept` 只检查种子路径，TFC 种子也能放入；
- `SeedlingItem` 只接受 BlockItem，TFC 种子不是 B 作物 BlockItem，移栽失败；
- 修复：canAccept 拒绝 `tfc:` 种子，TFC 保持原版直播；
- build 成功；
- 证据：docs/630、631。


## OPEN-020 野草香料种子源包含无种子树种（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `SpiceSeedDropHandler` 从全部 20 个 SpiceSpecies 随机；
- 5 个 tree 形态无 `AgricultureSpices.SEEDS` 条目，掉落被静默跳过；
- 修复：只从 `SEEDS.containsKey` 的物种随机；
- build 成功；
- 证据：docs/634、635。


## OPEN-021 TFC 灌木采收不产废枝（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `BushHarvestHandler` / `BushRightClickHarvestHandler` 采收成功后没有掉 `bush_waste`；
- 上一轮取消检查使 `BushWasteHandler` 不再补掉落；
- 修复：两个采收处理器成功后追加 `bush_waste`；
- build 成功；
- 证据：docs/636、637。


## OPEN-022 TFC 灌木废枝重复掉落（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `BushWasteHandler` 注册在 `BushHarvestHandler` 之前；
- 结果灌木破坏时前者先掉一份废枝，后者取消事件再掉一份；
- 修复：`BushWasteHandler` 跳过 `LIFECYCLE == FRUITING`，废枝只由采收处理器掉；
- build 成功；
- 证据：docs/638、639。


## OPEN-023 右键/左键交互未检查已取消事件（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `BushRightClickHarvestHandler`、`DirectSeedPlantingGate`、`CuttingBoardLeftClickHandler`、`InWorldRecipeHandler` 未检查 `event.isCanceled()`；
- 保护/取消场景下仍可能收获、取消种植或执行世界内配方；
- 修复：统一增加取消早退；
- build 成功；
- 证据：docs/640、641。


## OPEN-024 自定义树叶未重写 codec（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `SpiceTreeLeavesBlock` / `NutLeavesBlock` 构造函数带 species，但继承 `LeavesBlock.codec()`；
- codec 被使用时可能构造普通 `LeavesBlock`，丢失 species 类型；
- 修复：两个类重写 `public MapCodec<? extends LeavesBlock> codec()`；
- build 成功；
- 证据：docs/642、643。


## OPEN-025 香料作物形状子类未重写 codec（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `SpiceCropBlocks` 的 6 个形状类继承 `CropBlock.codec()`，会退化成普通 CropBlock；
- 修复：6 个类分别重写 `public MapCodec<? extends CropBlock> codec()`；
- build 成功；
- 证据：docs/644、645。


## OPEN-026 木料堆取空后残留空方块（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `LumberPileBlockEntity.updateState` 将 count 强制为至少 1；
- 取走最后一块木料后留下空库存方块，且破坏无掉落；
- 修复：库存为 0 时 `level.removeBlock(worldPosition, false)`；
- build 成功；
- 证据：docs/646、647。


## OPEN-027 木料堆 insert all 参数未生效（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `LumberPileBlockEntity.insert` 无论 `all` 真假都只插入 1；
- 修复：`amount = min(held.count, all ? available : 1)`；
- build 成功；
- 证据：docs/648、649。


## OPEN-028 盘子方块实体缺少客户端同步（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `ServingPlateBlockEntity` 直接继承 `BlockEntity`，没有 getUpdateTag/getUpdatePacket；
- 渲染器依赖 `plateStack`，客户端读不到，菜肴不可见；
- 修复：继承 `TFCBlockEntity`，set/clear 使用 `markForSync()`；
- build 成功；
- 证据：docs/650、651。


## OPEN-029 锅方块实体渲染内容不同步（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `CookingPanBlockEntity.sync()` 只发方块状态更新，不发 BlockEntity 数据；
- 客户端渲染器读不到 entries，锅里食材不可见；
- 修复：改用 `TFCBlockEntity.markForSync()`；
- build 成功；
- 证据：docs/652、653。


## OPEN-030 育苗盘空盘拒绝所有种子（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `NurseryTrayBlockEntity.canAccept` 写成 `if (seed.isEmpty() || stack.isEmpty()) return false;`；
- 空托盘永远不能放入种子，已有种子反而可接受；
- 修复：改为 `if (!seed.isEmpty() || stack.isEmpty()) return false;`；
- build 成功；
- 证据：docs/654、655。


## OPEN-031 育苗盘客户端也掉落种子（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `NurseryTrayBlockEntity.dropSeed` 未检查 `level.isClientSide()`；
- 客户端移除方块时生成客户端幽灵物品并清空客户端 BE；
- 修复：非服务端直接 return；
- build 成功；
- 证据：docs/656、657。


## OPEN-032 种子处理右键入口未检查取消（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `SeedTreatmentHandler` / `SeedTreatmentGrowthHandler` 未检查 `event.isCanceled()`；
- 取消场景下仍可能消耗材料、写组件、调度生长；
- 修复：两个入口增加取消早退；
- build 成功；
- 证据：docs/658、659。


## OPEN-033 锅油勺只模拟不转移（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `PanInteractions.scoopOil` 使用 `tryFluidTransfer(..., false)`，只模拟；
- 副手油不减少、锅油罐不增加，可反复触发；
- 修复：改为 `true` 实际转移；
- build 成功；
- 证据：docs/660、661。


## OPEN-034 锅可直接加入腐烂食材（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `isItemValid` 拒绝腐烂，但玩家右键走 `addIngredient`，该方法只检查 `FoodCapability.has`；
- 修复：`addIngredient` 增加 `isRotten` 检查；
- build 成功；
- 证据：docs/662、663。


## OPEN-035 副手锅铲搅拌损坏主手物品（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `CookingPanBlockEntity.stir` 固定扣 `EquipmentSlot.MAINHAND`；
- 副手锅铲不消耗耐久，主手物品被错扣；
- 修复：stir 接收 InteractionHand，按实际手选择槽；
- build 成功；
- 证据：docs/664、665。


## OPEN-036 锅可加入腐烂黄油作固态油（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `addSolidOil` 只检查 firmalife:food/butter，未检查 `isRotten`；
- 修复：增加 `FoodCapability.isRotten` 拒绝；
- build 成功；
- 证据：docs/666、667。


## OPEN-037 晾架自动化插入直接别名调用方物品栈（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `RackItemHandler.insertItem` 把调用方 stack 直接交给 `ItemStackHandler`；
- 空槽实际插入时可能别名同一对象；
- 修复：先 `stack.copy()` 再插入；
- build 成功；
- 证据：docs/668、669。


## OPEN-038 方块全量列表重复 drying rack（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `registerVariant` 已把 drying rack 放进 `ALL`；
- `all()` / `allIds()` 又追加 `DRYING_RACKS`，导致重复；
- 修复：只追加独立注册的 `TimberBlocks.ALL`；
- build 成功；
- 证据：docs/670、671。


## OPEN-039 种子处理生长 boost 未限制在农田（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `SeedTreatmentGrowthHandler` 只检查种子组件，不检查点击方块是否农田；
- 非农田/已有作物右击也可能触发 applyBoost；
- 修复：只允许 FarmBlock 或 ID 以 farmland 结尾的方块；
- build 成功；
- 证据：docs/672、673。


## OPEN-040 堆叠盘子食用会丢盘/状态串改（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `DishEating.finishItemUse` 对堆叠盘调用 `setCount(1)` 丢盘；
- `PanDishData.write(stack, rest)` 改整堆份数；
- 修复：堆叠时拆一张盘子、原 stack shrink(1)、单盘写 rest/清空后放回背包；
- build 成功；
- 证据：docs/674、675。


## OPEN-041 创造模式吃盘仍消耗/改份数（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `DishEating.eatFromPlateBlock` / `finishItemUse` 未检查 instabuild；
- 创造模式吃菜仍扣盘/改 dish 份数；
- 修复：两入口在 dish 合法后提前返回；
- build 成功；
- 证据：docs/676、677。


## OPEN-042 摆盘食物破坏时整块与切片同时掉落（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `PlaceableFoodBlock` 默认 loot table 掉整块，`onRemove` 又掉剩余切片；
- 修复：`getDrops` 返回空，剩余食物只由 BE dropContents 掉；
- build 成功；
- 证据：docs/678、679。


## OPEN-043 满份摆盘食物不返还整块（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- OPEN-042 后所有摆盘食物都只掉切片，满份也不返还整块；
- 修复：`PlaceableFoodBlockEntity` 增加 isFull，getDrops 满份返回方块物品，onRemove 满份不再 dropContents；
- build 成功；
- 证据：docs/680、681。


## OPEN-044 废枝叶/湿草/坚果壳未接入 TFC 堆肥标签（2026-10-31 全盘检查）

**状态：fixed-static / 待实机**

- 82 crop_waste、10 bush_waste、wet_grass、8 nut_shell 只有掉落/燃料，没有 TFC 堆肥标签；
- 修复：按文档 291 §4.1.2 分类追加到 `tfc:compost_greens/*` 与 `tfc:compost_browns/high`；
- 保留 TFC 原始 values；
- build 成功；
- 证据：docs/682、683。


## OPEN-045 坚果/坚果粉/野生蘑菇没有食物定义（2026-10-31 全盘检查）

**状态：fixed-static / 待实机**

- 8 坚果、8 ground_nut、15 wild_mushroom BlockItem 在 `tfc/food` 无定义；
- `FoodCapability.has` 为 false，不能食用/不进入腐烂营养链；
- 修复：新增 31 个 FoodDefinition；
- build 成功；
- 证据：docs/684、685。


## OPEN-046 20 种香料废枝叶未接入堆肥（2026-10-31 全盘检查）

**状态：fixed-static / 待实机**

- `spice_waste/*` 20 项只有掉落，无配方/标签/堆肥；
- 修复：herb 9 种进 `compost_greens/high`，其余 11 种进 medium；
- build 成功；
- 证据：docs/686、687。


## OPEN-047 TFC/Firmalife 作物/植物被豁免（2026-10-31 用户要求）

**状态：fixed-static / 待实机**

- `DirectSeedPlantingGate` 对 `tfc:` 种子提前返回；育苗盘拒绝 TFC 种子；
- Firmalife 8 个香草植物不在 B 废枝叶链；
- 修复：
  - TFC 种子进入 CropPropagation 表，归 SEED_DIRECT；
  - 育苗盘 + SeedlingItem 支持 tfc:crop 解析；
  - 新增 FirmalifePlantWasteHandler 追加 spice_waste；
  - 未知外部种子不再静默取消；
- build 成功；
- 证据：docs/688、689。


## OPEN-048 严格评估 P0：统一收获器把 BlockEntity 传成 null（2026-10-31）

**状态：fixed-static / 待实机**

- `UnifiedCropHarvestHandler` 取消玩家破坏后自行补掉落；
- `Block.getDrops(..., null, ...)` 导致 TFC `crop_yield_uniform` 读不到 CropBlockEntity，回落到 min=0；
- 影响 A 76 + TFC 19 个非谷类物种；
- 修复：传 `level.getBlockEntity(pos)`；
- 证据：docs/690、691。

## OPEN-049 严格评估 P1：TFC/Firmalife 覆盖与提示缺口（2026-10-31）

**状态：部分修复 / TFC 草莓右键已补，TFC/AFC 叶视觉与工业作物废料仍按边界保留**

- TFC 前缀豁免改为逐项查表，补 TFC 11 + A 10 分类；
- cane/strawberry/wild_crop 废枝叶补漏；
- 播种门加育苗提示；
- Firmalife 8 香草改为刀具门槛且不重复掉 B 产物；
- **未完成**：Firmalife 另外 12 个 plant 方块仍无 B 侧钩子；
- 证据：docs/690、691。


## OPEN-050 严格评估 P0-2：B 香料/草莓无法在 TFC 耕地存活（2026-10-31）

**状态：fixed-static / 待实机**

- SpiceCropBlocks 6 形态 + STRAWBERRY_CROP 继承原版 CropBlock，mayPlaceOn 只接受 vanilla FarmBlock；
- TFC 耕地是 tfc:farmland/*，不是 vanilla FarmBlock；
- 修复：TfcFarmlandCropBlock 同时接受 FarmBlock 与 TFCTags.Blocks.FARMLANDS；
- 同时修 DirectSeedPlantingGate/SeedTreatmentGrowthHandler 的耕地判断、wild_crop 的 mature、wintergreen ID；
- build 成功；
- 证据：docs/692、693。


## OPEN-051 严格评估收尾：Firmalife 全植物覆盖 + 种子处理 BE（2026-10-31）

**状态：fixed-static / 待实机**

- 新增 14 个 Firmalife crop_waste（cocoa/fig/grape/pineapple/nightshade 等），覆盖 12 个 plant/* + 2 个 grape_string_plant_*；
- 8 香草保留 spice_waste + 刀具门槛；
- 种子处理 boost 对 A/TFC 支持的 CropBlockEntity 直接 setGrowth；
- TfcFarmlandCropBlock 增加 codec；
- build 成功；证据 docs/694、695。


## OPEN-052 严格评估 P1 收尾：放置覆盖、boost 目标校验、growthTickStep（2026-10-31）

**状态：fixed-static / 待实机**

- SeedlingItem/CormItem/SpiceRootItem 增加 canBeReplaced 检查，避免覆盖已有方块；
- SeedTreatmentGrowthHandler 只对种子生效、只对可替换目标、非直种不排队；
- 种子处理 boost 改用 TFC CropHelpers.growthTickStep，不再 setGrowth；
- build 成功；证据 docs/696、697。


## OPEN-053 其他功能严格评估 P0/P1（2026-10-31）

**状态：fixed-static / 待实机**

- P0 worldgen biome 标签只含 vanilla，TFC 世界不生成蘑菇/坚果树/香料树；已加 85 个 TFC 陆生 biome；
- P1 厨房食物过滤改用 FoodCapability.has；
- P1 锅铲勺油 tryFluidTransfer 参数顺序修正；
- P1 lang 斜杠键改点号；
- P1 菌包/育苗盘 stage 模型区分；
- 证据 docs/698、699。


## OPEN-054 其他功能严格评估 P2：掉落上下文与锅自动化（2026-10-31）

**状态：fixed-static / 待实机**

- ServingPlate/PlaceableFood getDrops 改用 loot 上下文捕获的 BE；
- CookingPan automationView 委托 addIngredient，漏斗食材进入 entries；
- build 成功；证据 docs/700、701。


## OPEN-055 其他功能 P2 清理：创造守卫/自检计数（2026-10-31）

**状态：fixed-static / 待实机**

- FirmalifePlantWasteHandler 加 CreativeGuards；
- 客户端渲染自检 total 加入香料作物与盘子；
- build 成功；证据 docs/702、703。


## OPEN-056 2026-11-02 低峰批次：作物/设备/数据代码修复

**状态：fixed-static / 待实机**

- 谷物 age：A 9 种 7、TFC maize 5，修复玉米包不可达与提前收获；
- 树苗：树干替换树苗、树叶非永久、空间检查、去日志；
- 晾架批量产量按输入数量放大；
- 刀架逐件取放；餐盘 1px 碰撞；晾架/石臼/案板 actionbar；
- 育苗盘 BE 同步、完成态破坏掉幼苗；
- 可放置食物满份掉落保留新鲜度，BER 不再重复渲染；
- `TimberBlocks.ALL` 补 lumber_pile；
- 补 `tfcfarmingplus:materials/plant_fibers` tag；
- pimento 贴图路径修复；坚果/香料叶草色 tint；
- 香料链 ground_spice 消费端 + black_pepper 配方；
- 世界生成 rarity + climate；
- TFC 草莓右键补 B 种子/废枝叶；
- 证据：最终审计报告 §6；构建成功；jar 见验证记录。
