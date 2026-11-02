# 291 作物系统完整修改文档（整合稿 v2）
> 日期：2026-10-28
> 性质：**计划/修改规格**，不是实现。**本轮未推送、未提交远程。**
> 整合：`287` 要求、`288` 生产/培育链、`289` 116 条作物矩阵、`290` 流程/产量平衡；并新增 B 香料、坚果、蘑菇。

## 目录
- [1. 范围与统计](#1-范围与统计)
- [2. 当前状态与前置问题](#2-当前状态与前置问题)
- [3. 设计原则](#3-设计原则)
- [4. 生产链](#4-生产链)
- [5. 培育链与种子处理](#5-培育链与种子处理)
- [6. 流程 profile 与产量平衡](#6-流程-profile-与产量平衡)
- [7. A 87 作物矩阵](#7-a-87-作物矩阵)
- [8. TFC 29 作物矩阵](#8-tfc-29-作物矩阵)
- [9. B 新增农作物/栽培物](#9-b-新增农作物栽培物)
- [10. TFC 10 灌木](#10-tfc-10-灌木)
- [11. 修改范围清单](#11-修改范围清单)
- [12. 实施批次与验收](#12-实施批次与验收)
- [13. 未决问题](#13-未决问题)
- [14. 来源文档](#14-来源文档)

## 1. 范围与统计
| 类别 | 数量 | 说明 |
|---|---:|---|
| A 作物 | 87 | 以 `crops-manifest.json` 为准；旧文档常写 86 |
| TFC 作物 | 29 | TFC 原版 `crop/*` |
| TFC 灌木 | 10 | 草莓已经是 A 普通作物（A 也移除了 TFC 草莓灌木的世界生成），不再作为 B 的灌木重做目标 |
| 已有作物记录合计 | 116 | A 87 + TFC 29 |
| B 新增香料作物 | 20 | basil · bay_laurel · cardamom · cilantro · cumin · oregano · pimento · vanilla · black_pepper · cinnamon · clove · nutmeg · saffron · star_anise · rosemary · thyme · sage · dill · fennel · mustard |
| B 新增坚果 | 8 | acorn · chestnut · pistachio · cashew · macadamia · pine_nut · hickory_nut · beechnut；另有 A/AFC 已有 6 种坚果 |
| B 新增蘑菇 | 15 | oyster · shiitake · button · enoki · wood_ear · reishi · lions_mane · maitake · king_oyster · shimeji · porcini · morel · chanterelle · black_truffle · turkey_tail |
| B 新增记录合计 | 43 | 20 香料 + 8 坚果 + 15 蘑菇；蘑菇是栽培物，不是普通作物 |
| 副产物物品 | 1 + 16 + 102 | `tfcagricultureplus:wet_grass`（1，B 新物品）+ `grain_bundle/<crop>`（16，A 10 + TFC 6）+ `crop_waste/<crop>`（102，按实际副产）；坚果壳/菌渣另算 |
| 全部作物/栽培记录 | 159 | 116 已有 + 43 B 新增 |

> 统计口径：A 87 与 TFC 29 是已有内容；20 香料是 Firmalife 搁置项接管/重建，8 坚果是 B 新物品/树产 + 已有树叶状态，15 蘑菇含野生生成/刷新与可栽培 11/自然专用 4。

## 2. 当前状态与前置问题
### 2.1 当前状态
- B 没有作物生产/培育链，也没有 116 条作物映射；
- A 已有 87 种作物与食物/种子资源；A 还覆盖 6 个 TFC cabbage 模型；
- TFC 29 作物仍是原版十字模型与统一 6–10 掉落；**本次要求替换/覆盖其种植与收获流程，不再做资源旁路。**
- TFC 10 灌木仍在 TFC 灌木管线，本次替换采收/再生；草莓已经是 A 普通作物，TFC 草莓灌木被 A 关闭世界生成/隐藏；
- B 已有 `in_world`、案板、研钵、干燥架、炒锅，但没有育苗盘、移栽、种子处理、农艺操作；
- 香料、坚果、蘑菇三项此前搁置，当前完成度 0。
### 2.2 前置问题
1. **A/B 资源所有权**：A 持有 6 个 `assets/tfc/models/block/crop/cabbage_age_*.json`；B 的 TFC 29 覆盖会与 A 同路径冲突。
2. **TFC EUPL 授权链**：TFC 资源覆盖属于派生风险，EUPL 通知/许可证/来源登记未完成。
3. **范围未统一**：A 87、TFC 29、TFC 10 灌木、B 43 新增，四套范围的生产/培育链覆盖口径必须先定。

## 3. 设计原则
1. **每一作物都必须闭环**：主产品、副产品、繁殖、育苗/种子处理、初步加工、出口。
2. **不做纯资源重做**：六环节/九工序必须落的方块、物品、BE、`in_world`、DataComponent 上。
3. **产量按产率平衡**：TFC 29 与 A 87 的 raw **允许被 B 覆盖**；用 bundle/湿草/新叶状态替换原流程，旧值只作回退基线；TFC 不再绕过。
4. **不新增无用途产物**：新副产物必须有饲料/堆肥/纸/燃料/油/药等出口。
5. **不使用统一模板覆盖所有作物**：至少 27 个流程 profile，并逐作物填写关键工序。
6. **兼容优先**：TFC 存档、A 独立可卸载、TFC EUPL 义务必须先满足。

## 4. 生产链
| 族 | 数量 | 主链 |
|---|---:|---|
| A 叶菜/茎菜 | 21 | 切/撕→盐渍→乳酸发酵→晒干 |
| A 根/块茎/鳞茎 | 17 | 清洗→去皮→切片→晒干/磨粉/沉淀淀粉；木薯/芋头/山药先去毒 |
| A 谷物/禾本 | 12 | 脱粒→扬场→磨粉；麦类制麦芽、稻类碾米 |
| A 豆类 | 9 | 干燥→脱荚→浸泡→磨浆/煮制/发酵 |
| A 油料 | 4 | 清理→炒/烘→磨→蒸→制饼→压榨 |
| A 纤维 | 4 | 沤麻→打麻→梳麻→纺线/织布 |
| A 茄果/瓜类 | 10 | 取籽/切片→晒干/磨粉/腌渍/熬酱；丝瓜取络、葫芦做容器 |
| A 香草/香料 | 1 | 采叶/花→干燥→研磨→过筛 |
| A 特用 | 5 | 五物种五条不同链 |
| A 水生/其他 | 3 | 采割→脱粒/晒干/剥壳；纤维类沤制 |
| A 浆果特例 | 1 | 草莓匍匐茎苗→果酱/果干 |
| TFC 谷物 | 7 | 脱粒→扬场→磨粉/碾米/麦芽 |
| TFC 根/块茎/鳞茎 | 7 | 清洗→去皮→切片→晒干/磨粉/淀粉 |
| TFC 豆类/油料 | 5 | 干燥→脱荚/清理→浸泡/压榨/磨浆 |
| TFC 叶菜/饲草 | 2 | 盐渍/发酵/晒干；饲草晒干打捆 |
| TFC 茄果/瓜类 | 6 | 鲜食/晒干/磨粉/熬酱；瓜籽/果肉分开 |
| TFC 纤维 | 1 | 沤麻→打麻→梳麻→纺线 |
| TFC 水生/纤维 | 1 | 割茎→沤制/剥皮→压片/打麻 |
| B 香料 | 20 | 采叶/种子/果荚→干燥→研磨→过筛 |
| B 坚果 | 8 | 落果/采收→去壳→干燥→烤/磨粉/榨油 |
| B 蘑菇 | 15 | 菌包/菌根接种→走菌→出菇→采→干燥/鲜食/药用 |

生产链硬约束：每物种主产品+副产品；每产物至少一个加工/使用出口；原有掉落不减少；未成熟破坏补偿；禁止死端。

### 4.1 副产物出口：潮湿草与废枝叶
这两项是**收获/破坏方块时一次产出的副产物**，不是新的作物物种。
#### 4.1.1 潮湿草 `wet_grass`：B 新物品
| 项 | 设计 |
|---|---|
| 物品 | **`tfcagricultureplus:wet_grass`** —— B 新增物品，**不是 TFC 已有物品**；需模型/贴图/语言/标签 |
| 来源 1 | **A 10 + TFC 6 长秆谷物**成熟收获 → `grain_bundle/<crop>` → 脱粒 → 谷粒 + `wet_grass`；这是主路径（见 4.1.3） |
| 来源 2 | 13 种 TFC 野生草（beachgrass · bluegrass · bromegrass · fountain_grass · orchard_grass · pampas_grass · raddia_grass · red_oat_grass · ryegrass · scutch_grass · switchgrass · tall_fescue_grass · timothy_grass）在非干枯状态被收割 |
| 来源 3 | 未成熟作物被破坏时通过 `tfc:extra_products` 补偿产出 |
| 干燥 | `tfcagricultureplus:wet_grass` → **TFC `tfc:straw`（干草/秸秆）**，走晒架/Firmalife drying mat 或 TFC heating；1:1 干燥 |
| 用途 | 饲料、绿色堆肥 `tfc:compost_greens/*`、晒干后编织/燃料/青贮 |
| 平衡 | 每次收割 1–2 份湿草；晒干 1:1；不减少原有剪刀掉落；干枯草（`dry_grass` 等）直接走 `tfc:straw`，不产湿草 |
| 兼容 | 野草掉落表 `replace=false`，保留剪刀→植物方块；湿草是新增分支，不删除 TFC 的 straw 用途链 |
#### 4.1.2 废枝叶：不是所有作物都有，按实际加工判定
“废枝叶”只是统称，**不是每个作物都产**。只有实际加工步骤产生外叶/茎/藤/荚/皮渣的作物才有 `crop_waste/<crop>`；没有该副产的作物不造物品，走各自副产（straw / oil cake / shives / shell / spent substrate）。
| 作物 | 来源/组 | 废枝叶物品 | 类型 | 堆肥档 | 其它出口 |
|---|---|---|---|---|---|
| `spinach` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/spinach` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |
| `lettuce` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/lettuce` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |
| `celery` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/celery` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |
| `kale` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/kale` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |
| `napa_cabbage` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/napa_cabbage` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |
| `cabbage` | TFC·叶菜/饲草 | `tfcagricultureplus:crop_waste/cabbage` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |
| `mustard_greens` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/mustard_greens` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |
| `broccoli` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/broccoli` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |
| `cauliflower` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/cauliflower` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |
| `brussels_sprouts` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/brussels_sprouts` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |
| `swiss_chard` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/swiss_chard` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |
| `celtuce` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/celtuce` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |
| `garland_chrysanthemum` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/garland_chrysanthemum` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |
| `perilla` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/perilla` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |
| `arugula` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/arugula` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |
| `turnip` | A·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/turnip` | 茎叶/皮渣 | `tfc:compost_greens/medium` | 饲料/堆肥；嫩叶可食用 |
| `parsnip` | A·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/parsnip` | 茎叶/皮渣 | `tfc:compost_greens/medium` | 饲料/堆肥；嫩叶可食用 |
| `sunchoke` | A·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/sunchoke` | 茎叶/皮渣 | `tfc:compost_greens/medium` | 饲料/堆肥；嫩叶可食用 |
| `shallot` | A·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/shallot` | 茎叶/皮渣 | `tfc:compost_greens/medium` | 饲料/堆肥；嫩叶可食用 |
| `celeriac` | A·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/celeriac` | 茎叶/皮渣 | `tfc:compost_greens/medium` | 饲料/堆肥；嫩叶可食用 |
| `salsify` | A·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/salsify` | 茎叶/皮渣 | `tfc:compost_greens/medium` | 饲料/堆肥；嫩叶可食用 |
| `ginger` | A·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/ginger` | 茎叶/皮渣 | `tfc:compost_greens/medium` | 饲料/堆肥；嫩叶可食用 |
| `turmeric` | A·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/turmeric` | 茎叶/皮渣 | `tfc:compost_greens/medium` | 饲料/堆肥；嫩叶可食用 |
| `yacon` | A·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/yacon` | 茎叶/皮渣 | `tfc:compost_greens/medium` | 饲料/堆肥；嫩叶可食用 |
| `chicory_root` | A·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/chicory_root` | 茎叶/皮渣 | `tfc:compost_greens/medium` | 饲料/堆肥；嫩叶可食用 |
| `chickpea` | A·豆类 | `tfcagricultureplus:crop_waste/chickpea` | 藤蔓/豆荚 | `tfc:compost_greens/high` | 饲料/堆肥；部分可扦插 |
| `faba_bean` | A·豆类 | `tfcagricultureplus:crop_waste/faba_bean` | 藤蔓/豆荚 | `tfc:compost_greens/high` | 饲料/堆肥；部分可扦插 |
| `lupin` | A·豆类 | `tfcagricultureplus:crop_waste/lupin` | 藤蔓/豆荚 | `tfc:compost_greens/high` | 饲料/堆肥；部分可扦插 |
| `adzuki` | A·豆类 | `tfcagricultureplus:crop_waste/adzuki` | 藤蔓/豆荚 | `tfc:compost_greens/high` | 饲料/堆肥；部分可扦插 |
| `bambara_nut` | A·特用 | `tfcagricultureplus:crop_waste/bambara_nut` | 茎叶/残渣 | `tfc:compost_greens/medium` | 按物种；饲料/纤维/堆肥 |
| `fenugreek` | A·特用 | `tfcagricultureplus:crop_waste/fenugreek` | 茎叶/残渣 | `tfc:compost_greens/medium` | 按物种；饲料/纤维/堆肥 |
| `chili` | A·茄果/瓜类 | `tfcagricultureplus:crop_waste/chili` | 老叶/茎藤/瓜瓤 | `tfc:compost_greens/medium` | 饲料/堆肥；纤维/容器另计 |
| `eggplant` | A·茄果/瓜类 | `tfcagricultureplus:crop_waste/eggplant` | 老叶/茎藤/瓜瓤 | `tfc:compost_greens/medium` | 饲料/堆肥；纤维/容器另计 |
| `okra` | A·茄果/瓜类 | `tfcagricultureplus:crop_waste/okra` | 老叶/茎藤/瓜瓤 | `tfc:compost_greens/medium` | 饲料/堆肥；纤维/容器另计 |
| `asparagus` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/asparagus` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |
| `chive` | A·香草/香料 | `tfcagricultureplus:crop_waste/chive` | 茎叶残渣 | `tfc:compost_greens/medium` | 堆肥/饲料 |
| `rhubarb` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/rhubarb` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |
| `artichoke` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/artichoke` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |
| `taro` | A·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/taro` | 叶/皮渣 | `tfc:compost_greens/low` | 必须煮熟去毒后才可饲料/堆肥 |
| `water_chestnut` | A·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/water_chestnut` | 茎叶/皮渣 | `tfc:compost_greens/medium` | 饲料/堆肥；嫩叶可食用 |
| `water_caltrop` | A·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/water_caltrop` | 茎叶/皮渣 | `tfc:compost_greens/medium` | 饲料/堆肥；嫩叶可食用 |
| `lotus` | A·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/lotus` | 茎叶/皮渣 | `tfc:compost_greens/medium` | 饲料/堆肥；嫩叶可食用 |
| `water_dropwort` | A·水生/其他 | `tfcagricultureplus:crop_waste/water_dropwort` | 叶/茎残渣 | `tfc:compost_greens/medium` | 饲料/堆肥；纤维另计 |
| `water_spinach` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/water_spinach` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |
| `arrowhead` | A·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/arrowhead` | 茎叶/皮渣 | `tfc:compost_greens/medium` | 饲料/堆肥；嫩叶可食用 |
| `gorgon_nut` | A·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/gorgon_nut` | 茎叶/皮渣 | `tfc:compost_greens/medium` | 饲料/堆肥；嫩叶可食用 |
| `winter_melon` | A·茄果/瓜类 | `tfcagricultureplus:crop_waste/winter_melon` | 藤叶/瓜瓤 | `tfc:compost_greens/medium` | 饲料/堆肥 |
| `hops` | A·特用 | `tfcagricultureplus:crop_waste/hops` | 茎叶/残渣 | `tfc:compost_greens/medium` | 按物种；饲料/纤维/堆肥 |
| `loofah` | A·茄果/瓜类 | `tfcagricultureplus:crop_waste/loofah` | 藤叶/果渣 | `tfc:compost_greens/medium` | 堆肥；纤维另计 |
| `bitter_melon` | A·茄果/瓜类 | `tfcagricultureplus:crop_waste/bitter_melon` | 老叶/茎藤/瓜瓤 | `tfc:compost_greens/medium` | 饲料/堆肥；纤维/容器另计 |
| `snake_gourd` | A·茄果/瓜类 | `tfcagricultureplus:crop_waste/snake_gourd` | 老叶/茎藤/瓜瓤 | `tfc:compost_greens/medium` | 饲料/堆肥；纤维/容器另计 |
| `yam` | A·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/yam` | 叶/皮渣 | `tfc:compost_greens/low` | 去毒后饲料/堆肥 |
| `malabar_spinach` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/malabar_spinach` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |
| `chayote` | A·茄果/瓜类 | `tfcagricultureplus:crop_waste/chayote` | 老叶/茎藤/瓜瓤 | `tfc:compost_greens/medium` | 饲料/堆肥；纤维/容器另计 |
| `bottle_gourd` | A·茄果/瓜类 | `tfcagricultureplus:crop_waste/bottle_gourd` | 藤叶/果壳 | `tfc:compost_greens/medium` | 堆肥；容器另计 |
| `cantaloupe` | A·茄果/瓜类 | `tfcagricultureplus:crop_waste/cantaloupe` | 藤叶/瓜瓤 | `tfc:compost_greens/medium` | 饲料/堆肥 |
| `water_shield` | A·水生/其他 | `tfcagricultureplus:crop_waste/water_shield` | 叶/茎残渣 | `tfc:compost_greens/medium` | 饲料/堆肥；纤维另计 |
| `cardoon` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/cardoon` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |
| `purslane` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/purslane` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |
| `pea` | A·豆类 | `tfcagricultureplus:crop_waste/pea` | 藤蔓/豆荚 | `tfc:compost_greens/high` | 饲料/堆肥；部分可扦插 |
| `cowpea` | A·豆类 | `tfcagricultureplus:crop_waste/cowpea` | 藤蔓/豆荚 | `tfc:compost_greens/high` | 饲料/堆肥；部分可扦插 |
| `common_bean` | A·豆类 | `tfcagricultureplus:crop_waste/common_bean` | 藤蔓/豆荚 | `tfc:compost_greens/high` | 饲料/堆肥；部分可扦插 |
| `winged_bean` | A·豆类 | `tfcagricultureplus:crop_waste/winged_bean` | 藤蔓/豆荚 | `tfc:compost_greens/high` | 饲料/堆肥；部分可扦插 |
| `pigeon_pea` | A·豆类 | `tfcagricultureplus:crop_waste/pigeon_pea` | 藤蔓/豆荚 | `tfc:compost_greens/high` | 饲料/堆肥；部分可扦插 |
| `strawberry` | A·浆果特例 | `tfcagricultureplus:crop_waste/strawberry` | 老叶/匍匐茎残段 | `tfc:compost_greens/high` | 堆肥/饲料 |
| `beet` | TFC·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/beet` | 茎叶/皮渣 | `tfc:compost_greens/medium` | 饲料/堆肥；嫩叶可食用 |
| `carrot` | TFC·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/carrot` | 茎叶/皮渣 | `tfc:compost_greens/medium` | 饲料/堆肥；嫩叶可食用 |
| `cassava` | TFC·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/cassava` | 叶/皮渣 | `tfc:compost_greens/low` | 去毒后饲料/堆肥 |
| `garlic` | TFC·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/garlic` | 茎叶/皮渣 | `tfc:compost_greens/medium` | 饲料/堆肥；嫩叶可食用 |
| `green_bean` | TFC·豆类/油料 | `tfcagricultureplus:crop_waste/green_bean` | 藤蔓/豆荚 | `tfc:compost_greens/high` | 饲料/堆肥 |
| `lentil` | TFC·豆类/油料 | `tfcagricultureplus:crop_waste/lentil` | 藤蔓/豆荚 | `tfc:compost_greens/high` | 饲料/堆肥 |
| `melon` | TFC·茄果/瓜类 | `tfcagricultureplus:crop_waste/melon` | 藤叶/瓜瓤 | `tfc:compost_greens/medium` | 饲料/堆肥 |
| `onion` | TFC·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/onion` | 茎叶/皮渣 | `tfc:compost_greens/medium` | 饲料/堆肥；嫩叶可食用 |
| `peanut` | TFC·豆类/油料 | `tfcagricultureplus:crop_waste/peanut` | 藤蔓/豆荚 | `tfc:compost_greens/high` | 饲料/堆肥 |
| `potato` | TFC·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/potato` | 茎叶/皮渣 | `tfc:compost_greens/medium` | 饲料/堆肥；嫩叶可食用 |
| `pumpkin` | TFC·茄果/瓜类 | `tfcagricultureplus:crop_waste/pumpkin` | 藤叶/瓜瓤 | `tfc:compost_greens/medium` | 饲料/堆肥 |
| `radish` | TFC·根/块茎/鳞茎 | `tfcagricultureplus:crop_waste/radish` | 茎叶/皮渣 | `tfc:compost_greens/medium` | 饲料/堆肥；嫩叶可食用 |
| `red_bell_pepper` | TFC·茄果/瓜类 | `tfcagricultureplus:crop_waste/red_bell_pepper` | 老叶/茎藤/瓜瓤 | `tfc:compost_greens/medium` | 饲料/堆肥；纤维/容器另计 |
| `soybean` | TFC·豆类/油料 | `tfcagricultureplus:crop_waste/soybean` | 藤蔓/豆荚 | `tfc:compost_greens/high` | 饲料/堆肥 |
| `squash` | TFC·茄果/瓜类 | `tfcagricultureplus:crop_waste/squash` | 藤叶/瓜瓤 | `tfc:compost_greens/medium` | 饲料/堆肥 |
| `tomato` | TFC·茄果/瓜类 | `tfcagricultureplus:crop_waste/tomato` | 老叶/茎藤/瓜瓤 | `tfc:compost_greens/medium` | 饲料/堆肥；纤维/容器另计 |
| `yellow_bell_pepper` | TFC·茄果/瓜类 | `tfcagricultureplus:crop_waste/yellow_bell_pepper` | 老叶/茎藤/瓜瓤 | `tfc:compost_greens/medium` | 饲料/堆肥；纤维/容器另计 |

**不产 crop_waste 的 A/TFC 作物**（共 34 条）：
- A 谷物 12、A 油料 4、A 纤维 4、`agave`、`jobs_tears`、`wild_rice_stem`；
- TFC 谷物 7、`jute`、`papyrus`、`alfalfa`、`canola`；
- 这些作物的副产是：谷物 bundle/wet_grass/straw、油料 stalk/oil cake、纤维 shives、坚果 shell、蘑菇 spent substrate。

**B 新增 43 条的废料**：香料 20 条有 `crop_waste/<spice>`（计入 102）；坚果 8 条只有 `nut_shell`；蘑菇 15 条只有 `spent_substrate`，二者都不算绿色废枝叶。因此 **crop_waste 总数 = 82（A/TFC）+ 20（B 香料）= 102**，不是 159。

**没有实际废枝叶的作物不设物品**；`crop_waste` 不得成为“每作物一个死物品”的指标。

#### 4.1.3 谷物捆：湿草的加工来源

不是所有谷物都直接掉散粒：**A 10 + TFC 6 长秆谷物先收谷物捆，再脱粒**，脱粒副产才是湿草。

| 作物 | 来源 | 谷物捆物品 | 收获 | 脱粒 | 湿草/干燥 | 备注 |
|---|---|---|---|---|---|---|
| `millet` | A | `tfcagricultureplus:grain_bundle/millet` | 成熟收获 → 1–2 捆 + 种子 | 脱粒 → 谷粒 + 1–2 `tfcagricultureplus:wet_grass` | 1:1 晒干 → `tfc:straw` | 覆盖 A 原收获 |
| `foxtail_millet` | A | `tfcagricultureplus:grain_bundle/foxtail_millet` | 成熟收获 → 1–2 捆 + 种子 | 脱粒 → 谷粒 + 1–2 `tfcagricultureplus:wet_grass` | 1:1 晒干 → `tfc:straw` | 覆盖 A 原收获 |
| `fonio` | A | `tfcagricultureplus:grain_bundle/fonio` | 成熟收获 → 1–2 捆 + 种子 | 脱粒 → 谷粒 + 1–2 `tfcagricultureplus:wet_grass` | 1:1 晒干 → `tfc:straw` | 覆盖 A 原收获 |
| `spelt` | A | `tfcagricultureplus:grain_bundle/spelt` | 成熟收获 → 1–2 捆 + 种子 | 脱粒 → 谷粒 + 1–2 `tfcagricultureplus:wet_grass` | 1:1 晒干 → `tfc:straw` | 覆盖 A 原收获 |
| `emmer` | A | `tfcagricultureplus:grain_bundle/emmer` | 成熟收获 → 1–2 捆 + 种子 | 脱粒 → 谷粒 + 1–2 `tfcagricultureplus:wet_grass` | 1:1 晒干 → `tfc:straw` | 覆盖 A 原收获 |
| `einkorn` | A | `tfcagricultureplus:grain_bundle/einkorn` | 成熟收获 → 1–2 捆 + 种子 | 脱粒 → 谷粒 + 1–2 `tfcagricultureplus:wet_grass` | 1:1 晒干 → `tfc:straw` | 覆盖 A 原收获 |
| `pearl_millet` | A | `tfcagricultureplus:grain_bundle/pearl_millet` | 成熟收获 → 1–2 捆 + 种子 | 脱粒 → 谷粒 + 1–2 `tfcagricultureplus:wet_grass` | 1:1 晒干 → `tfc:straw` | 覆盖 A 原收获 |
| `finger_millet` | A | `tfcagricultureplus:grain_bundle/finger_millet` | 成熟收获 → 1–2 捆 + 种子 | 脱粒 → 谷粒 + 1–2 `tfcagricultureplus:wet_grass` | 1:1 晒干 → `tfc:straw` | 覆盖 A 原收获 |
| `sorghum` | A | `tfcagricultureplus:grain_bundle/sorghum` | 成熟收获 → 1–2 捆 + 种子 | 脱粒 → 谷粒 + 1–2 `tfcagricultureplus:wet_grass` | 1:1 晒干 → `tfc:straw` | 覆盖 A 原收获 |
| `jobs_tears` | A | `tfcagricultureplus:grain_bundle/jobs_tears` | 成熟收获 → 1–2 捆 + 种子 | 脱粒 → 谷粒 + 1–2 `tfcagricultureplus:wet_grass` | 1:1 晒干 → `tfc:straw` | 覆盖 A 原收获 |
| `barley` | TFC | `tfcagricultureplus:grain_bundle/barley` | 成熟收获 → 1–2 捆 + 种子 | 脱粒 → 谷粒 + 1–2 `tfcagricultureplus:wet_grass` | 1:1 晒干 → `tfc:straw` | 覆盖 TFC 原收获 |
| `oat` | TFC | `tfcagricultureplus:grain_bundle/oat` | 成熟收获 → 1–2 捆 + 种子 | 脱粒 → 谷粒 + 1–2 `tfcagricultureplus:wet_grass` | 1:1 晒干 → `tfc:straw` | 覆盖 TFC 原收获 |
| `rice` | TFC | `tfcagricultureplus:grain_bundle/rice` | 成熟收获 → 1–2 捆 + 种子 | 脱粒 → 谷粒 + 1–2 `tfcagricultureplus:wet_grass` | 1:1 晒干 → `tfc:straw` | 覆盖 TFC 原收获 |
| `rye` | TFC | `tfcagricultureplus:grain_bundle/rye` | 成熟收获 → 1–2 捆 + 种子 | 脱粒 → 谷粒 + 1–2 `tfcagricultureplus:wet_grass` | 1:1 晒干 → `tfc:straw` | 覆盖 TFC 原收获 |
| `wheat` | TFC | `tfcagricultureplus:grain_bundle/wheat` | 成熟收获 → 1–2 捆 + 种子 | 脱粒 → 谷粒 + 1–2 `tfcagricultureplus:wet_grass` | 1:1 晒干 → `tfc:straw` | 覆盖 TFC 原收获 |
| `maize` | TFC | `tfcagricultureplus:grain_bundle/maize` | 成熟收获 → 1–2 捆 + 种子 | 脱粒 → 谷粒 + 1–2 `tfcagricultureplus:wet_grass` | 1:1 晒干 → `tfc:straw` | 覆盖 TFC 原收获 |

TFC 6 种（barley/oat/rice/rye/wheat/maize）**同样走 bundle→脱粒→wet_grass**，覆盖 TFC 原有直接掉谷粒/秸秆的收获流程。

非谷物捆：`buckwheat` / `amaranth` / `quinoa`；TFC `sugarcane` 不属于谷物捆。

#### 4.1.4 废枝叶/菌渣/坚果壳的边界
- 坚果壳：不是“绿色废枝叶”，单独走 `nut_shell/<nut>` → `tfc:compost_browns/high` / 燃料；
- 蘑菇废菌包：`spent_substrate` → `tfc:compost_browns/medium` / 堆肥，不算绿色枝叶；
- 香料废枝叶：`crop_waste/<spice>` → 按 `compost_greens/high|medium`；
- 所有 `crop_waste` / 壳 / 菌渣必须有堆肥/饲料/燃料/纸至少一个出口，不得造死物品。

## 5. 培育链与种子处理
### 5.1 种植侧六环节
1. 留种/采种：有性种子 + 无性块茎/鳞茎/根茎/扦插/分株/匍匐茎；母株性状用 DataComponent。
2. 育苗：育苗盘/苗床方块 + BE，温湿度影响成活。
3. 移栽：`in_world` 手持苗右键耕地，校验土壤/气候，缓苗期。
4. 生长管理：间苗、培土、搭架、打顶、除草、施肥。
5. 收获：主产品+次产品；未成熟破坏补偿 **`wet_grass` 潮湿草**；废枝叶只有实际产出的作物才有 **`crop_waste/<crop>`**；A 10 + TFC 6 谷物按 4.1.3 先出谷物捆，脱粒产 `wet_grass`。
6. 留种循环：成熟株留种/扦插闭环。
### 5.2 加工侧九工序
采种→种子干燥→选种/筛种→浸种→催芽→拌种→扦插/分株→育苗→移栽。

**关键价值**：浸种/催芽缩短生长时间；无性繁殖保留母株性状。

## 6. 流程 profile 与产量平衡
### 6.1 现有产率基线
- A/TFC 普通作物：主产品 `0–(6–10)`，种子通常 1（部分 1–2）；
- 红/黄甜椒：`4–5 ×2`；
- melon/pumpkin：走果实方块掉落，不在 6–10 作物池；
- 当前普通作物没有按物种区分产率。
### 6.2 约束
``text
seedBack >= 1
processed <= raw
processed >= 1
byproduct >= 1
``
- **TFC 29 raw 由 B 覆盖**（bundle/湿草/新叶状态）；A 87 raw 同样可调；旧值只作回退基线；
- 平衡优先通过加工转化率、副产物比例、种子返还实现；
- 20 次收获均值/区间验收。
### 6.3 流程 profile
27 个 profile：`leaf-preserve`、`root-starch`、`root-detox`、`root-spice`、`grain-mill`、`grain-rice`、`grain-malt`、`legume-dry`、`legume-oil`、`oil-press`、`fiber-bast`、`fiber-oil`、`fiber-syrup`、`fiber-water`、`fruit-preserve`、`fruit-seed`、`fruit-fiber`、`fruit-container`、`fruit-spice`、`fruit-paste`、`herb-dry`、`water-grain`、`berry-runner`、`leaf-forage`、`sugar`、`special-brew`、`special-triple`。

## 7. A 87 作物矩阵
| # | 作物 | 来源/组 | 主产品 | 副产品 | 繁殖 | 育苗/种子处理 | 初步加工 | 流程 | 产率计划（现/目标/seed/加工/副） | 定制关键步骤 | 出口 | 批次 |
|---:|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `spinach` | A·叶菜/茎菜 | 食用叶/叶球/茎（`tfcfarmingplus:food/spinach`）；水生叶菜按 A 现有产物 | 种子 + 外叶/叶柄/修整料 → 堆肥、饲料；纤维类副产（cardoon/artichoke） | 种子直播/育苗移栽；artichoke/cardoon/rhubarb/asparagus 用分株/冠芽 | 种子：采种→晒干→筛选→浸种/催芽→育苗盘→移栽；分株：母株→分株→育苗→定植 | 清洗→切/撕→盐渍→乳酸发酵→晒干；叶球类可切丝盐渍 | `leaf-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:8–12 叶<br>seed:1<br>加工:2–4 份干菜/腌菜<br>副:2–4 外叶 | 清洗→切/撕→盐渍→乳酸发酵→晒干；叶球类可切丝盐渍 | 沙拉、汤、腌菜、干菜、堆肥/饲料 | P1 |
| 2 | `lettuce` | A·叶菜/茎菜 | 食用叶/叶球/茎（`tfcfarmingplus:food/lettuce`）；水生叶菜按 A 现有产物 | 种子 + 外叶/叶柄/修整料 → 堆肥、饲料；纤维类副产（cardoon/artichoke） | 种子直播/育苗移栽；artichoke/cardoon/rhubarb/asparagus 用分株/冠芽 | 种子：采种→晒干→筛选→浸种/催芽→育苗盘→移栽；分株：母株→分株→育苗→定植 | 清洗→切/撕→盐渍→乳酸发酵→晒干；叶球类可切丝盐渍 | `leaf-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:8–12 叶/球/茎<br>seed:1<br>加工:2–4 份腌/干/切丝<br>副:2–4 外叶/叶柄 → 堆肥/饲料 | 清洗→切/撕→盐渍→乳酸发酵→晒干；叶球类可切丝盐渍 | 沙拉、汤、腌菜、干菜、堆肥/饲料 | P1 |
| 3 | `celery` | A·叶菜/茎菜 | 食用叶/叶球/茎（`tfcfarmingplus:food/celery`）；水生叶菜按 A 现有产物 | 种子 + 外叶/叶柄/修整料 → 堆肥、饲料；纤维类副产（cardoon/artichoke） | 种子直播/育苗移栽；artichoke/cardoon/rhubarb/asparagus 用分株/冠芽 | 种子：采种→晒干→筛选→浸种/催芽→育苗盘→移栽；分株：母株→分株→育苗→定植 | 清洗→切/撕→盐渍→乳酸发酵→晒干；叶球类可切丝盐渍 | `leaf-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:8–12 叶/球/茎<br>seed:1<br>加工:2–4 份腌/干/切丝<br>副:2–4 外叶/叶柄 → 堆肥/饲料 | 清洗→切/撕→盐渍→乳酸发酵→晒干；叶球类可切丝盐渍 | 沙拉、汤、腌菜、干菜、堆肥/饲料 | P1 |
| 4 | `kale` | A·叶菜/茎菜 | 食用叶/叶球/茎（`tfcfarmingplus:food/kale`）；水生叶菜按 A 现有产物 | 种子 + 外叶/叶柄/修整料 → 堆肥、饲料；纤维类副产（cardoon/artichoke） | 种子直播/育苗移栽；artichoke/cardoon/rhubarb/asparagus 用分株/冠芽 | 种子：采种→晒干→筛选→浸种/催芽→育苗盘→移栽；分株：母株→分株→育苗→定植 | 采叶→焯水/盐渍/晒干 | `leaf-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:8–12 叶<br>seed:1<br>加工:2–3 份干菜/腌菜<br>副:2–3 外叶 | 先切分/盐渍，叶球类可发酵：采叶→焯水/盐渍/晒干 | 蔬菜、干菜、腌菜 | P1 |
| 5 | `napa_cabbage` | A·叶菜/茎菜 | 食用叶/叶球/茎（`tfcfarmingplus:food/napa_cabbage`）；水生叶菜按 A 现有产物 | 种子 + 外叶/叶柄/修整料 → 堆肥、饲料；纤维类副产（cardoon/artichoke） | 种子直播/育苗移栽；artichoke/cardoon/rhubarb/asparagus 用分株/冠芽 | 种子：采种→晒干→筛选→浸种/催芽→育苗盘→移栽；分株：母株→分株→育苗→定植 | 切丝→盐渍→乳酸发酵→晒干 | `leaf-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:8–12 叶球<br>seed:1<br>加工:2–4 份酸菜/干菜<br>副:3–4 外叶 | 先切分/盐渍，叶球类可发酵：切丝→盐渍→乳酸发酵→晒干 | 酸菜、泡菜、干菜 | P1 |
| 6 | `mustard_greens` | A·叶菜/茎菜 | 食用叶/叶球/茎（`tfcfarmingplus:food/mustard_greens`）；水生叶菜按 A 现有产物 | 种子 + 外叶/叶柄/修整料 → 堆肥、饲料；纤维类副产（cardoon/artichoke） | 种子直播/育苗移栽；artichoke/cardoon/rhubarb/asparagus 用分株/冠芽 | 种子：采种→晒干→筛选→浸种/催芽→育苗盘→移栽；分株：母株→分株→育苗→定植 | 清洗→切/撕→盐渍→乳酸发酵→晒干；叶球类可切丝盐渍 | `leaf-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:8–12 叶/球/茎<br>seed:1<br>加工:2–4 份腌/干/切丝<br>副:2–4 外叶/叶柄 → 堆肥/饲料 | 清洗→切/撕→盐渍→乳酸发酵→晒干；叶球类可切丝盐渍 | 沙拉、汤、腌菜、干菜、堆肥/饲料 | P1 |
| 7 | `broccoli` | A·叶菜/茎菜 | 食用叶/叶球/茎（`tfcfarmingplus:food/broccoli`）；水生叶菜按 A 现有产物 | 种子 + 外叶/叶柄/修整料 → 堆肥、饲料；纤维类副产（cardoon/artichoke） | 种子直播/育苗移栽；artichoke/cardoon/rhubarb/asparagus 用分株/冠芽 | 种子：采种→晒干→筛选→浸种/催芽→育苗盘→移栽；分株：母株→分株→育苗→定植 | 采花球→焯水/冷冻/晒干 | `leaf-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:8–12 叶/球/茎<br>seed:1<br>加工:2–4 份腌/干/切丝<br>副:2–4 外叶/叶柄 → 堆肥/饲料 | 先切分/盐渍，叶球类可发酵：采花球→焯水/冷冻/晒干 | 蔬菜、干菜 | P1 |
| 8 | `cauliflower` | A·叶菜/茎菜 | 食用叶/叶球/茎（`tfcfarmingplus:food/cauliflower`）；水生叶菜按 A 现有产物 | 种子 + 外叶/叶柄/修整料 → 堆肥、饲料；纤维类副产（cardoon/artichoke） | 种子直播/育苗移栽；artichoke/cardoon/rhubarb/asparagus 用分株/冠芽 | 种子：采种→晒干→筛选→浸种/催芽→育苗盘→移栽；分株：母株→分株→育苗→定植 | 采花球→焯水/腌渍/晒干 | `leaf-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:8–12 叶/球/茎<br>seed:1<br>加工:2–4 份腌/干/切丝<br>副:2–4 外叶/叶柄 → 堆肥/饲料 | 先切分/盐渍，叶球类可发酵：采花球→焯水/腌渍/晒干 | 蔬菜、腌菜 | P1 |
| 9 | `brussels_sprouts` | A·叶菜/茎菜 | 食用叶/叶球/茎（`tfcfarmingplus:food/brussels_sprouts`）；水生叶菜按 A 现有产物 | 种子 + 外叶/叶柄/修整料 → 堆肥、饲料；纤维类副产（cardoon/artichoke） | 种子直播/育苗移栽；artichoke/cardoon/rhubarb/asparagus 用分株/冠芽 | 种子：采种→晒干→筛选→浸种/催芽→育苗盘→移栽；分株：母株→分株→育苗→定植 | 采芽球→焯水/烤/腌渍 | `leaf-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:8–12 叶/球/茎<br>seed:1<br>加工:2–4 份腌/干/切丝<br>副:2–4 外叶/叶柄 → 堆肥/饲料 | 先切分/盐渍，叶球类可发酵：采芽球→焯水/烤/腌渍 | 蔬菜、腌菜 | P1 |
| 10 | `swiss_chard` | A·叶菜/茎菜 | 食用叶/叶球/茎（`tfcfarmingplus:food/swiss_chard`）；水生叶菜按 A 现有产物 | 种子 + 外叶/叶柄/修整料 → 堆肥、饲料；纤维类副产（cardoon/artichoke） | 种子直播/育苗移栽；artichoke/cardoon/rhubarb/asparagus 用分株/冠芽 | 种子：采种→晒干→筛选→浸种/催芽→育苗盘→移栽；分株：母株→分株→育苗→定植 | 清洗→切/撕→盐渍→乳酸发酵→晒干；叶球类可切丝盐渍 | `leaf-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:8–12 叶/球/茎<br>seed:1<br>加工:2–4 份腌/干/切丝<br>副:2–4 外叶/叶柄 → 堆肥/饲料 | 清洗→切/撕→盐渍→乳酸发酵→晒干；叶球类可切丝盐渍 | 沙拉、汤、腌菜、干菜、堆肥/饲料 | P1 |
| 11 | `celtuce` | A·叶菜/茎菜 | 食用叶/叶球/茎（`tfcfarmingplus:food/celtuce`）；水生叶菜按 A 现有产物 | 种子 + 外叶/叶柄/修整料 → 堆肥、饲料；纤维类副产（cardoon/artichoke） | 种子直播/育苗移栽；artichoke/cardoon/rhubarb/asparagus 用分株/冠芽 | 种子：采种→晒干→筛选→浸种/催芽→育苗盘→移栽；分株：母株→分株→育苗→定植 | 清洗→切/撕→盐渍→乳酸发酵→晒干；叶球类可切丝盐渍 | `leaf-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:8–12 叶/球/茎<br>seed:1<br>加工:2–4 份腌/干/切丝<br>副:2–4 外叶/叶柄 → 堆肥/饲料 | 清洗→切/撕→盐渍→乳酸发酵→晒干；叶球类可切丝盐渍 | 沙拉、汤、腌菜、干菜、堆肥/饲料 | P1 |
| 12 | `garland_chrysanthemum` | A·叶菜/茎菜 | 食用叶/叶球/茎（`tfcfarmingplus:food/garland_chrysanthemum`）；水生叶菜按 A 现有产物 | 种子 + 外叶/叶柄/修整料 → 堆肥、饲料；纤维类副产（cardoon/artichoke） | 种子直播/育苗移栽；artichoke/cardoon/rhubarb/asparagus 用分株/冠芽 | 种子：采种→晒干→筛选→浸种/催芽→育苗盘→移栽；分株：母株→分株→育苗→定植 | 清洗→切/撕→盐渍→乳酸发酵→晒干；叶球类可切丝盐渍 | `leaf-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:8–12 叶/球/茎<br>seed:1<br>加工:2–4 份腌/干/切丝<br>副:2–4 外叶/叶柄 → 堆肥/饲料 | 清洗→切/撕→盐渍→乳酸发酵→晒干；叶球类可切丝盐渍 | 沙拉、汤、腌菜、干菜、堆肥/饲料 | P1 |
| 13 | `perilla` | A·叶菜/茎菜 | 食用叶/叶球/茎（`tfcfarmingplus:food/perilla`）；水生叶菜按 A 现有产物 | 种子 + 外叶/叶柄/修整料 → 堆肥、饲料；纤维类副产（cardoon/artichoke） | 种子直播/育苗移栽；artichoke/cardoon/rhubarb/asparagus 用分株/冠芽 | 种子：采种→晒干→筛选→浸种/催芽→育苗盘→移栽；分株：母株→分株→育苗→定植 | 清洗→切/撕→盐渍→乳酸发酵→晒干；叶球类可切丝盐渍 | `leaf-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:8–12 叶/球/茎<br>seed:1<br>加工:2–4 份腌/干/切丝<br>副:2–4 外叶/叶柄 → 堆肥/饲料 | 清洗→切/撕→盐渍→乳酸发酵→晒干；叶球类可切丝盐渍 | 沙拉、汤、腌菜、干菜、堆肥/饲料 | P1 |
| 14 | `arugula` | A·叶菜/茎菜 | 食用叶/叶球/茎（`tfcfarmingplus:food/arugula`）；水生叶菜按 A 现有产物 | 种子 + 外叶/叶柄/修整料 → 堆肥、饲料；纤维类副产（cardoon/artichoke） | 种子直播/育苗移栽；artichoke/cardoon/rhubarb/asparagus 用分株/冠芽 | 种子：采种→晒干→筛选→浸种/催芽→育苗盘→移栽；分株：母株→分株→育苗→定植 | 清洗→切/撕→盐渍→乳酸发酵→晒干；叶球类可切丝盐渍 | `leaf-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:8–12 叶/球/茎<br>seed:1<br>加工:2–4 份腌/干/切丝<br>副:2–4 外叶/叶柄 → 堆肥/饲料 | 清洗→切/撕→盐渍→乳酸发酵→晒干；叶球类可切丝盐渍 | 沙拉、汤、腌菜、干菜、堆肥/饲料 | P1 |
| 15 | `turnip` | A·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfcfarmingplus:food/turnip`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 种子（turnip/parsnip/celeriac/salsify/chicory/radish/carrot/beet）或块茎/鳞茎/根茎（其余） | 种子：采种→晒干→筛选→浸种→直播；块茎/鳞茎：愈伤→分级→直播 | 清洗→去皮→切片→晒干/磨粉/沉淀淀粉；生姜/姜黄走香料链 | `root-starch` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 根/块茎<br>seed:1 个种薯/种球或 1 粒种子<br>加工:1–2 份淀粉/粉/干片<br>副:1–2 皮渣/茎叶 → 饲料/堆肥 | 先去皮/切片，再晒干或沉淀淀粉：清洗→去皮→切片→晒干/磨粉/沉淀淀粉；生姜/姜黄走香料链 | 主食、淀粉、腌菜、干片、饲料、堆肥 | P1 |
| 16 | `parsnip` | A·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfcfarmingplus:food/parsnip`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 种子（turnip/parsnip/celeriac/salsify/chicory/radish/carrot/beet）或块茎/鳞茎/根茎（其余） | 种子：采种→晒干→筛选→浸种→直播；块茎/鳞茎：愈伤→分级→直播 | 清洗→去皮→切片→晒干/磨粉/沉淀淀粉；生姜/姜黄走香料链 | `root-starch` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 根/块茎<br>seed:1 个种薯/种球或 1 粒种子<br>加工:1–2 份淀粉/粉/干片<br>副:1–2 皮渣/茎叶 → 饲料/堆肥 | 先去皮/切片，再晒干或沉淀淀粉：清洗→去皮→切片→晒干/磨粉/沉淀淀粉；生姜/姜黄走香料链 | 主食、淀粉、腌菜、干片、饲料、堆肥 | P1 |
| 17 | `sunchoke` | A·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfcfarmingplus:food/sunchoke`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 块茎 | 种薯→分级→直播 | 清洗→去皮→切片→煮/烤/晒干 | `root-starch` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 根/块茎<br>seed:1 个种薯/种球或 1 粒种子<br>加工:1–2 份淀粉/粉/干片<br>副:1–2 皮渣/茎叶 → 饲料/堆肥 | 先分级/催芽或去壳，再煮/磨粉：清洗→去皮→切片→煮/烤/晒干 | 蔬菜、饲料、菊粉 | P1 |
| 18 | `shallot` | A·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfcfarmingplus:food/shallot`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 种子（turnip/parsnip/celeriac/salsify/chicory/radish/carrot/beet）或块茎/鳞茎/根茎（其余） | 种子：采种→晒干→筛选→浸种→直播；块茎/鳞茎：愈伤→分级→直播 | 清洗→去皮→切片→晒干/磨粉/沉淀淀粉；生姜/姜黄走香料链 | `root-spice` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 个鳞茎<br>seed:1 个种球<br>加工:1–2 份干葱/葱粉<br>副:1 皮/叶 | 先分级/催芽或去壳，再煮/磨粉：清洗→去皮→切片→晒干/磨粉/沉淀淀粉；生姜/姜黄走香料链 | 主食、淀粉、腌菜、干片、饲料、堆肥 | P1 |
| 19 | `celeriac` | A·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfcfarmingplus:food/celeriac`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 种子（turnip/parsnip/celeriac/salsify/chicory/radish/carrot/beet）或块茎/鳞茎/根茎（其余） | 种子：采种→晒干→筛选→浸种→直播；块茎/鳞茎：愈伤→分级→直播 | 清洗→去皮→切片→晒干/磨粉/沉淀淀粉；生姜/姜黄走香料链 | `root-starch` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 根/块茎<br>seed:1 个种薯/种球或 1 粒种子<br>加工:1–2 份淀粉/粉/干片<br>副:1–2 皮渣/茎叶 → 饲料/堆肥 | 先去皮/切片，再晒干或沉淀淀粉：清洗→去皮→切片→晒干/磨粉/沉淀淀粉；生姜/姜黄走香料链 | 主食、淀粉、腌菜、干片、饲料、堆肥 | P1 |
| 20 | `salsify` | A·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfcfarmingplus:food/salsify`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 种子（turnip/parsnip/celeriac/salsify/chicory/radish/carrot/beet）或块茎/鳞茎/根茎（其余） | 种子：采种→晒干→筛选→浸种→直播；块茎/鳞茎：愈伤→分级→直播 | 清洗→去皮→切片→晒干/磨粉/沉淀淀粉；生姜/姜黄走香料链 | `root-starch` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 根/块茎<br>seed:1 个种薯/种球或 1 粒种子<br>加工:1–2 份淀粉/粉/干片<br>副:1–2 皮渣/茎叶 → 饲料/堆肥 | 先去皮/切片，再晒干或沉淀淀粉：清洗→去皮→切片→晒干/磨粉/沉淀淀粉；生姜/姜黄走香料链 | 主食、淀粉、腌菜、干片、饲料、堆肥 | P1 |
| 21 | `ginger` | A·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfcfarmingplus:food/ginger`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 根茎 | 种姜→催芽→切块→定植 | 清洗→去皮→切片→晒干→磨粉 | `root-spice` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–6 根茎<br>seed:1 段种姜/种芋<br>加工:1–2 份干粉/香料<br>副:1 茎叶渣 | 先干燥/蒸煮再磨粉：清洗→去皮→切片→晒干→磨粉 | 香料、姜茶、腌姜 | P1 |
| 22 | `turmeric` | A·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfcfarmingplus:food/turmeric`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 根茎 | 种姜→催芽→切块→定植 | 清洗→煮/蒸→晒干→磨粉 | `root-spice` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–6 根茎<br>seed:1 段种姜/种芋<br>加工:1–2 份干粉/香料<br>副:1 茎叶渣 | 先干燥/蒸煮再磨粉：清洗→煮/蒸→晒干→磨粉 | 香料、染料、咖喱 | P1 |
| 23 | `yacon` | A·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfcfarmingplus:food/yacon`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 块茎/分株 | 种薯→育苗→定植 | 清洗→去皮→切片→晒干/榨汁 | `root-starch` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 根/块茎<br>seed:1 个种薯/种球或 1 粒种子<br>加工:1–2 份淀粉/粉/干片<br>副:1–2 皮渣/茎叶 → 饲料/堆肥 | 先分级/催芽或去壳，再煮/磨粉：清洗→去皮→切片→晒干/榨汁 | 蔬菜、糖浆 | P1 |
| 24 | `chicory_root` | A·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfcfarmingplus:food/chicory_root`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 种子（turnip/parsnip/celeriac/salsify/chicory/radish/carrot/beet）或块茎/鳞茎/根茎（其余） | 种子：采种→晒干→筛选→浸种→直播；块茎/鳞茎：愈伤→分级→直播 | 清洗→去皮→切片→晒干/磨粉/沉淀淀粉；生姜/姜黄走香料链 | `root-starch` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 根/块茎<br>seed:1 个种薯/种球或 1 粒种子<br>加工:1–2 份淀粉/粉/干片<br>副:1–2 皮渣/茎叶 → 饲料/堆肥 | 先去皮/切片，再晒干或沉淀淀粉：清洗→去皮→切片→晒干/磨粉/沉淀淀粉；生姜/姜黄走香料链 | 主食、淀粉、腌菜、干片、饲料、堆肥 | P1 |
| 25 | `millet` | A·谷物/禾本 | 谷物籽粒（`tfcfarmingplus:food/millet`；TFC 用 `tfc:food/millet`） | 秸秆、糠/麸、种子 → 饲料、堆肥、燃料、留种 | 种子 | 采种→晒干→筛选→浸种/催芽（可选）→直播 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | `grain-mill` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 穗/籽粒<br>seed:1–2 粒<br>加工:3–5 份面粉/米/麦芽<br>副:2–4 秸秆/糠麸 → 饲料/燃料/堆肥 | 脱粒→去壳/磨粉；秸秆另收：脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | 面粉/米饭/麦芽/酿酒/饲料/燃料 | P1 |
| 26 | `foxtail_millet` | A·谷物/禾本 | 谷物籽粒（`tfcfarmingplus:food/foxtail_millet`；TFC 用 `tfc:food/foxtail_millet`） | 秸秆、糠/麸、种子 → 饲料、堆肥、燃料、留种 | 种子 | 采种→晒干→筛选→浸种/催芽（可选）→直播 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | `grain-mill` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 穗/籽粒<br>seed:1–2 粒<br>加工:3–5 份面粉/米/麦芽<br>副:2–4 秸秆/糠麸 → 饲料/燃料/堆肥 | 脱粒→去壳/磨粉；秸秆另收：脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | 面粉/米饭/麦芽/酿酒/饲料/燃料 | P1 |
| 27 | `buckwheat` | A·谷物/禾本 | 谷物籽粒（`tfcfarmingplus:food/buckwheat`；TFC 用 `tfc:food/buckwheat`） | 秸秆、糠/麸、种子 → 饲料、堆肥、燃料、留种 | 种子 | 采种→晒干→筛选→浸种/催芽（可选）→直播 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | `grain-mill` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 穗/籽粒<br>seed:1–2 粒<br>加工:3–5 份面粉/米/麦芽<br>副:2–4 秸秆/糠麸 → 饲料/燃料/堆肥 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | 面粉/米饭/麦芽/酿酒/饲料/燃料 | P1 |
| 28 | `fonio` | A·谷物/禾本 | 谷物籽粒（`tfcfarmingplus:food/fonio`；TFC 用 `tfc:food/fonio`） | 秸秆、糠/麸、种子 → 饲料、堆肥、燃料、留种 | 种子 | 采种→晒干→筛选→浸种/催芽（可选）→直播 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | `grain-mill` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 穗/籽粒<br>seed:1–2 粒<br>加工:3–5 份面粉/米/麦芽<br>副:2–4 秸秆/糠麸 → 饲料/燃料/堆肥 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | 面粉/米饭/麦芽/酿酒/饲料/燃料 | P1 |
| 29 | `spelt` | A·谷物/禾本 | 谷物籽粒（`tfcfarmingplus:food/spelt`；TFC 用 `tfc:food/spelt`） | 秸秆、糠/麸、种子 → 饲料、堆肥、燃料、留种 | 种子 | 采种→晒干→筛选→浸种/催芽（可选）→直播 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | `grain-mill` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 穗/籽粒<br>seed:1–2 粒<br>加工:3–5 份面粉/米/麦芽<br>副:2–4 秸秆/糠麸 → 饲料/燃料/堆肥 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | 面粉/米饭/麦芽/酿酒/饲料/燃料 | P1 |
| 30 | `emmer` | A·谷物/禾本 | 谷物籽粒（`tfcfarmingplus:food/emmer`；TFC 用 `tfc:food/emmer`） | 秸秆、糠/麸、种子 → 饲料、堆肥、燃料、留种 | 种子 | 采种→晒干→筛选→浸种/催芽（可选）→直播 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | `grain-mill` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 穗/籽粒<br>seed:1–2 粒<br>加工:3–5 份面粉/米/麦芽<br>副:2–4 秸秆/糠麸 → 饲料/燃料/堆肥 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | 面粉/米饭/麦芽/酿酒/饲料/燃料 | P1 |
| 31 | `einkorn` | A·谷物/禾本 | 谷物籽粒（`tfcfarmingplus:food/einkorn`；TFC 用 `tfc:food/einkorn`） | 秸秆、糠/麸、种子 → 饲料、堆肥、燃料、留种 | 种子 | 采种→晒干→筛选→浸种/催芽（可选）→直播 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | `grain-mill` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 穗/籽粒<br>seed:1–2 粒<br>加工:3–5 份面粉/米/麦芽<br>副:2–4 秸秆/糠麸 → 饲料/燃料/堆肥 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | 面粉/米饭/麦芽/酿酒/饲料/燃料 | P1 |
| 32 | `pearl_millet` | A·谷物/禾本 | 谷物籽粒（`tfcfarmingplus:food/pearl_millet`；TFC 用 `tfc:food/pearl_millet`） | 秸秆、糠/麸、种子 → 饲料、堆肥、燃料、留种 | 种子 | 采种→晒干→筛选→浸种/催芽（可选）→直播 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | `grain-mill` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 穗/籽粒<br>seed:1–2 粒<br>加工:3–5 份面粉/米/麦芽<br>副:2–4 秸秆/糠麸 → 饲料/燃料/堆肥 | 脱粒→去壳/磨粉；秸秆另收：脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | 面粉/米饭/麦芽/酿酒/饲料/燃料 | P1 |
| 33 | `amaranth` | A·谷物/禾本 | 谷物籽粒（`tfcfarmingplus:food/amaranth`；TFC 用 `tfc:food/amaranth`） | 秸秆、糠/麸、种子 → 饲料、堆肥、燃料、留种 | 种子 | 采种→晒干→筛选→浸种/催芽（可选）→直播 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | `grain-mill` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 穗/籽粒<br>seed:1–2 粒<br>加工:3–5 份面粉/米/麦芽<br>副:2–4 秸秆/糠麸 → 饲料/燃料/堆肥 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | 面粉/米饭/麦芽/酿酒/饲料/燃料 | P1 |
| 34 | `quinoa` | A·谷物/禾本 | 谷物籽粒（`tfcfarmingplus:food/quinoa`；TFC 用 `tfc:food/quinoa`） | 秸秆、糠/麸、种子 → 饲料、堆肥、燃料、留种 | 种子 | 采种→晒干→筛选→浸种/催芽（可选）→直播 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | `grain-mill` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 穗/籽粒<br>seed:1–2 粒<br>加工:3–5 份面粉/米/麦芽<br>副:2–4 秸秆/糠麸 → 饲料/燃料/堆肥 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | 面粉/米饭/麦芽/酿酒/饲料/燃料 | P1 |
| 35 | `finger_millet` | A·谷物/禾本 | 谷物籽粒（`tfcfarmingplus:food/finger_millet`；TFC 用 `tfc:food/finger_millet`） | 秸秆、糠/麸、种子 → 饲料、堆肥、燃料、留种 | 种子 | 采种→晒干→筛选→浸种/催芽（可选）→直播 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | `grain-mill` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 穗/籽粒<br>seed:1–2 粒<br>加工:3–5 份面粉/米/麦芽<br>副:2–4 秸秆/糠麸 → 饲料/燃料/堆肥 | 脱粒→去壳/磨粉；秸秆另收：脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | 面粉/米饭/麦芽/酿酒/饲料/燃料 | P1 |
| 36 | `jobs_tears` | A·特用 | 薏米 | 糠/秸秆→饲料 | 种子 | 按物种各自处理；详见行内覆盖 | 脱壳→碾米→煮/磨粉 | `grain-mill` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 穗/籽粒<br>seed:1–2 粒<br>加工:3–5 份面粉/米/麦芽<br>副:2–4 秸秆/糠麸 → 饲料/燃料/堆肥 | 脱壳→碾米→煮/磨粉 | 粮食、药食 | P2/P3 |
| 37 | `chickpea` | A·豆类 | 干豆或鲜荚（`tfcfarmingplus:food/chickpea`；TFC 用 `tfc:food/chickpea`） | 豆荚、秸秆、种子 → 饲料、堆肥、留种 | 种子 | 采种→晒干→筛选→浸种→直播 | 干燥→脱荚→浸泡→磨浆/煮制/发酵 | `legume-dry` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 荚/豆<br>seed:1–2 粒<br>加工:2–4 份干豆/豆粉/豆制品<br>副:1–3 豆荚/秸秆 → 饲料/堆肥 | 先脱荚/浸泡，豆类去毒/磨浆：干燥→脱荚→浸泡→磨浆/煮制/发酵 | 豆制品、豆粉、豆酱、饲料 | P1 |
| 38 | `faba_bean` | A·豆类 | 干豆或鲜荚（`tfcfarmingplus:food/faba_bean`；TFC 用 `tfc:food/faba_bean`） | 豆荚、秸秆、种子 → 饲料、堆肥、留种 | 种子 | 采种→晒干→筛选→浸种→直播 | 干燥→脱荚→浸泡→磨浆/煮制/发酵 | `legume-dry` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 荚/豆<br>seed:1–2 粒<br>加工:2–4 份干豆/豆粉/豆制品<br>副:1–3 豆荚/秸秆 → 饲料/堆肥 | 先脱荚/浸泡，豆类去毒/磨浆：干燥→脱荚→浸泡→磨浆/煮制/发酵 | 豆制品、豆粉、豆酱、饲料 | P1 |
| 39 | `lupin` | A·豆类 | 干豆或鲜荚（`tfcfarmingplus:food/lupin`；TFC 用 `tfc:food/lupin`） | 豆荚、秸秆、种子 → 饲料、堆肥、留种 | 种子 | 采种→晒干→筛选→浸种→直播 | 干燥→脱荚→浸泡→磨浆/煮制/发酵 | `legume-dry` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 荚/豆<br>seed:1–2 粒<br>加工:2–4 份干豆/豆粉/豆制品<br>副:1–3 豆荚/秸秆 → 饲料/堆肥 | 先脱荚/浸泡，豆类去毒/磨浆：干燥→脱荚→浸泡→磨浆/煮制/发酵 | 豆制品、豆粉、豆酱、饲料 | P1 |
| 40 | `adzuki` | A·豆类 | 干豆或鲜荚（`tfcfarmingplus:food/adzuki`；TFC 用 `tfc:food/adzuki`） | 豆荚、秸秆、种子 → 饲料、堆肥、留种 | 种子 | 采种→晒干→筛选→浸种→直播 | 干燥→脱荚→浸泡→磨浆/煮制/发酵 | `legume-dry` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 荚/豆<br>seed:1–2 粒<br>加工:2–4 份干豆/豆粉/豆制品<br>副:1–3 豆荚/秸秆 → 饲料/堆肥 | 先脱荚/浸泡，豆类去毒/磨浆：干燥→脱荚→浸泡→磨浆/煮制/发酵 | 豆制品、豆粉、豆酱、饲料 | P1 |
| 41 | `bambara_nut` | A·特用 | 豆类 | 豆荚/秸秆→饲料 | 种子 | 按物种各自处理；详见行内覆盖 | 干燥→脱荚→煮/磨粉 | `legume-dry` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 荚/豆<br>seed:1–2 粒<br>加工:2–4 份干豆/豆粉/豆制品<br>副:1–3 豆荚/秸秆 → 饲料/堆肥 | 干燥→脱荚→煮/磨粉 | 豆制品、豆粉 | P2/P3 |
| 42 | `fenugreek` | A·特用 | 种子香料 + 叶菜 + 芽菜 | 茎叶→饲料/堆肥 | 种子 | 按物种各自处理；详见行内覆盖 | 种子干燥→磨粉；叶鲜食/晒干；种子发芽 | `special-triple` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–6 株<br>seed:1–2 粒<br>加工:1–2 份香料 + 2–4 份叶菜/芽菜<br>副:1–2 茎叶/种皮 | 种子干燥→磨粉；叶鲜食/晒干；种子发芽 | 香料、蔬菜、芽菜 | P2/P3 |
| 43 | `flax` | A·油料 | 纤维 + 亚麻籽油 | 亚麻籽→油；麻屑→纸/填料 | 种子 | 采种→晒干→筛选→直播 | 沤麻→打麻→梳麻→纺线；种子→压榨 | `fiber-oil` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 茎<br>seed:1–2 粒<br>加工:1–2 份油 + 2–3 份纤维<br>副:1–2 麻屑/油饼 | 纤维与油料双线：沤麻→打麻→梳麻→纺线；种子→压榨 | 布、绳、纸、亚麻油 | P1 |
| 44 | `sesame` | A·油料 | 油籽 → 食用油（`tfcfarmingplus:food/sesame` / 油料产物） | 油饼/粕 → 饲料、肥料；部分纤维/秸秆 | 种子 | 采种→晒干→筛选→直播 | 清理→炒/烘→磨→蒸→制饼→压榨→过滤 | `oil-press` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 单位油籽<br>seed:1–2 粒<br>加工:1–2 份油<br>副:1–2 油饼/粕 → 饲料/肥料 | 清理→炒/烘→磨→蒸→制饼→压榨→过滤 | 食用油、油饼饲料、调味油 | P1 |
| 45 | `safflower` | A·油料 | 油籽 → 食用油（`tfcfarmingplus:food/safflower` / 油料产物） | 油饼/粕 → 饲料、肥料；部分纤维/秸秆 | 种子 | 采种→晒干→筛选→直播 | 清理→炒/烘→磨→蒸→制饼→压榨→过滤 | `oil-press` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 单位油籽<br>seed:1–2 粒<br>加工:1–2 份油<br>副:1–2 油饼/粕 → 饲料/肥料 | 清理→炒/烘→磨→蒸→制饼→压榨→过滤 | 食用油、油饼饲料、调味油 | P1 |
| 46 | `ramie` | A·纤维 | 韧皮纤维 | 麻屑→纸/堆肥；根茎可繁殖 | 根茎/分株 | 种子：采种→晒干→筛选→直播；无性：母株→扦插/分株→育苗→移栽 | 剥麻→沤麻→打麻→梳麻→纺线 | `fiber-bast` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 单位茎/叶<br>seed:1 粒或 1 段种茎<br>加工:2–4 份纤维<br>副:1–2 麻屑/叶渣 → 纸/堆肥/燃料 | 剥麻→沤麻→打麻→梳麻→纺线 | 布、绳、纸 | P2 |
| 47 | `chili` | A·茄果/瓜类 | 辣椒果实/辣椒粉 | 种子、辣椒秆→堆肥 | 种子 | 采种→晒干→筛选→育苗→移栽 | 鲜食/晒干→磨粉；发酵辣酱 | `fruit-spice` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 果<br>seed:1–2 粒<br>加工:1–2 份干辣椒/辣椒粉<br>副:1–2 辣椒秆/种子 | 鲜食/干制/酱三条出口：鲜食/晒干→磨粉；发酵辣酱 | 调料、辣酱 | P1 |
| 48 | `eggplant` | A·茄果/瓜类 | 果实/蔬菜（`tfcfarmingplus:food/eggplant`） | 种子、果肉/瓜瓤 → 饲料/堆肥；loofah 纤维、bottle_gourd 容器、瓜籽油 | 种子；多数育苗后移栽 | 采种→晒干→筛选→浸种/催芽→育苗盘→移栽 | 清洗→切片/取籽→晒干/磨粉/腌制/熬酱；loofah 取络、葫芦掏空 | `fruit-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 个果<br>seed:1–2 粒<br>加工:1–3 份酱/干/粉/容器/纤维<br>副:1–2 果肉/瓜瓤/种子 → 饲料/油/堆肥 | 清洗→切片/取籽→晒干/磨粉/腌制/熬酱；loofah 取络、葫芦掏空 | 蔬菜、香料、酱、籽油、洗具、容器 | P1 |
| 49 | `okra` | A·茄果/瓜类 | 果实/蔬菜（`tfcfarmingplus:food/okra`） | 种子、果肉/瓜瓤 → 饲料/堆肥；loofah 纤维、bottle_gourd 容器、瓜籽油 | 种子；多数育苗后移栽 | 采种→晒干→筛选→浸种/催芽→育苗盘→移栽 | 鲜食/晒干/腌渍 | `fruit-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 个果<br>seed:1–2 粒<br>加工:1–3 份酱/干/粉/容器/纤维<br>副:1–2 果肉/瓜瓤/种子 → 饲料/油/堆肥 | 鲜食/晒干/腌渍 | 蔬菜、干菜、腌菜 | P1 |
| 50 | `cotton` | A·纤维 | 棉纤维 + 棉籽油 | 棉籽→油/饼；棉秆→燃料 | 种子 | 种子：采种→晒干→筛选→直播；无性：母株→扦插/分株→育苗→移栽 | 轧棉→梳棉→纺线；棉籽压榨 | `fiber-oil` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 株<br>seed:1–2 粒<br>加工:2–3 份纤维 + 1–2 份棉籽油<br>副:1–2 棉籽饼 | 纤维与油料双线：轧棉→梳棉→纺线；棉籽压榨 | 布、油、饲料 | P2 |
| 51 | `asparagus` | A·叶菜/茎菜 | 食用叶/叶球/茎（`tfcfarmingplus:food/asparagus`）；水生叶菜按 A 现有产物 | 种子 + 外叶/叶柄/修整料 → 堆肥、饲料；纤维类副产（cardoon/artichoke） | 冠芽/分株 | 母株→冠芽→育苗→定植 | 采嫩茎→焯水/晒干/腌渍 | `leaf-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:8–12 叶/球/茎<br>seed:1<br>加工:2–4 份腌/干/切丝<br>副:2–4 外叶/叶柄 → 堆肥/饲料 | 采嫩茎→焯水/晒干/腌渍 | 蔬菜、干菜 | P1 |
| 52 | `chive` | A·香草/香料 | 叶/花/种子（`tfcfarmingplus:food/chive`） | 种子、茎叶修整料 → 留种/堆肥 | 种子或分株 | 采种→晒干→筛选→育苗/直播 | 采叶→干燥→研磨→过筛；鲜用 | `herb-dry` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–6 单位叶/花<br>seed:1 粒<br>加工:1–2 份干香草/粉<br>副:1 茎叶渣 → 堆肥 | 采叶→干燥→研磨→过筛；鲜用 | 调料、香草粉、腌渍、茶饮 | P2 |
| 53 | `rhubarb` | A·叶菜/茎菜 | 食用叶/叶球/茎（`tfcfarmingplus:food/rhubarb`）；水生叶菜按 A 现有产物 | 种子 + 外叶/叶柄/修整料 → 堆肥、饲料；纤维类副产（cardoon/artichoke） | 分株/冠芽 | 母株→分株→育苗→定植 | 采叶柄→去叶→糖渍/晒干 | `leaf-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:8–12 叶/球/茎<br>seed:1<br>加工:2–4 份腌/干/切丝<br>副:2–4 外叶/叶柄 → 堆肥/饲料 | 采叶柄→去叶→糖渍/晒干 | 甜点、果酱 | P1 |
| 54 | `artichoke` | A·叶菜/茎菜 | 食用叶/叶球/茎（`tfcfarmingplus:food/artichoke`）；水生叶菜按 A 现有产物 | 种子 + 外叶/叶柄/修整料 → 堆肥、饲料；纤维类副产（cardoon/artichoke） | 分株/冠芽 | 母株→分株→育苗→定植 | 采花苞→蒸煮/腌渍 | `leaf-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:8–12 叶/球/茎<br>seed:1<br>加工:2–4 份腌/干/切丝<br>副:2–4 外叶/叶柄 → 堆肥/饲料 | 采花苞→蒸煮/腌渍 | 蔬菜、腌菜 | P1 |
| 55 | `taro` | A·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfcfarmingplus:food/taro`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 球茎/分株 | 种芋→催芽→定植 | 清洗→去皮→煮/蒸→制泥/晒干 | `root-detox` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 块根<br>seed:1 段种茎/种芋<br>加工:1–2 份淀粉/粉<br>副:1–2 皮渣/茎叶 | 先去毒（浸泡/煮熟/发酵）→清洗→去皮→煮/蒸→制泥/晒干 | 主食、淀粉 | P1 |
| 56 | `water_chestnut` | A·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfcfarmingplus:food/water_chestnut`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 球茎 | 种球→浅水定植 | 采球→去皮→煮/磨粉 | `root-starch` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 根/块茎<br>seed:1 个种薯/种球或 1 粒种子<br>加工:1–2 份淀粉/粉/干片<br>副:1–2 皮渣/茎叶 → 饲料/堆肥 | 先分级/催芽或去壳，再煮/磨粉：采球→去皮→煮/磨粉 | 主食、淀粉 | P1 |
| 57 | `water_caltrop` | A·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfcfarmingplus:food/water_caltrop`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 种子/球茎 | 种球→浅水定植 | 采果→去壳→煮/磨粉 | `root-starch` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 根/块茎<br>seed:1 个种薯/种球或 1 粒种子<br>加工:1–2 份淀粉/粉/干片<br>副:1–2 皮渣/茎叶 → 饲料/堆肥 | 先分级/催芽或去壳，再煮/磨粉：采果→去壳→煮/磨粉 | 主食、淀粉 | P1 |
| 58 | `wild_rice_stem` | A·水生/其他 | 水生谷物 | 秸秆→饲料/编织 | 种子/分株 | 种子：采种→晒干→筛选→浅水直播；根茎：分株→定植 | 采穗→脱粒→碾米 | `water-grain` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 单位水生器官<br>seed:1–2 粒/种茎<br>加工:1–2 份米/粉/菜<br>副:1–2 叶渣/根茎 → 堆肥/饲料 | 采穗→脱粒→碾米 | 粮食 | P2 |
| 59 | `lotus` | A·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfcfarmingplus:food/lotus`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 根茎（藕） | 种藕→浅水定植 | 采藕→去节→切片→煮/磨粉；莲子另收 | `root-starch` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 根/块茎<br>seed:1 个种薯/种球或 1 粒种子<br>加工:1–2 份淀粉/粉/干片<br>副:1–2 皮渣/茎叶 → 饲料/堆肥 | 先分级/催芽或去壳，再煮/磨粉：采藕→去节→切片→煮/磨粉；莲子另收 | 蔬菜、淀粉、莲子 | P1 |
| 60 | `water_dropwort` | A·水生/其他 | 水生叶菜 | 茎叶渣→堆肥 | 分株/扦插 | 种子：采种→晒干→筛选→浅水直播；根茎：分株→定植 | 采嫩茎叶→焯水/晒干 | `water-grain` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 单位水生器官<br>seed:1–2 粒/种茎<br>加工:1–2 份米/粉/菜<br>副:1–2 叶渣/根茎 → 堆肥/饲料 | 采嫩茎叶→焯水/晒干 | 蔬菜 | P2 |
| 61 | `water_spinach` | A·叶菜/茎菜 | 水生叶菜 | 茎叶渣→堆肥 | 种子/扦插 | 种子：采种→晒干→筛选→浸种/催芽→育苗盘→移栽；分株：母株→分株→育苗→定植 | 采嫩茎叶→焯水/晒干 | `leaf-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:8–12 叶/球/茎<br>seed:1<br>加工:2–4 份腌/干/切丝<br>副:2–4 外叶/叶柄 → 堆肥/饲料 | 采嫩茎叶→焯水/晒干 | 蔬菜 | P1 |
| 62 | `arrowhead` | A·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfcfarmingplus:food/arrowhead`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 球茎 | 种球→浅水定植 | 采球→去皮→煮/晒干 | `root-starch` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 根/块茎<br>seed:1 个种薯/种球或 1 粒种子<br>加工:1–2 份淀粉/粉/干片<br>副:1–2 皮渣/茎叶 → 饲料/堆肥 | 先分级/催芽或去壳，再煮/磨粉：采球→去皮→煮/晒干 | 蔬菜、淀粉 | P1 |
| 63 | `gorgon_nut` | A·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfcfarmingplus:food/gorgon_nut`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 种子 | 采种→浸种→浅水育苗→定植 | 采种→脱壳→煮/磨粉 | `root-starch` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 根/块茎<br>seed:1 个种薯/种球或 1 粒种子<br>加工:1–2 份淀粉/粉/干片<br>副:1–2 皮渣/茎叶 → 饲料/堆肥 | 先分级/催芽或去壳，再煮/磨粉：采种→脱壳→煮/磨粉 | 粮食、淀粉 | P1 |
| 64 | `winter_melon` | A·茄果/瓜类 | 果实；种子 | 瓜籽→炒制/榨油；瓜瓤→饲料 | 种子 | 采种→晒干→筛选→浸种/催芽→育苗盘→移栽 | 果实→切块/熬酱/糖渍；瓜籽→洗净晒干 | `fruit-seed` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 果<br>seed:1–2 粒<br>加工:2–4 份果肉/酱 + 1–2 份瓜籽<br>副:瓜瓤/皮 → 饲料/堆肥 | 果肉与瓜籽分开：果实→切块/熬酱/糖渍；瓜籽→洗净晒干 | 蔬菜、瓜酱、籽油 | P1 |
| 65 | `hops` | A·特用 | 啤酒花 | 藤蔓→堆肥/纤维 | 根茎/扦插 | 母株→根茎/扦插→搭架定植 | 采花→干燥→酿酒 | `special-brew` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 花<br>seed:1 段根茎<br>加工:1–2 份干啤酒花<br>副:1 藤蔓/叶 | 先干燥后酿酒：采花→干燥→酿酒 | 啤酒 | P2/P3 |
| 66 | `loofah` | A·茄果/瓜类 | 嫩果食用 + 老果纤维 | 丝瓜络、种子 | 种子 | 采种→晒干→筛选→浸种/催芽→育苗盘→移栽 | 嫩果食用；老果泡水→去皮去籽→丝瓜络 | `fruit-fiber` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 果<br>seed:1–2 粒<br>加工:嫩果 2–4 份 + 老果纤维 1–2 份<br>副:1–2 种子/果渣 | 嫩果/老果分收：嫩果食用；老果泡水→去皮去籽→丝瓜络 | 蔬菜、洗具、过滤 | P1 |
| 67 | `bitter_melon` | A·茄果/瓜类 | 果实/蔬菜（`tfcfarmingplus:food/bitter_melon`） | 种子、果肉/瓜瓤 → 饲料/堆肥；loofah 纤维、bottle_gourd 容器、瓜籽油 | 种子；多数育苗后移栽 | 采种→晒干→筛选→浸种/催芽→育苗盘→移栽 | 清洗→切片/取籽→晒干/磨粉/腌制/熬酱；loofah 取络、葫芦掏空 | `fruit-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 个果<br>seed:1–2 粒<br>加工:1–3 份酱/干/粉/容器/纤维<br>副:1–2 果肉/瓜瓤/种子 → 饲料/油/堆肥 | 清洗→切片/取籽→晒干/磨粉/腌制/熬酱；loofah 取络、葫芦掏空 | 蔬菜、香料、酱、籽油、洗具、容器 | P1 |
| 68 | `snake_gourd` | A·茄果/瓜类 | 果实/蔬菜（`tfcfarmingplus:food/snake_gourd`） | 种子、果肉/瓜瓤 → 饲料/堆肥；loofah 纤维、bottle_gourd 容器、瓜籽油 | 种子；多数育苗后移栽 | 采种→晒干→筛选→浸种/催芽→育苗盘→移栽 | 清洗→切片/取籽→晒干/磨粉/腌制/熬酱；loofah 取络、葫芦掏空 | `fruit-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 个果<br>seed:1–2 粒<br>加工:1–3 份酱/干/粉/容器/纤维<br>副:1–2 果肉/瓜瓤/种子 → 饲料/油/堆肥 | 清洗→切片/取籽→晒干/磨粉/腌制/熬酱；loofah 取络、葫芦掏空 | 蔬菜、香料、酱、籽油、洗具、容器 | P1 |
| 69 | `yam` | A·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfcfarmingplus:food/yam`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 块茎/零余子 | 种薯→催芽→定植 | 清洗→去皮→煮/蒸/磨粉 | `root-detox` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 块根<br>seed:1 段种茎/种芋<br>加工:1–2 份淀粉/粉<br>副:1–2 皮渣/茎叶 | 先去毒（浸泡/煮熟/发酵）→清洗→去皮→煮/蒸/磨粉 | 主食、淀粉 | P1 |
| 70 | `malabar_spinach` | A·叶菜/茎菜 | 食用叶/叶球/茎（`tfcfarmingplus:food/malabar_spinach`）；水生叶菜按 A 现有产物 | 种子 + 外叶/叶柄/修整料 → 堆肥、饲料；纤维类副产（cardoon/artichoke） | 种子/扦插 | 种子：采种→晒干→筛选→浸种/催芽→育苗盘→移栽；分株：母株→分株→育苗→定植 | 采嫩茎叶→焯水/晒干 | `leaf-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:8–12 叶/球/茎<br>seed:1<br>加工:2–4 份腌/干/切丝<br>副:2–4 外叶/叶柄 → 堆肥/饲料 | 采嫩茎叶→焯水/晒干 | 蔬菜 | P1 |
| 71 | `chayote` | A·茄果/瓜类 | 果实/蔬菜（`tfcfarmingplus:food/chayote`） | 种子、果肉/瓜瓤 → 饲料/堆肥；loofah 纤维、bottle_gourd 容器、瓜籽油 | 种子；多数育苗后移栽 | 采种→晒干→筛选→浸种/催芽→育苗盘→移栽 | 清洗→切片/取籽→晒干/磨粉/腌制/熬酱；loofah 取络、葫芦掏空 | `fruit-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 个果<br>seed:1–2 粒<br>加工:1–3 份酱/干/粉/容器/纤维<br>副:1–2 果肉/瓜瓤/种子 → 饲料/油/堆肥 | 清洗→切片/取籽→晒干/磨粉/腌制/熬酱；loofah 取络、葫芦掏空 | 蔬菜、香料、酱、籽油、洗具、容器 | P1 |
| 72 | `bottle_gourd` | A·茄果/瓜类 | 嫩果食用 + 老果容器 | 种子、葫芦壳 | 种子 | 采种→晒干→筛选→浸种/催芽→育苗盘→移栽 | 嫩果食用；老果掏空→晾干→容器 | `fruit-container` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 果<br>seed:1–2 粒<br>加工:嫩果 2–4 份 + 老果容器 1–2 个<br>副:1–2 种子/壳 | 嫩果/老果分收：嫩果食用；老果掏空→晾干→容器 | 蔬菜、容器、水瓢 | P1 |
| 73 | `cantaloupe` | A·茄果/瓜类 | 果实；种子 | 瓜籽→炒制/榨油；瓜瓤→饲料 | 种子 | 采种→晒干→筛选→浸种/催芽→育苗盘→移栽 | 果实→鲜食/果酱；瓜籽→洗净晒干 | `fruit-seed` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 果<br>seed:1–2 粒<br>加工:2–4 份果肉/酱 + 1–2 份瓜籽<br>副:瓜瓤/皮 → 饲料/堆肥 | 果肉与瓜籽分开：果实→鲜食/果酱；瓜籽→洗净晒干 | 水果、果酱、籽油 | P1 |
| 74 | `water_shield` | A·水生/其他 | 水生叶菜/根 | 叶渣→堆肥 | 种子/分株 | 种子：采种→晒干→筛选→浅水直播；根茎：分株→定植 | 采叶/根→清洗→煮/晒干 | `water-grain` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 单位水生器官<br>seed:1–2 粒/种茎<br>加工:1–2 份米/粉/菜<br>副:1–2 叶渣/根茎 → 堆肥/饲料 | 采叶/根→清洗→煮/晒干 | 蔬菜 | P2 |
| 75 | `cardoon` | A·叶菜/茎菜 | 食用叶/叶球/茎（`tfcfarmingplus:food/cardoon`）；水生叶菜按 A 现有产物 | 种子 + 外叶/叶柄/修整料 → 堆肥、饲料；纤维类副产（cardoon/artichoke） | 分株/种子 | 种子育苗或分株→定植 | 采叶柄→去筋→焯水/腌渍；纤维副产 | `leaf-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:8–12 叶/球/茎<br>seed:1<br>加工:2–4 份腌/干/切丝<br>副:2–4 外叶/叶柄 → 堆肥/饲料 | 采叶柄→去筋→焯水/腌渍；纤维副产 | 蔬菜、纤维 | P1 |
| 76 | `agave` | A·特用 | 纤维 + 龙舌兰糖浆 | 叶渣→纤维/饲料；糖蜜 | 吸芽/种子 | 按物种各自处理；详见行内覆盖 | 割叶→刮纤维；烤心→压汁→熬糖浆 | `fiber-syrup` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 叶/心<br>seed:1 吸芽<br>加工:2–4 份纤维 + 1–2 糖浆<br>副:1–2 叶渣/糖蜜 | 叶纤维与心糖浆分开：割叶→刮纤维；烤心→压汁→熬糖浆 | 绳、布、糖浆 | P2/P3 |
| 77 | `purslane` | A·叶菜/茎菜 | 食用叶/叶球/茎（`tfcfarmingplus:food/purslane`）；水生叶菜按 A 现有产物 | 种子 + 外叶/叶柄/修整料 → 堆肥、饲料；纤维类副产（cardoon/artichoke） | 种子直播/育苗移栽；artichoke/cardoon/rhubarb/asparagus 用分株/冠芽 | 种子：采种→晒干→筛选→浸种/催芽→育苗盘→移栽；分株：母株→分株→育苗→定植 | 清洗→切/撕→盐渍→乳酸发酵→晒干；叶球类可切丝盐渍 | `leaf-preserve` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:8–12 叶/球/茎<br>seed:1<br>加工:2–4 份腌/干/切丝<br>副:2–4 外叶/叶柄 → 堆肥/饲料 | 清洗→切/撕→盐渍→乳酸发酵→晒干；叶球类可切丝盐渍 | 沙拉、汤、腌菜、干菜、堆肥/饲料 | P1 |
| 78 | `pea` | A·豆类 | 干豆或鲜荚（`tfcfarmingplus:food/pea`；TFC 用 `tfc:food/pea`） | 豆荚、秸秆、种子 → 饲料、堆肥、留种 | 种子 | 采种→晒干→筛选→浸种→直播 | 干燥→脱荚→浸泡→磨浆/煮制/发酵 | `legume-dry` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 荚/豆<br>seed:1–2 粒<br>加工:2–4 份干豆/豆粉/豆制品<br>副:1–3 豆荚/秸秆 → 饲料/堆肥 | 先脱荚/浸泡，豆类去毒/磨浆：干燥→脱荚→浸泡→磨浆/煮制/发酵 | 豆制品、豆粉、豆酱、饲料 | P1 |
| 79 | `cowpea` | A·豆类 | 干豆或鲜荚（`tfcfarmingplus:food/cowpea`；TFC 用 `tfc:food/cowpea`） | 豆荚、秸秆、种子 → 饲料、堆肥、留种 | 种子 | 采种→晒干→筛选→浸种→直播 | 干燥→脱荚→浸泡→磨浆/煮制/发酵 | `legume-dry` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 荚/豆<br>seed:1–2 粒<br>加工:2–4 份干豆/豆粉/豆制品<br>副:1–3 豆荚/秸秆 → 饲料/堆肥 | 先脱荚/浸泡，豆类去毒/磨浆：干燥→脱荚→浸泡→磨浆/煮制/发酵 | 豆制品、豆粉、豆酱、饲料 | P1 |
| 80 | `common_bean` | A·豆类 | 干豆或鲜荚（`tfcfarmingplus:food/common_bean`；TFC 用 `tfc:food/common_bean`） | 豆荚、秸秆、种子 → 饲料、堆肥、留种 | 种子 | 采种→晒干→筛选→浸种→直播 | 干燥→脱荚→浸泡→磨浆/煮制/发酵 | `legume-dry` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 荚/豆<br>seed:1–2 粒<br>加工:2–4 份干豆/豆粉/豆制品<br>副:1–3 豆荚/秸秆 → 饲料/堆肥 | 先脱荚/浸泡，豆类去毒/磨浆：干燥→脱荚→浸泡→磨浆/煮制/发酵 | 豆制品、豆粉、豆酱、饲料 | P1 |
| 81 | `winged_bean` | A·豆类 | 干豆或鲜荚（`tfcfarmingplus:food/winged_bean`；TFC 用 `tfc:food/winged_bean`） | 豆荚、秸秆、种子 → 饲料、堆肥、留种 | 种子 | 采种→晒干→筛选→浸种→直播 | 干燥→脱荚→浸泡→磨浆/煮制/发酵 | `legume-dry` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 荚/豆<br>seed:1–2 粒<br>加工:2–4 份干豆/豆粉/豆制品<br>副:1–3 豆荚/秸秆 → 饲料/堆肥 | 先脱荚/浸泡，豆类去毒/磨浆：干燥→脱荚→浸泡→磨浆/煮制/发酵 | 豆制品、豆粉、豆酱、饲料 | P1 |
| 82 | `pigeon_pea` | A·豆类 | 干豆或鲜荚（`tfcfarmingplus:food/pigeon_pea`；TFC 用 `tfc:food/pigeon_pea`） | 豆荚、秸秆、种子 → 饲料、堆肥、留种 | 种子 | 采种→晒干→筛选→浸种→直播 | 干燥→脱荚→浸泡→磨浆/煮制/发酵 | `legume-dry` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 荚/豆<br>seed:1–2 粒<br>加工:2–4 份干豆/豆粉/豆制品<br>副:1–3 豆荚/秸秆 → 饲料/堆肥 | 先脱荚/浸泡，豆类去毒/磨浆：干燥→脱荚→浸泡→磨浆/煮制/发酵 | 豆制品、豆粉、豆酱、饲料 | P1 |
| 83 | `sunflower` | A·油料 | 油籽 → 食用油（`tfcfarmingplus:food/sunflower` / 油料产物） | 油饼/粕 → 饲料、肥料；部分纤维/秸秆 | 种子 | 采种→晒干→筛选→直播 | 清理→炒/烘→磨→蒸→制饼→压榨→过滤 | `oil-press` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 单位油籽<br>seed:1–2 粒<br>加工:1–2 份油<br>副:1–2 油饼/粕 → 饲料/肥料 | 清理→炒/烘→磨→蒸→制饼→压榨→过滤 | 食用油、油饼饲料、调味油 | P1 |
| 84 | `hemp` | A·纤维 | 纤维 + 大麻籽油 | 麻屑/籽饼→饲料/建材/纸 | 种子 | 种子：采种→晒干→筛选→直播；无性：母株→扦插/分株→育苗→移栽 | 沤麻→打麻→梳麻→纺线；种子压榨 | `fiber-oil` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 茎/籽<br>seed:1–2 粒<br>加工:2–3 份纤维 + 1–2 份油<br>副:1–2 麻屑/油饼 | 纤维与油料双线：沤麻→打麻→梳麻→纺线；种子压榨 | 布、绳、纸、油 | P2 |
| 85 | `sorghum` | A·谷物/禾本 | 谷物籽粒（`tfcfarmingplus:food/sorghum`；TFC 用 `tfc:food/sorghum`） | 秸秆、糠/麸、种子 → 饲料、堆肥、燃料、留种 | 种子 | 采种→晒干→筛选→浸种/催芽（可选）→直播 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | `grain-mill` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:6–10 穗/籽粒<br>seed:1–2 粒<br>加工:3–5 份面粉/米/麦芽<br>副:2–4 秸秆/糠麸 → 饲料/燃料/堆肥 | 脱粒→去壳/磨粉；秸秆另收：脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | 面粉/米饭/麦芽/酿酒/饲料/燃料 | P1 |
| 86 | `sisal` | A·纤维 | 叶纤维 | 叶渣→堆肥/沼气 | 吸芽/分株 | 种子：采种→晒干→筛选→直播；无性：母株→扦插/分株→育苗→移栽 | 割叶→刮肉→晒干→梳麻→纺绳 | `fiber-bast` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 单位茎/叶<br>seed:1 粒或 1 段种茎<br>加工:2–4 份纤维<br>副:1–2 麻屑/叶渣 → 纸/堆肥/燃料 | 割叶→刮肉→晒干→梳麻→纺绳 | 绳、网、垫 | P2 |
| 87 | `strawberry` | A·浆果特例 | 浆果（`tfcfarmingplus:food/strawberry`） | 匍匐茎苗/种子；果渣 → 堆肥 | 匍匐茎分株为主，种子为辅 | 母株→匍匐茎苗→育苗→移栽 | 鲜食→果酱/果干/冰淇淋 | `berry-runner` | 现:0–(6–10)，种子 1（个别 1–2）<br>目标:4–8 个浆果<br>seed:匍匐茎苗 1–2 株<br>加工:1–2 份果酱/果干<br>副:1 果渣 → 堆肥 | 鲜食→果酱/果干/冰淇淋 | 鲜果、果酱、果干、甜点 | P1 |

## 8. TFC 29 作物矩阵

**TFC 29 不是资源旁路**：B 要替换/覆盖 TFC 的原种植与收获流程：
- 覆盖 TFC 29 的作物 blockstate/model/loot table，不再保留原 6–10 直掉；
- 种植：种子处理（DataComponent）、B 的育苗/移栽/农艺流程接入 TFC 作物；
- 收获：A/TFC 谷物全部走 `grain_bundle → 脱粒 → 谷粒 + wet_grass`；非谷物按 B 的 profile 出主/副产品；
- TFC 方块行为通过 B 的 block/mixin 接管；旧存档的 TFC 作物状态给默认迁移值；
- 矩阵中的“TFC 原值”只是回退基线，不是最终目标。
| # | 作物 | 来源/组 | 主产品 | 副产品 | 繁殖 | 育苗/种子处理 | 初步加工 | 流程 | 产率计划（现/目标/seed/加工/副） | 定制关键步骤 | 出口 | 批次 |
|---:|---|---|---|---|---|---|---|---|---|---|---|---|
| 88 | `alfalfa` | TFC·叶菜/饲草 | 饲草/种子 | 干草→饲料 | 种子 | 采种→晒干→筛选→直播 | 割草→晒干→打捆；种子清选 | `leaf-forage` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1–2 粒<br>加工:2–4 份干草/饲料<br>副:1–2 秸秆 → 堆肥/燃料 | 割草→晒干→打捆；种子清选 | 饲料、种子 | P1 |
| 89 | `barley` | TFC·谷物/禾本 | 谷物籽粒（`tfc:food/barley`；TFC 用 `tfc:food/barley`） | 秸秆、糠/麸、种子 → 饲料、堆肥、燃料、留种 | 种子 | 采种→晒干→筛选→浸种/催芽（可选）→直播 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | `grain-malt` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1–2 粒<br>加工:3–5 份麦芽/面粉<br>副:2–4 秸秆/糠 | 先脱粒/扬场，麦类另走麦芽：脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | 面粉/米饭/麦芽/酿酒/饲料/燃料 | P1 |
| 90 | `beet` | TFC·根/块茎/鳞茎 | 根/糖 | 叶/渣→饲料 | 种子（turnip/parsnip/celeriac/salsify/chicory/radish/carrot/beet）或块茎/鳞茎/根茎（其余） | 种子：采种→晒干→筛选→浸种→直播；块茎/鳞茎：愈伤→分级→直播 | 清洗→切片→煮/榨糖/腌渍 | `root-starch` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1 个种薯/种球或 1 粒种子<br>加工:1–2 份淀粉/粉/干片<br>副:1–2 皮渣/茎叶 → 饲料/堆肥 | 先去皮/切片，再晒干或沉淀淀粉：清洗→切片→煮/榨糖/腌渍 | 糖、蔬菜、饲料 | P1 |
| 91 | `cabbage` | TFC·叶菜/饲草 | 叶菜/饲草（TFC 现有产物） | 种子/秸秆 → 留种、饲料、堆肥 | 种子 | 采种→晒干→筛选→直播 | 切丝→盐渍→乳酸发酵→晒干 | `leaf-preserve` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1<br>加工:2–4 份酸菜/干菜<br>副:3–4 外叶 | 先切分/盐渍，叶球类可发酵：切丝→盐渍→乳酸发酵→晒干 | 酸菜、泡菜、干菜 | P1 |
| 92 | `canola` | TFC·豆类/油料 | 油菜籽/菜籽油 | 豆荚/秸秆/油饼 → 饲料、堆肥 | 种子 | 采种→晒干→筛选→浸种→直播 | 干燥→清理→压榨→过滤 | `oil-press` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1–2 粒<br>加工:1–2 份油<br>副:1–2 菜籽饼 | 干燥→清理→压榨→过滤 | 食用油、油饼饲料 | P1 |
| 93 | `carrot` | TFC·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfc:food/carrot`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 种子（turnip/parsnip/celeriac/salsify/chicory/radish/carrot/beet）或块茎/鳞茎/根茎（其余） | 种子：采种→晒干→筛选→浸种→直播；块茎/鳞茎：愈伤→分级→直播 | 清洗→去皮→切片→煮/晒干/腌渍 | `root-starch` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1 个种薯/种球或 1 粒种子<br>加工:1–2 份淀粉/粉/干片<br>副:1–2 皮渣/茎叶 → 饲料/堆肥 | 先去皮/切片，再晒干或沉淀淀粉：清洗→去皮→切片→煮/晒干/腌渍 | 蔬菜、干菜 | P1 |
| 94 | `cassava` | TFC·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfc:food/cassava`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 茎段 | 种茎→切段→定植 | 去皮→磨浆→沉淀淀粉/发酵 | `root-detox` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1 段种茎<br>加工:1–3 份淀粉<br>副:1–2 皮渣/叶 | 先去毒（浸泡/煮熟/发酵）→去皮→磨浆→沉淀淀粉/发酵 | 淀粉、木薯粉 | P1 |
| 95 | `garlic` | TFC·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfc:food/garlic`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 蒜瓣 | 蒜瓣→分级→定植 | 干燥→去皮→切片→晒干/腌渍 | `root-spice` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1 个蒜瓣<br>加工:1–2 份干蒜/蒜粉<br>副:1 皮/叶 | 先分级/催芽或去壳，再煮/磨粉：干燥→去皮→切片→晒干/腌渍 | 调料、腌菜 | P1 |
| 96 | `green_bean` | TFC·豆类/油料 | 鲜荚/干豆 | 豆荚/秸秆/油饼 → 饲料、堆肥 | 种子 | 采种→晒干→筛选→浸种→直播 | 鲜食/晒干/脱荚 | `legume-dry` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1–2 粒<br>加工:2–4 份干豆/豆粉/豆制品<br>副:1–3 豆荚/秸秆 → 饲料/堆肥 | 先脱荚/浸泡，豆类去毒/磨浆：鲜食/晒干/脱荚 | 蔬菜、干豆 | P1 |
| 97 | `jute` | TFC·纤维 | 韧皮纤维 | 麻屑/种子→纸/饲料 | 种子 | 种子：采种→晒干→筛选→直播；无性：母株→扦插/分株→育苗→移栽 | 沤麻→打麻→梳麻→纺线/织袋 | `fiber-bast` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1 粒或 1 段种茎<br>加工:2–4 份纤维<br>副:1–2 麻屑/叶渣 → 纸/堆肥/燃料 | 沤麻→打麻→梳麻→纺线/织袋 | 麻袋、绳、纸 | P2 |
| 98 | `lentil` | TFC·豆类/油料 | 干豆 | 豆荚/秸秆/油饼 → 饲料、堆肥 | 种子 | 采种→晒干→筛选→浸种→直播 | 干燥→脱荚→煮/磨粉 | `legume-dry` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1–2 粒<br>加工:2–4 份干豆/豆粉/豆制品<br>副:1–3 豆荚/秸秆 → 饲料/堆肥 | 先脱荚/浸泡，豆类去毒/磨浆：干燥→脱荚→煮/磨粉 | 豆类、豆粉 | P1 |
| 99 | `maize` | TFC·谷物/禾本 | 谷物籽粒（`tfc:food/maize`；TFC 用 `tfc:food/maize`） | 秸秆、糠/麸、种子 → 饲料、堆肥、燃料、留种 | 种子 | 采种→晒干→筛选→浸种/催芽（可选）→直播 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | `grain-mill` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1–2 粒<br>加工:3–5 份面粉/米/麦芽<br>副:2–4 秸秆/糠麸 → 饲料/燃料/堆肥 | 脱粒→去壳/磨粉；秸秆另收：脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | 面粉/米饭/麦芽/酿酒/饲料/燃料 | P1 |
| 100 | `melon` | TFC·茄果/瓜类 | 果实；种子 | 瓜籽→炒制/榨油 | 种子；多数育苗后移栽 | 采种→晒干→筛选→浸种/催芽→育苗盘→移栽 | 鲜食/果酱；瓜籽洗净晒干 | `fruit-seed` | 现:果实方块 1–2 个（非 6–10 池）<br>目标:1–2 个果实（果实方块，不是 6–10 作物池）<br>seed:1–2 粒<br>加工:1–3 份果肉/酱 + 1–2 份瓜籽<br>副:1–2 瓜瓤 | 果肉与瓜籽分开：鲜食/果酱；瓜籽洗净晒干 | 水果、籽油 | P1 |
| 101 | `oat` | TFC·谷物/禾本 | 谷物籽粒（`tfc:food/oat`；TFC 用 `tfc:food/oat`） | 秸秆、糠/麸、种子 → 饲料、堆肥、燃料、留种 | 种子 | 采种→晒干→筛选→浸种/催芽（可选）→直播 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | `grain-malt` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1–2 粒<br>加工:3–5 份面粉/麦芽<br>副:2–4 秸秆/糠 | 先脱粒/扬场，麦类另走麦芽：脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | 面粉/米饭/麦芽/酿酒/饲料/燃料 | P1 |
| 102 | `onion` | TFC·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfc:food/onion`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 种球/种子 | 种球→分级→定植；种子育苗 | 干燥→去皮→切片→晒干/腌渍 | `root-spice` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1 粒种子/1 个种球<br>加工:1–2 份干洋葱/洋葱粉<br>副:1–2 皮/叶 | 先分级/催芽或去壳，再煮/磨粉：干燥→去皮→切片→晒干/腌渍 | 调料、腌菜 | P1 |
| 103 | `papyrus` | TFC·水生/纤维 | 纤维/纸 | 根茎/叶渣→堆肥 | 根茎/分株 | 母株→分株→浅水定植 | 割茎→剥皮→压片→晾干→纸 | `fiber-water` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1 段根茎<br>加工:1–3 份纤维/纸<br>副:1–2 叶渣/根茎 → 堆肥 | 割茎→剥皮→压片→晾干→纸 | 纸、编织 | P2 |
| 104 | `peanut` | TFC·豆类/油料 | 花生/花生油 | 豆荚/秸秆/油饼 → 饲料、堆肥 | 种子 | 采种→晒干→筛选→浸种→直播 | 干燥→脱壳→炒/压榨 | `oil-press` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1–2 粒<br>加工:1–2 份油 + 2–3 份坚果<br>副:1–2 花生饼 | 干燥→脱壳→炒/压榨 | 坚果、油、花生酱 | P1 |
| 105 | `potato` | TFC·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfc:food/potato`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 种薯 | 种薯→催芽→切块→直播 | 清洗→去皮→煮/炸/淀粉 | `root-starch` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1 个种薯<br>加工:2–4 份淀粉/薯制品<br>副:1–2 皮渣 | 先分级/催芽或去壳，再煮/磨粉：清洗→去皮→煮/炸/淀粉 | 主食、淀粉 | P1 |
| 106 | `pumpkin` | TFC·茄果/瓜类 | 果实；种子 | 瓜籽→炒制/榨油；瓜肉→饲料 | 种子；多数育苗后移栽 | 采种→晒干→筛选→浸种/催芽→育苗盘→移栽 | 果实→煮/烤/熬酱；瓜籽洗净晒干 | `fruit-seed` | 现:果实方块 1–2 个（非 6–10 池）<br>目标:1–2 个果实（果实方块，不是 6–10 作物池）<br>seed:1–2 粒<br>加工:1–3 份果肉/酱 + 1–2 份瓜籽<br>副:1–2 瓜瓤 | 果肉与瓜籽分开：果实→煮/烤/熬酱；瓜籽洗净晒干 | 蔬菜、籽油、饲料 | P1 |
| 107 | `radish` | TFC·根/块茎/鳞茎 | 食用根/块茎/鳞茎，或淀粉/粉（`tfc:food/radish`） | 茎叶/皮渣 → 饲料、堆肥；种薯/种球/种瓣留种 | 种子（turnip/parsnip/celeriac/salsify/chicory/radish/carrot/beet）或块茎/鳞茎/根茎（其余） | 种子：采种→晒干→筛选→浸种→直播；块茎/鳞茎：愈伤→分级→直播 | 清洗→切片→腌渍/晒干 | `root-starch` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1 个种薯/种球或 1 粒种子<br>加工:1–2 份淀粉/粉/干片<br>副:1–2 皮渣/茎叶 → 饲料/堆肥 | 先去皮/切片，再晒干或沉淀淀粉：清洗→切片→腌渍/晒干 | 蔬菜、腌菜 | P1 |
| 108 | `red_bell_pepper` | TFC·茄果/瓜类 | 果实/蔬菜（`tfc:food/red_bell_pepper`） | 种子、果肉/瓜瓤 → 饲料/堆肥；loofah 纤维、bottle_gourd 容器、瓜籽油 | 种子；多数育苗后移栽 | 采种→晒干→筛选→浸种/催芽→育苗盘→移栽 | 鲜食→晒干→磨粉/烤制 | `fruit-spice` | 现:4–5 ×2（TFC 原值）<br>目标:4–5（B 覆盖，双池）<br>seed:1–2 粒<br>加工:1–2 份干椒/椒粉<br>副:辣椒秆/种子 → 堆肥 | 鲜食→晒干→磨粉/烤制 | 蔬菜、香料 | P1 |
| 109 | `rice` | TFC·谷物/禾本 | 谷物籽粒（`tfc:food/rice`；TFC 用 `tfc:food/rice`） | 秸秆、糠/麸、种子 → 饲料、堆肥、燃料、留种 | 种子 | 采种→晒干→筛选→浸种/催芽（可选）→直播 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | `grain-rice` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1–2 粒<br>加工:3–5 份米<br>副:2–4 秸秆/糠 | 先脱粒、砻谷、碾米：脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | 面粉/米饭/麦芽/酿酒/饲料/燃料 | P1 |
| 110 | `rye` | TFC·谷物/禾本 | 谷物籽粒（`tfc:food/rye`；TFC 用 `tfc:food/rye`） | 秸秆、糠/麸、种子 → 饲料、堆肥、燃料、留种 | 种子 | 采种→晒干→筛选→浸种/催芽（可选）→直播 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | `grain-malt` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1–2 粒<br>加工:3–5 份面粉/麦芽<br>副:2–4 秸秆/糠 | 先脱粒/扬场，麦类另走麦芽：脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | 面粉/米饭/麦芽/酿酒/饲料/燃料 | P1 |
| 111 | `soybean` | TFC·豆类/油料 | 大豆 | 豆荚/秸秆/油饼 → 饲料、堆肥 | 种子 | 采种→晒干→筛选→浸种→直播 | 干燥→浸泡→磨浆→豆腐/豆酱/榨油 | `legume-oil` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1–2 粒<br>加工:2–4 份豆制品/油<br>副:1–2 豆荚/粕 | 干燥→浸泡→磨浆→豆腐/豆酱/榨油 | 豆制品、油、饲料 | P1 |
| 112 | `squash` | TFC·茄果/瓜类 | 果实；种子 | 瓜籽→炒制/榨油；瓜肉→饲料 | 种子；多数育苗后移栽 | 采种→晒干→筛选→浸种/催芽→育苗盘→移栽 | 果实→煮/烤/熬酱；瓜籽洗净晒干 | `fruit-seed` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1–2 粒<br>加工:2–4 份果肉/酱 + 1–2 份瓜籽<br>副:瓜瓤/皮 → 饲料/堆肥 | 果肉与瓜籽分开：果实→煮/烤/熬酱；瓜籽洗净晒干 | 蔬菜、籽油、饲料 | P1 |
| 113 | `sugarcane` | TFC·谷物/禾本 | 甘蔗/糖 | 蔗渣→燃料/纸；糖蜜→发酵 | 蔗种/茎段 | 采种→晒干→筛选→浸种/催芽（可选）→直播 | 压榨→熬糖→糖蜜/朗姆 | `sugar` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1 段蔗种<br>加工:2–4 份糖/糖蜜<br>副:2–4 蔗渣 | 压榨→熬糖，蔗渣另出口：压榨→熬糖→糖蜜/朗姆 | 糖、糖蜜、酒 | P1 |
| 114 | `tomato` | TFC·茄果/瓜类 | 果实/蔬菜（`tfc:food/tomato`） | 种子、果肉/瓜瓤 → 饲料/堆肥；loofah 纤维、bottle_gourd 容器、瓜籽油 | 种子；多数育苗后移栽 | 采种→晒干→筛选→浸种/催芽→育苗盘→移栽 | 鲜食→晒干/熬酱/罐装 | `fruit-paste` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1–2 粒<br>加工:1–2 份番茄酱/干番茄<br>副:1–2 果皮/籽 | 鲜食/干制/酱三条出口：鲜食→晒干/熬酱/罐装 | 蔬菜、番茄酱、干番茄 | P1 |
| 115 | `wheat` | TFC·谷物/禾本 | 谷物籽粒（`tfc:food/wheat`；TFC 用 `tfc:food/wheat`） | 秸秆、糠/麸、种子 → 饲料、堆肥、燃料、留种 | 种子 | 采种→晒干→筛选→浸种/催芽（可选）→直播 | 脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | `grain-malt` | 现:0–(6–10)，种子 1（部分 1–2）<br>目标:6–10（B 覆盖，旧值回退）<br>seed:1–2 粒<br>加工:3–5 份面粉<br>副:2–4 秸秆/糠 | 先脱粒/扬场，麦类另走麦芽：脱粒→扬场→磨粉；麦类可制麦芽；稻类可碾米 | 面粉/米饭/麦芽/酿酒/饲料/燃料 | P1 |
| 116 | `yellow_bell_pepper` | TFC·茄果/瓜类 | 果实/蔬菜（`tfc:food/yellow_bell_pepper`） | 种子、果肉/瓜瓤 → 饲料/堆肥；loofah 纤维、bottle_gourd 容器、瓜籽油 | 种子；多数育苗后移栽 | 采种→晒干→筛选→浸种/催芽→育苗盘→移栽 | 鲜食→晒干→磨粉/烤制 | `fruit-spice` | 现:4–5 ×2（TFC 原值）<br>目标:4–5（B 覆盖，双池）<br>seed:1–2 粒<br>加工:1–2 份干椒/椒粉<br>副:辣椒秆/种子 → 堆肥 | 鲜食→晒干→磨粉/烤制 | 蔬菜、香料 | P1 |

## 9. B 新增农作物/栽培物
> 本批是把此前搁置的香料、坚果、蘑菇纳入 B；它们不属于 A 87/TFC 29，必须单独建 ID/标签/手册/产量。
### 9.1 香料作物 20 种
| # | 物种 | 形态 | 主产品 | 副产品 | 繁殖 | 育苗 | 初步加工 | 出口 | 目标产率 |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `basil` | 草本 | 叶 | 茎叶渣 | 种子 | 采种→育苗→移栽 | 鲜叶→干燥→研磨 | 调料、沙拉、汤 | 2–4 株；叶 2–4 份 |
| 2 | `bay_laurel` | 灌木/小乔木 | 叶 | 枝条 | 种子/扦插 | 育苗→移栽 | 采叶→阴干→研磨 | 调料、汤、炖菜 | 2–3 株；叶 3–6 份 |
| 3 | `cardamom` | 根茎草本 | 果荚/种子 | 茎叶渣 | 根茎分株 | 分株→育苗→定植 | 采果→干燥→脱壳→研磨 | 调料、甜点、咖喱 | 2–4 株；荚 1–2 份 |
| 4 | `cilantro` | 草本 | 叶/种子 | 茎叶渣 | 种子 | 采种→育苗/直播 | 鲜叶/种子→干燥→研磨 | 调料、沙拉、汤 | 2–4 株；叶/籽 2–3 份 |
| 5 | `cumin` | 草本 | 种子 | 茎秆 | 种子 | 采种→直播 | 采种→干燥→研磨 | 调料、咖喱、烘焙 | 2–3 株；籽 1–2 份 |
| 6 | `oregano` | 草本 | 叶 | 茎叶渣 | 种子/分株 | 育苗/分株→移栽 | 采叶→干燥→研磨 | 调料、披萨、汤 | 2–4 株；叶 2–3 份 |
| 7 | `pimento` | 小乔木 | 浆果/干果 | 枝叶 | 种子/扦插 | 育苗→移栽 | 采果→干燥→研磨 | 香料、腌渍、甜点 | 2–3 株；果 1–2 份 |
| 8 | `vanilla` | 攀援兰 | 果荚 | 藤蔓 | 扦插 | 母株→扦插→搭架→定植 | 采荚→杀青→发酵→干燥 | 香草精、甜点 | 1–2 株；荚 1–2 份 |
| 9 | `black_pepper` | 攀援藤 | 胡椒粒 | 藤蔓/叶 | 扦插/种子 | 母株→扦插→搭架→定植 | 采果→浸泡→去皮→干燥→研磨 | 黑胡椒/白胡椒、调料 | 1–2 株；椒 1–2 份 |
| 10 | `cinnamon` | 乔木 | 树皮 | 枝叶 | 种子/萌蘖 | 育苗→定植；萌蘖更新 | 剥皮→阴干→卷曲→研磨 | 桂皮、肉桂粉、甜点 | 1–2 株；皮 1–2 份 |
| 11 | `clove` | 小乔木 | 花蕾 | 枝叶 | 种子/扦插 | 育苗→定植 | 采花蕾→干燥 | 丁香、腌渍、甜点 | 1–2 株；蕾 0.5–1 份 |
| 12 | `nutmeg` | 乔木 | 种仁/假种皮 | 果壳/果肉 | 种子/嫁接 | 育苗→定植 | 采果→去壳→干燥→研磨 | 肉豆蔻/肉豆蔻衣、甜点 | 1–2 株；仁 1 份 |
| 13 | `saffron` | 球茎草本 | 柱头 | 花瓣/球茎 | 球茎分株 | 球茎→分级→定植 | 采花→取柱头→阴干 | 藏红花、调味、染料 | 1–2 球；柱头 0.2–0.5 份 |
| 14 | `star_anise` | 乔木 | 八角果 | 枝叶 | 种子/扦插 | 育苗→定植 | 采果→干燥 | 八角、卤味、香料 | 1–2 株；果 1–2 份 |
| 15 | `rosemary` | 灌木 | 叶 | 枝条 | 扦插/种子 | 扦插→育苗→定植 | 采叶→干燥→研磨 | 迷迭香、烤肉、调料 | 2–4 株；叶 2–3 份 |
| 16 | `thyme` | 草本/小灌木 | 叶 | 茎叶渣 | 种子/分株 | 育苗/分株→定植 | 采叶→干燥→研磨 | 百里香、汤、调料 | 2–4 株；叶 2–3 份 |
| 17 | `sage` | 草本/小灌木 | 叶 | 茎叶渣 | 种子/扦插 | 育苗/扦插→定植 | 采叶→干燥→研磨 | 鼠尾草、烤肉、调料 | 2–4 株；叶 2–3 份 |
| 18 | `dill` | 草本 | 叶/种子 | 茎秆 | 种子 | 采种→直播/育苗 | 叶/种子→干燥→研磨 | 莳萝、腌渍、调料 | 2–4 株；叶/籽 2–3 份 |
| 19 | `fennel` | 草本 | 种子/叶/球茎 | 茎叶渣 | 种子 | 采种→育苗→移栽 | 种子/叶→干燥→研磨；球茎鲜食 | 茴香、调料、蔬菜 | 2–4 株；籽 1–2 份 |
| 20 | `mustard` | 草本 | 种子/叶 | 茎叶渣 | 种子 | 采种→直播 | 种子→研磨→制酱；叶鲜食/腌渍 | 芥末、芥菜、腌菜 | 2–4 株；籽 1–2 份 |
### 9.2 坚果
| 物种 | 来源 | 主产品 | 副产品 | 繁殖 | 采收/加工 | 出口 | 目标产率 |
|---|---|---|---|---|---|---|---|
| acorn（橡子） | B 新增（挂 oak） | 橡子 | 壳斗/壳 | 树上结果；树苗繁殖 | 成熟→落果/采收→去壳 | 干燥→去涩→烤/磨粉/榨油 | 4–8 个/树；壳 2–4 |
| chestnut（栗子） | B 新增（挂 chestnut） | 栗子 | 总苞/壳 | 树上结果；树苗繁殖 | 成熟→落果/采收→去壳 | 干燥→去壳→煮/烤/磨粉 | 4–8 个/树；壳 2–4 |
| pistachio | B 新增（乔木） | 开心果 | 壳 | 种子/嫁接 | 育苗→定植 | 去壳→干燥→烤/磨粉 | 4–8 个/树；壳 2–4 |
| cashew | B 新增（乔木） | 腰果 | 腰果苹果/壳 | 种子/嫁接 | 育苗→定植 | 去壳→烘烤→去皮 | 4–8 个/树；壳 2–4 |
| macadamia | B 新增（乔木） | 夏威夷果 | 壳 | 种子/嫁接 | 育苗→定植 | 去壳→干燥→烤/榨油 | 4–8 个/树；壳 2–4 |
| pine_nut | B 新增（挂 pine） | 松子 | 松塔/壳 | 树上结果；松苗繁殖 | 成熟→采松塔→取籽 | 去壳→干燥→烤/榨油 | 4–8 个/树；壳 2–4 |
| hickory_nut | B 新增（挂 hickory） | 山核桃 | 壳 | 树上结果；树苗繁殖 | 成熟→落果→去壳 | 干燥→去壳→烤/磨粉/榨油 | 4–8 个/树；壳 2–4 |
| beechnut | B 新增（挂 beech） | 山毛榉坚果 | 壳/总苞 | 树上结果；树苗繁殖 | 成熟→采收→去壳 | 干燥→去壳→烤/磨粉/榨油 | 4–8 个/树；壳 2–4 |
| almond | A 已有 | 杏仁 | 壳 | 果树/树苗 | 开花结果→采收 | 去壳→烤/磨粉/榨油 | — |
| hazelnut | A 已有 | 榛子 | 壳 | 果树/树苗 | 结果→采收 | 去壳→烤/磨粉/榨油 | — |
| pecan | A 已有 | 碧根果 | 壳 | 果树/树苗 | 结果→采收 | 去壳→烤/磨粉/榨油 | — |
| walnut | A 已有 | 核桃 | 壳 | 果树/树苗 | 结果→采收 | 去壳→烤/磨粉/榨油 | — |
| hardy_chestnut | AFC 已有 | 栗子 | 壳 | 果树/树苗 | 结果→采收 | 去壳→煮/烤/磨粉 | — |
| chinquapin | AFC 已有 | 栗子 | 壳 | 果树/树苗 | 结果→采收 | 去壳→煮/烤/磨粉 | — |
### 9.3 蘑菇 15 种：野生生成、刷新与栽培边界
**所有 15 种都要有世界自然生成**；其中部分只能自然生成/刷新，不能培育。野生蘑菇学习 TFC 原版野生植物：`PlantBlock`/`SeasonalPlantBlock` 的随机刻扩散、季节/气候休眠与重新刷新，不是一次性 worldgen。

- **可栽培 11 种**：oyster · shiitake · button · enoki · wood_ear · reishi · lions_mane · maitake · king_oyster · shimeji · turkey_tail
- **只能自然刷新、不可培育 4 种**：porcini · morel · chanterelle · black_truffle

| 类别 | 物种 | 生成/刷新 | 栽培 |
|---|---|---|---|
| 可栽培 | 上述 11 种 | 世界野生 + 菌包/腐木/菌根载体 | 菌包 4 stage |
| 自然专用 | porcini · morel · chanterelle · black_truffle | 只在对应林地/树根/林下菌床生成；随机刻重新刷新 | **禁止菌包配方** |

野生蘑菇实现：
- 新增 B 的 wild mushroom 方块/物品，按 TFC `PlantBlock`/`SeasonalPlantBlock` 做随机刻、季节、气候、扩散/刷新；
- worldgen `configured_feature` / `placed_feature` + biome tag；自然专用 4 种只生成、不出菌包；
- 菌包仍用 `stage=0` 空包 → `1` 走菌 → `2` 出菇 → `3` 枯竭；孢子来自原版 brown/red mushroom；
- 温湿度复用温室/地窖；废菌包→堆肥。
- **被破坏/采收后由随机刻重新长回**，不是一次性 worldgen；自然专用 4 种只靠这条刷新。
| # | 物种 | 形态/类型 | 载体 | 流程 | 加工/出口 | 目标产率 |
|---:|---|---|---|---|---|---|
| 1 | `oyster` | 平菇（食用） | 菌包 | 孢子接种→走菌→出菇→采 | 鲜食/干燥/汤 | 2–4/潮；2–3 潮 |
| 2 | `shiitake` | 香菇（食用） | 菌包 | 孢子接种→走菌→出菇→采 | 鲜食/干燥/汤/调味 | 2–4/潮；2–3 潮 |
| 3 | `button` | 双孢菇（食用） | 菌包 | 孢子接种→走菌→出菇→采 | 鲜食/干燥/汤 | 2–4/潮；2–3 潮 |
| 4 | `enoki` | 金针菇（食用） | 菌包 | 孢子接种→走菌→出菇→采 | 鲜食/汤/腌渍 | 2–4/潮；2–3 潮 |
| 5 | `wood_ear` | 木耳（食用） | 菌包 | 孢子接种→走菌→出菇→采 | 干燥/泡发/炒制 | 2–4/潮；2–3 潮 |
| 6 | `reishi` | 灵芝（药用） | 菌包 | 孢子接种→走菌→出菇→采 | 干燥→切片→煎煮/研磨 | 1–2/潮；2–3 潮 |
| 7 | `lions_mane` | 猴头菇（药用/食用） | 菌包 | 孢子接种→走菌→出菇→采 | 鲜食/干燥/煎煮 | 1–2/潮；2–3 潮 |
| 8 | `maitake` | 舞茸（食用/药用） | 菌包/腐木 | 孢子接种→走菌→出菇→采 | 鲜食/干燥/煎煮 | 2–4/潮；2–3 潮 |
| 9 | `king_oyster` | 杏鲍菇（食用） | 菌包 | 孢子接种→走菌→出菇→采 | 鲜食/烤/干制 | 2–3/潮；2–3 潮 |
| 10 | `shimeji` | 蟹味菇（食用） | 菌包 | 孢子接种→走菌→出菇→采 | 鲜食/汤/干制 | 2–4/潮；2–3 潮 |
| 11 | `porcini` | 牛肝菌（食用） | **无（仅野生）** | 自然生成/随机刷新→采 | 鲜食/干燥/调味 | 1–2/季 |
| 12 | `morel` | 羊肚菌（食用） | **无（仅野生）** | 自然生成/随机刷新→采 | 鲜食/干燥/调味 | 1–2/季 |
| 13 | `chanterelle` | 鸡油菌（食用） | **无（仅野生）** | 自然生成/随机刷新→采 | 鲜食/干燥/调味 | 1–2/季 |
| 14 | `black_truffle` | 黑松露（食用/药用） | **无（仅野生）** | 自然生成/随机刷新→采 | 鲜食/研磨/油浸 | 1–2/季；极低产 |
| 15 | `turkey_tail` | 云芝（药用） | 菌包/腐木 | 孢子接种→走菌→出菇→采 | 干燥→煎煮/研磨 | 1–2/潮；2–3 潮 |
### 9.4 已有乔木坚果：新叶状态与季节挂果

已有乔木的坚果不另造一棵树，而是在**原树叶方块上增加新的叶子状态**，按 TFC 季节挂果并随机掉落。

| 乔木 | 坚果 | 新增叶状态 | 挂果季节（TFC 日历） | 自然掉落 |
|---|---|---|---|---|
| oak | acorn | `nut_state=0/1/2/3`（无/花/青/熟） | 夏末—秋 | 成熟后随机刻掉落 1–2 |
| chestnut | chestnut | 同上 | 夏末—秋 | 成熟后随机刻掉落 1–2 |
| pine | pine_nut | 同上 | 夏—秋 | 松塔成熟后掉落 |
| hickory | hickory_nut | 同上 | 夏末—秋 | 成熟后随机刻掉落 1–2 |
| beech | beechnut | 同上 | 夏末—秋 | 成熟后随机刻掉落 1–2 |
| almond | almond | 同上（A 树覆盖） | 春—夏 | 成熟后随机刻掉落 |
| hazelnut | hazelnut | 同上（A 树覆盖） | 夏末—秋 | 成熟后随机刻掉落 |
| pecan | pecan | 同上（A 树覆盖） | 夏末—秋 | 成熟后随机刻掉落 |
| walnut | walnut | 同上（A 树覆盖） | 夏末—秋 | 成熟后随机刻掉落 |
| hardy_chestnut / chinquapin | chestnut | 同上（AFC 树覆盖） | 夏末—秋 | 成熟后随机刻掉落 |

**实现要求**：
- 新增叶状态属性 `nut_state`（或等价 `fruiting` 属性），并覆盖树叶 blockstate/model 的全部组合，不能只覆盖默认态；
- 用 TFC 季节/日历驱动挂果；挂果期叶模型出现坚果 overlay，非挂果期隐藏；
- 成熟后随机刻概率掉落坚果，玩家也可右键采收；采收/掉落后退回无果态；
- TFC/A/AFC 已有树叶方块通过 B 的 block/mixin **新增叶状态并覆盖全部 blockstate/model 组合**，**不另建重复树**；旧存档缺省 `nut_state=0`；
- 坚果自然掉落在树下生成物品实体，可被水冲/被动物吃掉，避免只靠手动右键。

### 9.5 新增内容总量
- 20 香料 + 8 坚果 + 15 蘑菇 = **43 条新增记录**；
- 香料是 Firmalife 搁置项接管/重建 + 新增；坚果是 B 新物品/树产 + 已有树叶状态；蘑菇含野生生成/刷新与可栽培 11/自然专用 4；
- 全部进入 P1/P2 批次，不混入 A 87/TFC 29 的统计；43 条全部必须逐条有产物/副产物/加工/出口。

## 10. TFC 10 灌木
| 物种 | 主产品 | 繁殖 | 初步加工/出口 | 育苗 |
|---|---|---|---|---|
| `blackberry` | 聚合果 | 扦插/压条 | 果酱、果干、汁 | 扦插→育苗→移栽 |
| `blueberry` | 浆果 | 种子/扦插 | 果酱、果干、汁 | 扦插→育苗→移栽 |
| `bunchberry` | 浆果 | 种子/分株 | 果酱、果干 | 分株/种子→育苗→移栽 |
| `cloudberry` | 浆果 | 种子/分株 | 果酱、果干 | 分株→育苗→移栽 |
| `cranberry` | 浆果 | 扦插/匍匐茎 | 果酱、果干、汁 | 匍匐茎→育苗→定植 |
| `elderberry` | 浆果 | 种子/扦插 | 果酱、糖浆、汁 | 扦插→育苗→移栽 |
| `gooseberry` | 浆果 | 种子/扦插 | 果酱、果干 | 扦插→育苗→移栽 |
| `raspberry` | 聚合果 | 分株/扦插 | 果酱、果干、汁 | 分株→育苗→移栽 |
| `snowberry` | 浆果 | 种子/分株 | 果酱、果干 | 分株→育苗→移栽 |
| `wintergreen` | 浆果 | 种子/分株 | 果酱、干果 | 分株→育苗→移栽 |

草莓已经由 A 迁移为普通作物，不在 B 的 10 种 TFC 灌木重做范围内；TFC 草莓灌木的世界生成已由 A 的标签 remove 关闭。10 种灌木不得改 A 已有标签；覆盖 TFC 标签只能追加；蜂蜜 `buzzing_leaves` 兼容不能破坏。

## 11. 修改范围清单
| 层 | 修改内容 | 备注 |
|---|---|---|
| 数据 | 159 条记录/产量/产物映射；A 87、TFC 29、B 43 分开 | TFC 29 的种植/收获/掉落由 B 覆盖；旧 raw 作回退基线 |
| 物品 | 处理种子、苗、扦插枝、种薯/种球、孢子/菌种 | 需定 B 新 ID 或 DataComponent |
| 副产物 | `wet_grass`；`grain_bundle/<crop>`；每作物 `crop_waste/<crop>`；坚果壳/菌渣另计 | 不设通用废枝叶；湿草来自谷物捆脱粒/野草/未成熟补偿；堆肥按作物分档 |
| 方块 | 育苗盘/苗床、种子干燥架、筛选台、浸种/催芽容器、移栽载体、菌包 | 菌包 4 stage；苗床需 BE |
| 行为 | 六环节、九工序、农艺操作、留种循环、蘑菇走菌/出菇 | `in_world` + DataComponent + 随机刻 |
| 加工 | 27 个 profile 的初加工与副产物出口 | 每个 profile 至少 1 完整链 |
| 香料/坚果/蘑菇 | 20+8+15 新内容，独立 ID/标签/手册 | 香料接管 Firmalife 需兼容 |
| TFC | **29 作物替换/覆盖种植+收获+掉落** + **10 灌木替换采收/再生** | 先解决 A cabbage 所有权/EUPL；旧存档迁移/回退 |
| 验收 | 159 条记录逐条检查 | 不以静态/贴图替代实机 |

## 12. 实施批次与验收
| 批次 | 内容 | 验收 |
|---|---|---|
| P0 | 数据矩阵/ID/标签/产量带落表；选 1 物种打通全链 | 字段完整、无死端 |
| P1 | 种子处理+育苗+移栽+缓苗；`wet_grass` 野草/谷物捆脱粒/干燥；逐作物 `crop_waste` 绿色堆肥标签；香料/坚果开始 | 六环节可执行、seedBack 达标 |
| P2 | 各 profile 初加工；蘑菇菌包；坚果去壳/榨油；香料干燥/研磨；潮湿草晒干/废枝叶堆肥验证 | 每 profile 至少 1 完整链 |
| P3 | 159 条逐作物覆盖与产量实测调参 | 全记录通过验收 |
| P4 | TFC 29 种植/收获/掉落覆盖 + TFC 10 灌木采收/再生覆盖 | 覆盖 TFC 原流程；存档迁移/回退方案同步验证 |

每记录验收：主产品/副产品、繁殖、育苗/种子处理、初步加工、出口、原掉落不减少、20 次收获均值在产量带、与同类无数量级失衡。

## 13. 未决问题与解决方案

完整分析与决定见 [292 未决问题决策](292-crop-open-issues-decisions-20261028.md)。摘要：

| # | 决定 |
|---:|---|
| 1 | A 以实际 87 种为准，旧文档 86 废弃 |
| 2 | A 87/B 43 全链；TFC 29 **替换/覆盖种植+收获+掉落**；TFC 10 灌木**替换采收/再生** |
| 3 | 育苗/移栽用 B 自有方块 + `in_world`，不改 TFC |
| 4 | 种子处理用 DataComponent，不新增 116 个处理种子物品 |
| 5 | **TFC/A raw 都允许被 B 覆盖**；TFC 29 用 bundle/湿草/新叶状态替换原流程；旧 raw 作回退基线 |
| 6 | A 删除 6 个 TFC cabbage 模型，B 接管 29 作物 TFC 资源；补 EUPL 通知 |
| 7 | 双主产共用一个 raw ledger，不重复计 raw |
| 8 | 20 香料分草本/灌木/乔木/攀援藤/球茎五类 |
| 9 | 15 蘑菇全部世界生成+可刷新；可栽培 11，自然专用 4（porcini/morel/chanterelle/black_truffle） |
| 10 | 已有乔木加 `nut_state` 叶状态、按季节挂果并随机掉落；3 新坚果用新 B 树 |
| 11 | A 10 + TFC 6 谷物全部 bundle→脱粒→wet_grass；TFC 原收获/raw 由 B 覆盖 |
| 12 | 废枝叶按实际加工；仅 102 条有 `crop_waste`，其余走 straw/cake/shives/shell/spent substrate |
| 13 | TFC 10 灌木替换采收/再生流程；草莓已是 A 普通作物 |

## 14. 来源文档

- `287-crop-redo-requirements-20261028.md`：原始要求、29 作物/10 灌木、当前缺口；草莓已由 A 迁移为普通作物。
- `288-crop-production-and-cultivation-chain-20261028.md`：86 种生产链、六环节/九工序。
- `289-crop-master-plan-20261028.md`：116 条逐作物矩阵。
- `290-crop-flow-and-yield-balance-20261028.md`：27 profile、产率/平衡。
- `archive/117-agriculture-redesign-plan.md` §6.1（香料/蘑菇/坚果搁置项解禁）、§6.8（六环节）、§9.1（新增/接管清单）。
