# 287 农作物重做要求归档（从既有文档提取）

> 日期：2026-10-28
> 性质：**要求摘录/归档**，不是新设计；本轮没有实现农作物重做。
> 来源：`126`（B 实现总方案，现已归档）、`117`（农业重设计计划，现已归档）、`280 §11`、`282 §5`。

## 0. 关键问题：A 已经占用了 TFC 作物资源，B 的 29 作物重做不是“从零开始”

这是上一版归档漏掉的真正关键点。

### 0.1 文档证据

`117 §〇.2.2` 明确记录：A 当前有 **6 个 TFC 作物模型覆盖**：

```text
assets/tfc/models/block/crop/cabbage_age_0.json
assets/tfc/models/block/crop/cabbage_age_1.json
assets/tfc/models/block/crop/cabbage_age_2.json
assets/tfc/models/block/crop/cabbage_age_3.json
assets/tfc/models/block/crop/cabbage_age_4.json
assets/tfc/models/block/crop/cabbage_age_5.json
```

这些文件在**当前源码里仍然存在**：

```text
mod_rebuild/tfcfarmingplus/src/main/resources/assets/tfc/models/block/crop/cabbage_age_0..5.json
```

`117 §5.5.2` 也把它们列为 A1 覆盖组（6 个），说明它们不是历史记录，而是**A 当前实际发布的资源覆盖**。

此外，A 当前还实际写入了：

- **26 个** `assets/tfc/patchouli_books/**` 手册文件（`117` 旧稿写 14，已漂移）；
- **19 个** `data/tfc/tags/**` 标签文件（`117` 旧稿写 21，已漂移）。

### 0.2 这为什么是 B 作物重做的关键阻塞

1. **TFC 的 29 种作物包含 `cabbage`（卷心菜）**。
2. B 的 A1 目标要求覆盖 `assets/tfc/models/block/crop/<name>_age_*.json`，其中 cabbage 的路径与 A 当前占用的 6 个文件**完全相同**。
3. 两个独立 jar 写同一路径时，谁生效取决于**资源包/mod 加载顺序**，不是由 B 的“A1”语义保证。可能出现：
   - A 的 cabbage 覆盖赢 ⇒ B 的 cabbage 重做看不见；
   - B 赢 ⇒ A 的 6 个 TFC 模型变成死资源，A 的“仅接入”行为被 B 隐式改变；
   - 两者在某些情况下都不完整 ⇒ TFC cabbage 回退到 TFC 原版十字模型。
4. `117 §〇.2` 的最高优先级是“先拆 A/B 包”，但**当前 A 仍拥有 TFC 作物模型**，说明拆分尚未真正完成；B 直接在 A 的路径上写资源，会破坏“A 可独立发布 / B 可独立卸载”的目标。
5. B 的 `assets/tfc` 当前只有 Patchouli（无作物模型），但 **A 的 6 个 TFC 模型不是“B 的 0”**：B 作物完成度是 0，**A 已经做了 cabbage 样板**，所以 B 的 29 作物重做不是 greenfield，而是**跨 jar 所有权迁移**。

### 0.3 第二个关键阻塞：TFC 资源覆盖的 EUPL 授权链

`277 §3.2` 和 `THIRD-PARTY-ASSETS.md §1` 已经指出：

- TFC 是 **EUPL-1.2**，不是 MIT；
- A 的 6 个 `assets/tfc/models/block/crop/cabbage_age_*.json` 是“基于 TFC 模型的资源覆盖”；
- A 的 26 个 TFC 手册文件是对 TFC `field_guide` 的修改/补译；
- A 还有 8 张 strawberry 作物贴图与 TFC **逐像素相同**；
- 项目自身许可证文本/通知缺失，`mods.toml` 却写 MIT；
- 当前状态是 **EUPL 义务未履行**。

因此，B 的 A1“29 种作物资源覆盖”不只是画图任务：

1. 覆盖 TFC 的 blockstate/model/texture/loot_table 可能构成对 TFC 资产的**修改/衍生**；
2. 直接复制/改写 TFC 模型或贴图会触发 EUPL 的源码/许可证/通知义务；
3. 项目当前没有解决 MIT 与 EUPL 的冲突，也没有 TFC 的 LICENSE/NOTICE 与来源登记；
4. 在授权链解决前，把“覆盖 TFC 作物资源”做成发布内容，属于**许可证阻断项**，不是普通实现项。

**结论：作物重做的第一道门不是美术，也不是 29 个 ID 清单，而是“A 的 TFC 跨命名空间覆盖所有权 + TFC EUPL 授权链”这两个前置问题。**

### 0.4 实测审计

用 `tfcagricultureplus/tools/audit_crop_ownership.py` 对当前树实测：

```text
A TFC crop model files: 6
  assets/tfc/models/block/crop/cabbage_age_0..5.json
B TFC crop model files: 0
A TFC Patchouli files: 26; B TFC Patchouli files: 12
A TFC tag files: 19; B TFC tag files: 4
Current exact A/B crop-model path overlap: 0
Future B 29-crop target collision:
  assets/tfc/models/block/crop/cabbage_age_0..5.json: A owns, B target would collide
```

“当前精确重叠 0”只是因为 B 还没开始写作物资源；B 一旦按 A1 写 cabbage，6 个路径就会与 A **同路径冲突**。所以不能用“当前没有重复文件”掩盖这个前置冲突。

### 0.5 因此正确的第一步

不是直接写 29 套 blockstate/model/texture，而是先决定并执行：

- A 的 6 个 `assets/tfc/models/block/crop/cabbage_age_*.json` 是否：
  - **移交给 B**（A 删除，B 负责全部 29 种，包括 cabbage）；
  - 或 **A 保留 cabbage**（B 明确跳过 cabbage，依赖 A 作为 29 种之一）；
  - 或 **改为 B 只在无 A 时覆盖**（NeoForge 资源条件加载，复杂度高）。
- A 的 26 个 TFC Patchouli 文件与 B 的作物/浆果手册如何分家；
- A 的 19 个 TFC 标签文件与 B 的作物/浆果标签如何合并（必须 `replace=false`，不能清空 A 已有条目）。

**在这些所有权决定之前，B 的 29 作物重做不能算“已开始”，也不能直接铺资源。**

## 1. 归属与总目标

### 1.1 归属

农作物重做属于 **B（`tfcagricultureplus`）**，不属于 A（`tfcfarmingplus`）：

- 来源：`archive/126-b-module-implementation.md` §10.1 A1/A2；`280` §11.1–11.3。
- B 的目标是**覆盖 TFC 自带的作物/灌木资源**，让玩家装 B 后连 TFC 原版作物也变成同一套美术与形态语言。
- 这不是 A 的职责：A 的 86/77 种是 A 自有作物；B 覆盖的是 TFC 的 29 种作物和 10 种灌木；草莓已经由 A 迁移为普通作物。

### 1.2 一句话目标

> 让 TFC 的 29 种作物“看起来像我们画的”：
> 7 种形状、每物种 6 龄 + 枯死态，风格与 A 的 86 种完全同族；
> 玩家分不出哪些是“我们的”、哪些是“TFC 的”。

来源：`126` §10.2 A1；`280` §11.1。

## 2. 覆盖清单

### 2.1 TFC 29 种作物

实测 `assets/tfc/blockstates/crop/*.json` 恰好 29 个：

```text
alfalfa · barley · beet · cabbage · canola · carrot · cassava ·
garlic · green_bean · jute · lentil · maize · melon · oat ·
onion · papyrus · peanut · potato · pumpkin · radish ·
red_bell_pepper · rice · rye · soybean · squash · sugarcane ·
tomato · wheat · yellow_bell_pepper
```

来源：`117` §5.1；`126` §10.2 A1；`280` §11.1。

⚠️ 特殊项：

- `melon` / `pumpkin` 的 `crop/*.json` 实测 variants 为 0（它们是果实方块，不是普通作物年龄方块）——覆盖时不能按普通 6 龄处理。
- `wheat` / `barley` / `oat` / `rye` / `rice` / `squash` 等实测为 8 个 age 变体，不是 6 个。
- `tomato` / `green_bean` 实测有 `stick=false/true`，共 20 变体。
- `maize` / `jute` / `papyrus` 有 `part=bottom/top`。
- `sugarcane` 实测 12 变体。

⇒ **“6 龄”是目标描述，不是可照抄的变体数；必须以 TFC 实际 blockstate 的完整变体空间为准。**

### 2.2 TFC 10 种浆果灌木（草莓已移出）

实测 TFC 有 13 个 `*_bush` blockstate，减去 2 个枯死态 `dead_berry_bush` / `dead_bush`，原本为 11 种。

但 **A 已经把草莓迁移为普通作物**：
- A 的 `crops-manifest.json` 中有 `strawberry`（普通作物）；
- A 有 `crop/strawberry`、`wild_crop/strawberry`、`dead_crop/strawberry`、种子与掉落表；
- A 的 `data/tfc/tags/worldgen/placed_feature/feature/berry_bushes.json` 已 `remove` 了 `tfc:plant/strawberry_bush_patch`，即 TFC 草莓灌木不再自然生成；
- 因此 B 的 TFC 灌木重做目标应为 **10 种，不含草莓**。

```text
blackberry · blueberry · bunchberry · cloudberry · cranberry ·
elderberry · gooseberry · raspberry · snowberry · wintergreen
```

来源：`117` §5.1；`126` §10.2 A2。

⚠️ **草莓不在 B 的 10 种重做范围内**：它是 A 的普通作物；TFC 草莓灌木只被 A 关闭世界生成/隐藏，B 不重复迁移。

## 3. 作物重做的实现要求

### 3.1 手段

**2026-10-28 用户新口径：不是资源旁路，TFC 29 要替换/覆盖种植与收获流程。** 资源覆盖只是其中一部分：

- `assets/tfc/blockstates/crop/<name>.json`
- `assets/tfc/models/block/crop/<name>_age_*.json`
- `assets/tfc/textures/block/crop/<name>_*.png`
- `data/tfc/loot_table/blocks/crop/<name>.json`

关键约束：

- TFC 作物的方块类/blockstate 可以被 B 扩展或接管（如新增 `nut_state` 叶状态）；
- 必须做旧存档迁移与回退，不能再假设“只换皮”。
- 覆盖 blockstate 时**必须覆盖它的全部变体**（`age × fruiting × part × stick`），不能只写 `age`；A 的 kale 曾因漏掉 `fruiting` 导致 6 个模型永远不显示（`AGENTS.md` 第 48 轮）。

### 3.2 掉落

- 覆盖 `data/tfc/loot_table/blocks/crop/<name>.json`；
- 接入 B 的主/次产品，使用 TFC 的 `tfc:extra_products`；
- 验收要求：**TFC 原种植/收获/掉落被 B 覆盖**；旧 raw 只作回退基线，必须提供迁移；
- 副产物：**`tfcagricultureplus:wet_grass`**（B 新物品；谷物捆脱粒/野草/未成熟补偿；晒干→`tfc:straw`）；废枝叶只在真实产出时逐作物 `crop_waste/<crop>`（→`tfc:compost_greens/*`），不设通用 `green_waste`。
- 风险：覆盖 `data/tfc/loot_table/**` 会盖住邻居更新；需要 `OVERRIDE-REGISTRY.md` 登记 + 对齐检查。

来源：`126` §10.2 A1。

### 3.3 形态/美术

- 7 种形状：普通 / 双段 / 攀爬 / 蔓延 / 水生 / 莲座 / 可摘；
- 每物种 6 龄 + 枯死态（但实际变体数按 TFC 真实 blockstate，见 §2.1）；
- 与 A 的 86 种完全同族；
- 玩家不应能区分“B 改过的 TFC 作物”和“A 原生作物”。

### 3.4 验收

来自 `126` §10.2 A1：

1. 29 种在游戏里都长成 B 的风格；
2. 29 种的种植/收获/掉落由 B 覆盖，旧流程可回退；
3. 存档里已种的 TFC 作物不消失，旧状态有迁移默认值。

### 3.5 280 号追加的规划项

`280` §11.4 / §11.5 在原要求上追加了完整批次范围：

| 子项 | 目标 |
|---|---|
| TFC 29 作物 | 7 形状 × 6 龄 + 枯死态；同族外观 |
| 资源覆盖 | 覆盖 TFC `blockstates` / `models` / `textures` |
| 方块/行为 | 作物方块、野生生成、生长/收获、种子/产物 |
| 标签/兼容 | 覆盖 TFC 作物/浆果标签，不改 A 标签；蜂蜜/蜜蜂兼容 |
| 手册/语言 | 作物/浆果的 B 手册条目 |
| 贴图 | 全部重绘（用户已说明贴图由合作者更新） |

**已定案（2026-10-28）：按 `280` 的完整行为口径**；`126 A1` 的“仅资源覆盖、方块类不变”作废。TFC 29 要替换种植/收获/掉落，不是资源旁路。

## 4. 草莓与灌木要求

### 4.1 10 种灌木（草莓已迁移）

- 走 B 的灌木管线：`MyBerryBushBlock` / `MySpreadingBushBlock`（旧类名，当前 B 已重建）；
- 与 A 的 12 种同族；
- 资源覆盖 `assets/tfc/blockstates/plant/<name>_bush.json` 等；
- **不要动 A 已写的标签**（红线 2）；
- 覆盖 TFC 标签时只能追加、不能清空；
- 蜂蜜仍能访问 `buzzing_leaves`（A 已接的 48 条果树叶子）。

来源：`126` §10.2 A2。

### 4.2 草莓：已由 A 迁移，不再是 B 的例外任务

- **草莓已经由 A 迁移为普通作物**：A 的 manifest、`crop/strawberry`、野生/枯死作物、种子和掉落表均已存在；
- A 的 TFC 世界生成标签已 `remove` `tfc:plant/strawberry_bush_patch`，TFC 草莓灌木不再自然生成；
- 因此 B **不重复创建草莓普通作物**，也不把 TFC 草莓灌木列为 B 的 10 种重做目标；
- 验收改为：确认 A 的草莓普通作物仍可种植/生长/收获，B 的 10 种灌木重做不误伤它。

来源：`117` §5.2；`126` A2。

**已定案**：草莓由 A 迁移为普通作物；B 不再新建/迁移草莓，也不把 TFC 草莓灌木列入重做。

## 5. 当前实际状态

`280` §11.2 实测：

- B 的 `assets/tfc/` 目前**只有 Patchouli 手册**；
- 但 **A 已有 6 个 TFC cabbage 模型覆盖**、26 个 TFC 手册文件、19 个 TFC 标签文件（见 §0）；A 不是“无 TFC 资源”的干净态；
- 没有 `blockstates/crop/`、`models/block/crop/`、`textures/block/crop/`；
- 没有 B 的 `CropBlock` / `BerryBushBlock` 子类；
- 没有对 `tfc:plant/*` / TFC 作物方块 ID 的注册覆盖；
- 但 A 已经在 TFC `assets/tfc/models/block/crop/` 中写入了 cabbage 6 个模型，所以 B 不能假设 TFC 资源是原始的；
- 作物/浆果仍由 A 和 TFC 提供；
- **A2 要求没有进入 B 的任何已实现批次**；
- 同时，A 的 6 个 TFC cabbage 模型是 B 29 作物重做的**同路径前置冲突**，不是无关历史。

完成度表（`280` §11.4）：

| 子项 | 当前 |
|---|---|
| TFC 29 作物 | 0 |
| TFC 10 灌木（不含草莓） | 0 |
| 资源覆盖 | 0（仅 Patchouli） |
| 方块/行为 | 0 |
| 标签/兼容 | 0 |
| 手册/语言 | 0 |
| 贴图 | 0（待合作者重绘） |

## 6. 需求中明确不能违反的边界

1. B 不写 `assets/tfcfarmingplus/**` / A 的资源或代码；
2. 覆盖 TFC 标签用 `replace=false`，不能清空 TFC/A 原有条目；
3. 覆盖 TFC blockstate 必须覆盖全部实际变体，不能漏 `fruiting` / `part` / `stick`；
4. TFC 原掉落可被覆盖，但必须提供旧值回退；
5. 方块状态可扩展，必须做存档迁移；
6. 草莓必须绕过 A 的标签，不改 A；
7. 蜂蜜/蜜蜂兼容不能破坏；
8. 贴图由合作者重绘，当前所有新贴图只能是占位，不能当最终验收。

## 7. 仍需用户/文档owner决定的点

1. **验收基线已定**：按 `280` 的完整行为重做；TFC 29 种植/收获/掉落由 B 覆盖。
2. **TFC cabbage 所有权**：A 现在已有 6 个 `assets/tfc/models/block/crop/cabbage_age_*.json`；B 的 29 作物重做必须决定 A 删除移交、A 保留 B 跳过、还是做条件覆盖。
3. **A 的 TFC 手册/标签如何与 B 合并**：A 当前有 26 个 TFC 手册文件、19 个 TFC 标签文件；B 的作物/浆果手册和标签不能直接覆盖清空。
4. **草莓已定案**：A 已是普通作物，B 不再新建/迁移草莓；后续只需确保 B 的灌木重做不误伤 A 草莓。
5. **“6 龄”与实际变体冲突**：以 TFC 实际 blockstate 为准，还是强行把所有作物压成 6 龄？后者会改 TFC 方块状态并影响存档，不建议。
6. **7 种形状的逐作物映射**：现有文档只给了形状分类，没有给出 29 种作物各自的 shape 分配表，需要补一份映射后才能施工。
7. **melon/pumpkin 特殊处理**：它们不是普通 age 作物，是按“果实方块”覆盖还是排除出 29 种清单？
8. **“野外生成/标签”已纳入 B 覆盖范围**：包含 TFC 作物 worldgen、标签、作物行为，需要迁移方案。
9. **TFC EUPL 授权链**：B 覆盖 TFC 作物资产前，必须先解决 `277 §3.2` 的 EUPL 通知/许可证/来源登记；否则该批次不应发布。
