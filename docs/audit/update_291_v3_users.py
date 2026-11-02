from pathlib import Path

p = Path("mod_rebuild/docs/291-crop-system-complete-modification-20261028.md")
t = p.read_text(encoding="utf-8")

# --- stats ---
t = t.replace("| 副产物物品 | 1 + 10 + 101 | `wet_grass`（1）+ `grain_bundle/<crop>`（10，A 谷物）+ `crop_waste/<crop>`（101，按实际副产）；坚果壳/菌渣另算 |",
              "| 副产物物品 | 1 + 16 + 101 | `tfcagricultureplus:wet_grass`（1，B 新物品）+ `grain_bundle/<crop>`（16，A 10 + TFC 6）+ `crop_waste/<crop>`（101，按实际副产）；坚果壳/菌渣另算 |")

# --- TFC flow replacement statements ---
t = t.replace("- TFC 29 作物仍是原版十字模型与统一 6–10 掉落；",
              "- TFC 29 作物仍是原版十字模型与统一 6–10 掉落；**本次要求替换/覆盖其种植与收获流程，不再做资源旁路。**")
t = t.replace("3. **产量按产率平衡**：TFC raw 保持原值，A raw 可调但需单批评审；优先调加工转化率、副产物、种子返还。",
              "3. **产量按产率平衡**：TFC 29 与 A 87 的 raw **允许被 B 覆盖**；用 bundle/湿草/新叶状态替换原流程，旧值只作回退基线；TFC 不再绕过。")
t = t.replace("- TFC 29 raw 保持原值；A 87 raw 可调但需单批评审；",
              "- **TFC 29 raw 由 B 覆盖**（bundle/湿草/新叶状态）；A 87 raw 同样可调；旧值只作回退基线；")
t = t.replace("| 数据 | 159 条记录/产量/产物映射；A 87、TFC 29、B 43 分开 | TFC raw 保持原值 |",
              "| 数据 | 159 条记录/产量/产物映射；A 87、TFC 29、B 43 分开 | TFC 29 的种植/收获/掉落由 B 覆盖；旧 raw 作回退基线 |")
t = t.replace("| P4 | TFC 29+10 灌木资源层接入 | 不改 TFC raw；存档安全 |",
              "| P4 | TFC 29 种植/收获/掉落覆盖 + TFC 10 灌木接入 | 覆盖 TFC 原流程；存档迁移/回退方案同步验证 |")
t = t.replace("| 2 | 分四层：A 87/B 43 全链；TFC 29 资源+加工；TFC 10 灌木资源+采收/加工 |",
              "| 2 | A 87/B 43 全链；TFC 29 **替换/覆盖种植+收获+掉落**；TFC 10 灌木资源+采收/加工 |")
t = t.replace("| 5 | P1 不改 TFC/A raw；TFC raw 永久保持；A raw 调整仅可选数据包 |",
              "| 5 | **TFC/A raw 都允许被 B 覆盖**；TFC 29 用 bundle/湿草/新叶状态替换原流程；旧 raw 作回退基线 |")
t = t.replace("| 11 | A 10 谷物 bundle→wet_grass；TFC 6 谷物默认 raw 不变，bundle 可选 |",
              "| 11 | A 10 + TFC 6 谷物全部 bundle→脱粒→wet_grass；不再保留 TFC 原 raw 路径 |")

# --- wet grass item explicit new B item ---
t = t.replace("#### 4.1.1 潮湿草 `wet_grass`\n",
              "#### 4.1.1 潮湿草 `wet_grass`：B 新物品\n")
t = t.replace("| 来源 1 | **A 的 10 种长秆谷物**成熟收获 → `grain_bundle/<crop>` → 脱粒 → 谷粒 + `wet_grass`；这是主路径（见 4.1.3） |",
              "| 物品 | **`tfcagricultureplus:wet_grass`** —— B 新增物品，**不是 TFC 已有物品**；需模型/贴图/语言/标签 |\n"
              "| 来源 1 | **A 10 + TFC 6 长秆谷物**成熟收获 → `grain_bundle/<crop>` → 脱粒 → 谷粒 + `wet_grass`；这是主路径（见 4.1.3） |")
t = t.replace("| 干燥 | `wet_grass` → **TFC `tfc:straw`（干草/秸秆）**，走晒架/Firmalife drying mat 或 TFC heating；1:1 干燥，不新增第二条 straw 链 |",
              "| 干燥 | `tfcagricultureplus:wet_grass` → **TFC `tfc:straw`（干草/秸秆）**，走晒架/Firmalife drying mat 或 TFC heating；1:1 干燥 |")

# --- bundle TFC 6 rows and update note ---
t = t.replace("**TFC 6 种谷物**（barley/oat/rice/rye/wheat/maize）：P1 **保持 TFC 原 raw，不启用 bundle**；湿草仅来自野草收割/未成熟补偿。bundle 版本列为可选数据包，P2 后评估。",
              "**TFC 6 种谷物**（barley/oat/rice/rye/wheat/maize）：**同样走 bundle→脱粒→wet_grass**，覆盖 TFC 原有直接掉谷粒/秸秆的收获流程；不再保留 TFC 原 raw 路径。")
# Insert TFC bundle rows before non-grain line.
needle = "非谷物捆：`buckwheat` / `amaranth` / `quinoa`；TFC `sugarcane` 不属于谷物捆。"
tfc_rows = "\n".join([
    f"| `{crop}` | TFC | `tfcagricultureplus:grain_bundle/{crop}` | 成熟收获 → 1–2 捆 + 种子 | 脱粒 → 谷粒 + 1–2 `tfcagricultureplus:wet_grass` | 1:1 晒干 → `tfc:straw` | 覆盖 TFC 原收获 |"
    for crop in ["barley", "oat", "rice", "rye", "wheat", "maize"]
])
t = t.replace(needle, tfc_rows + "\n\n" + needle)

# --- mushrooms: natural generation / respawn / natural-only ---
t = t.replace("### 9.3 蘑菇栽培 15 种\n菌包：`stage=0` 空包 → `1` 走菌 → `2` 出菇 → `3` 枯竭；孢子来自 vanilla brown/red mushroom；温湿度复用温室/地窖；收获后废菌包→堆肥。",
"""### 9.3 蘑菇 15 种：野生生成、刷新与栽培边界
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
- 温湿度复用温室/地窖；废菌包→堆肥。""")

# --- nut leaf state section inserted before 9.4 totals ---
needle = "### 9.4 新增内容总量"
leaf = r'''### 9.4 已有乔木坚果：新叶状态与季节挂果\n
已有乔木的坚果不另造一棵树，而是在**原树叶方块上增加新的叶子状态**，按 TFC 季节挂果并随机掉落。\n
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
- TFC/A/AFC 已有树叶方块通过 B 的 block/mixin 扩展实现，**不另建重复树**；存档旧叶状态给默认值；
- 坚果自然掉落在树下生成物品实体，可被水冲/被动物吃掉，避免只靠手动右键。

'''
t = t.replace(needle, leaf + "### 9.5 新增内容总量")

# --- decision table updates 9/10/11 ---
t = t.replace("| 9 | 15 蘑菇分菌包 11 / 菌根树根 3 / 林下菌床 1；菌包 4 stage |",
              "| 9 | 15 蘑菇全部世界生成+可刷新；可栽培 11，自然专用 4（porcini/morel/chanterelle/black_truffle） |")
t = t.replace("| 10 | 5 坚果挂已有树，3 坚果用新 B 树；不重复 A/AFC 坚果 |",
              "| 10 | 已有乔木加 `nut_state` 叶状态、按季节挂果并随机掉落；3 新坚果用新 B 树 |")
t = t.replace("| 11 | A 10 + TFC 6 谷物全部 bundle→脱粒→wet_grass；不再保留 TFC 原 raw 路径 |",
              "| 11 | A 10 + TFC 6 谷物全部 bundle→脱粒→wet_grass；TFC 原收获/raw 由 B 覆盖 |")

p.write_text(t, encoding="utf-8")
print("291 updated for new wet grass/TFC override/mushrooms/nut leaf states")
