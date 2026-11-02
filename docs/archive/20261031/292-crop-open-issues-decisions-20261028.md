# 292 作物系统未决问题：分析与解决方案

> 日期：2026-10-28
> 对应 291 §13 的 12 项未决问题，并新增“废枝叶不是所有作物都有”的第 13 项。
> 性质：决策建议，不是实现；本轮未推送、未提交远程。

## 决策总表

| # | 问题 | 决定 | 实施影响 |
|---:|---|---|---|
| 1 | A 87 还是文档 86 | **以实际 `crops-manifest.json` 的 87 为准**；86 是旧稿漂移 | 文档统计、矩阵行数、批次以 87 计算；不改 A 资源 |
| 2 | A/TFC/B/灌木的范围 | A 87 全链；B 43 全链；**TFC 29 替换/覆盖种植+收获+掉落**；TFC 10 灌木替换采收/再生 | TFC 不再做资源旁路；TFC 29 走 B 的种植/收获行为 |
| 3 | 育苗盘/移栽 API | **B 自有方块 + B 自有苗物品 + `in_world`**；不 mixin TFC | 新方块/物品/BE 全在 `tfcagricultureplus`；TFC 作物保持原生长 |
| 4 | TFC 种子处理产物 | **DataComponent 加在现有 TFC/A 种子上**，不新增 116 个处理种子物品 | 组件 `seed_treatment`（stage/soak/germination/dressing）；无重复 ID |
| 5 | TFC/A raw 是否调整 | **TFC/A raw 都允许被 B 覆盖**；TFC 29 用 bundle/湿草/新叶状态替换原流程；旧 raw 只作回退基线 | 不再绕过 TFC；存档迁移与回退方案必须同步做 |
| 6 | A 的 6 个 TFC cabbage 模型 / EUPL | **B 接管 TFC 作物资源**：A 删除 6 个 `assets/tfc/models/block/crop/cabbage_age_*`，B 写入自己的 29 作物覆盖；补 EUPL 通知/来源/许可证 | A 变成纯接入；B 唯一负责 TFC 作物覆盖；EUPL 义务可追溯 |
| 7 | 双主产（纤维+油、坚果+油）的分账 | **每作物一张 yield ledger**：raw 只记一次，main/processed/byproduct 分开；双主产按同一 raw 的两个 fraction 计算，不重复计 raw | 避免“油料又算油又算饼为两份主产”；平衡表可审计 |
| 8 | 20 香料的树/藤/草本形态 | **5 类形态**：草本、灌木、乔木、攀援藤、球茎；逐物种归类和气候/支架 | 树/藤不塞进普通 `MyCropBlock`；藤类必须搭架 |
| 9 | 15 蘑菇的世界生成/刷新与栽培 | **全部 15 种世界自然生成并随机刷新**；可栽培 11（菌包/腐木），**自然专用 4**（porcini/morel/chanterelle/black_truffle）禁止菌包 | 野生蘑菇学 TFC `PlantBlock`/`SeasonalPlantBlock` 随机刻刷新；自然专用只可采 |
| 10 | 已有乔木坚果的叶状态/掉落 | 已有树加 **`nut_state` 叶状态**（无/花/青/熟），按 TFC 季节挂果、成熟随机掉落；**5 种挂已有树** + **3 种新 B 树**（pistachio/cashew/macadamia） | 不另造重复树；覆盖树叶全部 blockstate/model；旧存档默认无果 |
| 11 | 潮湿草与谷物捆 | **A 10 + TFC 6 长秆谷物全部 bundle→脱粒→wet_grass**；TFC 原收获/raw 由 B 覆盖；野草/未成熟补偿保留 | 湿草是 B 新物品 `tfcagricultureplus:wet_grass`，不是 TFC 已有物品 |
| 12 | 废枝叶是否每作物都有 | **不是**。只有实际加工产生叶/茎/藤/荚/皮渣的作物才有 `crop_waste/<crop>`；谷物、油料、纤维、坚果、蘑菇走各自副产 | 102 条有 crop_waste，其余无；不造统一 `green_waste` |
| 13 | TFC 10 灌木是否做六环节 | **替换采收/再生流程 + 资源覆盖**；不做育苗/移栽/农艺 | 覆盖 TFC 灌木原采收；草莓已是 A 普通作物，不列入 |

## 逐项分析

### 1. A 87 vs 旧文档 86

**分析**：`crops-manifest.json` 实际 87 项，旧文档 86 是历史数字；继续写 86 会让矩阵漏一项、验收少一行。

**决定**：以 87 为准；在 291/289 标注“87，旧稿 86 已废弃”。不改 A 的注册/资源。

### 2. 范围分层

**分析**：A 87、B 43、TFC 29 都要求有生产/培育闭环；TFC 29 不能只换贴图或绕过原流程，必须覆盖种植/收获/掉落。

**决定**：

| 层 | 内容 | 生产链 | 六环节 |
|---|---|---|---|
| A 87 | A 作物 | 完整 | 完整（B 提供加工/设备） |
| B 43 | 香料/坚果/蘑菇 | 完整 | 完整（B 自有作物） |
| TFC 29 | TFC 作物 | **替换/覆盖** | **完整六环节 + B 收获/掉落** |
| TFC 10 灌木 | TFC 灌木 | **替换采收/再生** | 不做六环节 |

### 3. 育苗/移栽 API

**分析**：TFC 作物方块没有育苗/移栽状态；mixin 会破坏存档和兼容。B 已有 `in_world` 框架和自定义方块能力。

**决定**：

- 新增 B 的 `nursery_tray` 方块 + BE；
- 苗/扦插枝为 B 物品或带组件；
- 移栽用 `in_world` 右键耕地；
- 不给 TFC 作物强行加育苗；TFC 仍直接播种。

### 4. TFC 种子处理

**分析**：为 116 种种子各造处理物品会产生大量重复 ID；TFC 种子物品不可替换。

**决定**：

- 使用 **DataComponent `seed_treatment`** 存在原种子上；
- 字段：`stage=soaked|germinated|dressed`、`crop`、`expires`；
- 不改变种子物品 ID/栈；
- A/B 种子同样用该组件，TFC 种子兼容。

### 5. raw 产量

**分析**：用户要求替换 TFC 原种植/收获流程，不允许绕过；因此 TFC/A raw 都可被覆盖，但必须做存档迁移与回退。

**决定**：

- TFC 29 raw 由 B 覆盖：bundle/湿草/新叶状态替换原流程；
- A 87 raw 同步按 profile 调整；
- 旧 raw/旧收获路径保留为回退基线；
- 存档迁移（已有作物/树叶/掉落）必须与覆盖同批验证。
- 平衡通过加工转化、副产物、种子返还实现；
- 20 次收获均值验收。

### 6. A 的 cabbage / EUPL

**分析**：A 现有 6 个 TFC cabbage 模型覆盖；B 的 29 作物覆盖 cabbage 会与 A 同路径冲突。TFC 资源是 EUPL 派生风险。

**决定**：

1. A 删除 6 个 `assets/tfc/models/block/crop/cabbage_age_*`；
2. B 建立全部 29 作物的 TFC 资源覆盖，并接管其种植/收获/掉落；
3. 发布物补 TFC EUPL 文本、版权行、来源/修改登记；
4. `THIRD-PARTY-ASSETS.md` 更新 6 个 cabbage 模型、29 作物资源、TFC 书页；
5. 若法务要求 A 不能带 TFC 覆盖，则 A 只保留自己的 `assets/tfcfarmingplus/**`，B 负责全部 TFC 命名空间。

### 7. 双主产分账

**分析**：亚麻/大麻/棉花既有纤维又有油；坚果既果仁又有壳；若 raw 记两次会虚增产量。

**决定**：

```text
raw = 一个作物每次收获的生物学产量（只记一次）
fraction_fiber = raw × 出麻率
fraction_oil   = raw × 含油率
byproduct      = cake / shives / shell / spent substrate
```

- 双主产不重复计 raw；
- 每个作物一个 ledger：raw、main、fiber/oil、byproduct、seedBack；
- 验收检查 `main + byproduct <= raw`（同一 fraction 内）。

### 8. 20 香料形态

**决定**：

| 形态 | 物种 |
|---|---|
| 草本 | basil · cilantro · cumin · oregano · dill · fennel · mustard · thyme · sage |
| 灌木 | bay_laurel · rosemary · sage（可归灌木） |
| 乔木 | cinnamon · clove · nutmeg · star_anise · pimento |
| 攀援藤 | black_pepper · vanilla |
| 球茎 | saffron |

- 草本走 B 的普通 crop；
- 灌木/乔木不塞普通 crop，使用 B 的 shrub/树/挂树接口；
- 藤类必须搭架；
- 气候按现实 + Firmalife 数据分配。

### 9. 15 蘑菇：世界生成、刷新与栽培边界

**分析**：蘑菇不能只是菌包系统；要像 TFC 野生植物一样在世界中生成并可持续刷新。部分蘑菇在现实中无法人工栽培，必须只能自然获得。

**决定**：

- **全部 15 种**都有世界自然生成 + 随机刻刷新，学习 TFC `PlantBlock`/`SeasonalPlantBlock` 的扩散/季节/气候/休眠；
- **可栽培 11 种**：oyster · shiitake · button · enoki · wood_ear · reishi · lions_mane · maitake · king_oyster · shimeji · turkey_tail；
- **只能自然刷新、不可培育 4 种**：porcini · morel · chanterelle · black_truffle；**禁止菌包配方**；
- 野生蘑菇方块按 biome/林地/树根/腐木生成；有 worldgen configured/placed feature + biome tag；
- 自然专用 4 种只用野生方块；菌包只对可栽培 11 种开放；
- 菌包仍为 `stage=0` 空包 → `1` 走菌 → `2` 出菇 → `3` 枯竭；废菌包 → 堆肥；
- 药用蘑菇效果分级并设上限。

### 10. 已有乔木坚果：新叶状态与随机掉落

**分析**：已有乔木不需要另造树；但需要让特定季节出现坚果，并让坚果自然掉落，而不是只在合成/右键时凭空产生。

**决定**：

- 在已有树叶方块增加 **`nut_state`** 叶状态：`0=无 / 1=花 / 2=青 / 3=熟`；
- 用 TFC 季节/日历驱动：夏季—秋季进入挂果，成熟后随机刻掉落坚果；
- 挂果时叶模型增加坚果 overlay；非挂果期隐藏；
- 玩家可右键采收；自然掉落也会在树下生成坚果物品实体；
- 覆盖树叶 blockstate/model 的**全部组合**，旧存档缺省 `nut_state=0`；
- 已有树：oak/acorn · chestnut/chestnut · pine/pine_nut · hickory/hickory_nut · beech/beechnut；A 的 almond/hazelnut/pecan/walnut；AFC hardy_chestnut/chinquapin 同样覆盖；
- 新树仅用于 pistachio/cashew/macadamia，不重复 A/AFC 已有坚果。

### 11. 潮湿草与谷物捆

**分析**：用户要求湿草是 B 新物品，并且湿草要来自加工流程；不允许绕过 TFC 原收获。

**决定**：

- 新物品 **`tfcagricultureplus:wet_grass`** —— B 新增，不是 TFC 已有物品；
- **A 10 + TFC 6 长秆谷物**全部走：
  `成熟收获 → grain_bundle/<crop> → 脱粒 → 谷粒 + wet_grass → 1:1 晒干 tfc:straw`；
- TFC 6 种（barley/oat/rice/rye/wheat/maize）也覆盖原收获，不再保留 TFC 直接掉谷粒/秸秆的路径；
- 野草 13 种：保留剪刀掉落，增加湿草分支；未成熟作物破坏用 `extra_products` 补湿草；
- 非 bundle：buckwheat / amaranth / quinoa；sugarcane 不属于谷物捆；
- 旧 raw 只作回退基线。

### 12. 废枝叶不是所有作物都有

**分析**：谷物、油料、纤维、坚果、蘑菇的实际副产不是“废枝叶”；强行每作物一个 `crop_waste` 会造死物品。

**决定**：

- **只有实际产生叶/茎/藤/荚/皮渣的作物才有 `crop_waste/<crop>`**：
  - 叶菜、根菜、豆类、茄果瓜类、香草、香料、草莓、部分水生作物；
- **没有 crop_waste 的作物**：
  - 谷物 → `grain_bundle`/`wet_grass`/`tfc:straw`；
  - 油料 → `oil_cake`/`stalk`；
  - 纤维 → `shives`/`fiber_residue`；
  - 坚果 → `nut_shell`；
  - 蘑菇 → `spent_substrate`；
- `crop_waste` 数量约 **102**（A 64 + TFC 18 + B 香料 20），不是 159；
- 每个有 crop_waste 的作物单独定 high/medium/low；
- 没有实际的作物不造物品，表里写“无”。

### 13. TFC 10 灌木

**决定**：

- **替换采收/再生流程 + 资源覆盖**；
- 不做育苗/移栽/农艺；
- 草莓已由 A 迁移为普通作物，不列入；
- 不误伤 A 的 TFC 标签/世界生成。

## 最终建议

先做 **A 10 + TFC 6 谷物 bundle→wet_grass、102 个实际 crop_waste、TFC 29 种植/收获覆盖、TFC 10 灌木采收/再生覆盖**；湿草用 B 新物品 `wet_grass`，坚果用 `nut_state` 叶状态，蘑菇全部世界生成、自然专用 4 种禁止菌包。这样同时满足“加工关联”“具体作物具体实现”“不绕过 TFC”三个约束。
