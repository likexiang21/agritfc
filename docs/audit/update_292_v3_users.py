from pathlib import Path

p = Path("mod_rebuild/docs/292-crop-open-issues-decisions-20261028.md")
t = p.read_text(encoding="utf-8")

t = t.replace(
"| 2 | A/TFC/B/灌木的范围 | **分四层**：A 87 全链；B 43 全链；TFC 29 资源覆盖+加工；TFC 10 灌木资源覆盖+采收/加工 | TFC 作物不做六环节行为改造；A/B 作物做完整六环节 |",
"| 2 | A/TFC/B/灌木的范围 | A 87 全链；B 43 全链；**TFC 29 替换/覆盖种植+收获+掉落**；TFC 10 灌木替换采收/再生 | TFC 不再做资源旁路；TFC 29 走 B 的种植/收获行为 |")
t = t.replace(
"| 5 | TFC/A raw 是否调整 | **P1 一律不改 raw**；TFC raw 永久保持；A raw 调整留作可选数据包 | 先靠加工转化率、副产物、种子返还平衡；不破坏存档/掉落 |",
"| 5 | TFC/A raw 是否调整 | **TFC/A raw 都允许被 B 覆盖**；TFC 29 用 bundle/湿草/新叶状态替换原流程；旧 raw 只作回退基线 | 不再绕过 TFC；存档迁移与回退方案必须同步做 |")
t = t.replace(
"| 9 | 15 蘑菇的载体与效果 | **3 类载体**：菌包 11、菌根树根 3、林下菌床 1；统一 4 stage 菌包 | 菌根类不按普通菌包；药用效果分级并设上限 |",
"| 9 | 15 蘑菇的世界生成/刷新与栽培 | **全部 15 种世界自然生成并随机刷新**；可栽培 11（菌包/腐木），**自然专用 4**（porcini/morel/chanterelle/black_truffle）禁止菌包 | 野生蘑菇学 TFC `PlantBlock`/`SeasonalPlantBlock` 随机刻刷新；自然专用只可采 |")
t = t.replace(
"| 10 | 8 坚果的挂树方式 | **5 种挂已有树**（oak/chestnut/pine/hickory/beech）+ **3 种新 B 树**（pistachio/cashew/macadamia） | 不新增重复的 A/AFC 坚果；挂树坚果走已有树叶/枝干接口 |",
"| 10 | 已有乔木坚果的叶状态/掉落 | 已有树加 **`nut_state` 叶状态**（无/花/青/熟），按 TFC 季节挂果、成熟随机掉落；**5 种挂已有树** + **3 种新 B 树**（pistachio/cashew/macadamia） | 不另造重复树；覆盖树叶全部 blockstate/model；旧存档默认无果 |")
t = t.replace(
"| 11 | 潮湿草与谷物捆 | **A 10 种长秆谷物先做 bundle→脱粒→wet_grass**；TFC 6 种默认保持 raw，不启用 bundle；野草/未成熟补偿保留 | TFC 兼容优先；TFC bundle 作为可选数据包，后期评估 |",
"| 11 | 潮湿草与谷物捆 | **A 10 + TFC 6 长秆谷物全部 bundle→脱粒→wet_grass**；TFC 原收获/raw 由 B 覆盖；野草/未成熟补偿保留 | 湿草是 B 新物品 `tfcagricultureplus:wet_grass`，不是 TFC 已有物品 |")
t = t.replace(
"| 13 | TFC 10 灌木是否做六环节 | **只做资源覆盖 + 采收/加工**；不做育苗/移栽/农艺 | 避免改 TFC 方块；草莓已是 A 普通作物，不列入 |",
"| 13 | TFC 10 灌木是否做六环节 | **替换采收/再生流程 + 资源覆盖**；不做育苗/移栽/农艺 | 覆盖 TFC 灌木原采收；草莓已是 A 普通作物，不列入 |")

# Section 2 analysis/table
t = t.replace(
"**分析**：把 A 87、TFC 29、TFC 10 灌木、B 43 全部按“同一套六环节”做，会强迫改 TFC 方块行为，和“TFC 资源覆盖、存档安全”冲突。",
"**分析**：A 87、B 43、TFC 29 都要求有生产/培育闭环；TFC 29 不能只换贴图或绕过原流程，必须覆盖种植/收获/掉落。")
t = t.replace("| TFC 29 | TFC 作物 | 只做 B 加工/产物 | 只做种子处理/收获，不做移栽/农艺 |",
              "| TFC 29 | TFC 作物 | **替换/覆盖** | **完整六环节 + B 收获/掉落** |")
t = t.replace("| TFC 10 灌木 | TFC 灌木 | 采收/加工 | 不做六环节 |",
              "| TFC 10 灌木 | TFC 灌木 | **替换采收/再生** | 不做六环节 |")

# Section 5
t = t.replace("**分析**：TFC 29 的 raw 改变会破坏现有存档/平衡；A 的 raw 也统一 6–10，应先靠加工转化率平衡。",
              "**分析**：用户要求替换 TFC 原种植/收获流程，不允许绕过；因此 TFC/A raw 都可被覆盖，但必须做存档迁移与回退。")
t = t.replace("- P1 不改任何 raw；\n- TFC raw 永久保持；\n- A raw 只做可选数据包；",
              "- TFC 29 raw 由 B 覆盖：bundle/湿草/新叶状态替换原流程；\n- A 87 raw 同步按 profile 调整；\n- 旧 raw/旧收获路径保留为回退基线；\n- 存档迁移（已有作物/树叶/掉落）必须与覆盖同批验证。")

# Section 6 cabbage resource line
t = t.replace("2. B 建立全部 29 作物的 TFC 资源覆盖；",
              "2. B 建立全部 29 作物的 TFC 资源覆盖，并接管其种植/收获/掉落；")

# Section 9 replace block content
start = t.find("### 9. 15 蘑菇")
end = t.find("### 10. 坚果挂树")
if start < 0 or end < 0:
    raise SystemExit("292 mushroom section missing")
new9 = """### 9. 15 蘑菇：世界生成、刷新与栽培边界

**分析**：蘑菇不能只是菌包系统；要像 TFC 野生植物一样在世界中生成并可持续刷新。部分蘑菇在现实中无法人工栽培，必须只能自然获得。

**决定**：

- **全部 15 种**都有世界自然生成 + 随机刻刷新，学习 TFC `PlantBlock`/`SeasonalPlantBlock` 的扩散/季节/气候/休眠；
- **可栽培 11 种**：oyster · shiitake · button · enoki · wood_ear · reishi · lions_mane · maitake · king_oyster · shimeji · turkey_tail；
- **只能自然刷新、不可培育 4 种**：porcini · morel · chanterelle · black_truffle；**禁止菌包配方**；
- 野生蘑菇方块按 biome/林地/树根/腐木生成；有 worldgen configured/placed feature + biome tag；
- 自然专用 4 种只用野生方块；菌包只对可栽培 11 种开放；
- 菌包仍为 `stage=0` 空包 → `1` 走菌 → `2` 出菇 → `3` 枯竭；废菌包 → 堆肥；
- 药用蘑菇效果分级并设上限。

"""
t = t[:start] + new9 + t[end:]

# Section 10 replace block
start = t.find("### 10. 坚果挂树")
end = t.find("### 11. 潮湿草与谷物捆")
if start < 0 or end < 0:
    raise SystemExit("292 nut section missing")
new10 = """### 10. 已有乔木坚果：新叶状态与随机掉落

**分析**：已有乔木不需要另造树；但需要让特定季节出现坚果，并让坚果自然掉落，而不是只在合成/右键时凭空产生。

**决定**：

- 在已有树叶方块增加 **`nut_state`** 叶状态：`0=无 / 1=花 / 2=青 / 3=熟`；
- 用 TFC 季节/日历驱动：夏季—秋季进入挂果，成熟后随机刻掉落坚果；
- 挂果时叶模型增加坚果 overlay；非挂果期隐藏；
- 玩家可右键采收；自然掉落也会在树下生成坚果物品实体；
- 覆盖树叶 blockstate/model 的**全部组合**，旧存档缺省 `nut_state=0`；
- 已有树：oak/acorn · chestnut/chestnut · pine/pine_nut · hickory/hickory_nut · beech/beechnut；A 的 almond/hazelnut/pecan/walnut；AFC hardy_chestnut/chinquapin 同样覆盖；
- 新树仅用于 pistachio/cashew/macadamia，不重复 A/AFC 已有坚果。

"""
t = t[:start] + new10 + t[end:]

# Section 11 replace block
start = t.find("### 11. 潮湿草与谷物捆")
end = t.find("### 12. 废枝叶")
if start < 0 or end < 0:
    raise SystemExit("292 wet section missing")
new11 = """### 11. 潮湿草与谷物捆

**分析**：用户要求湿草是 B 新物品，并且湿草要来自加工流程；不允许绕过 TFC 原收获。

**决定**：

- 新物品 **`tfcagricultureplus:wet_grass`** —— B 新增，不是 TFC 已有物品；
- **A 10 + TFC 6 长秆谷物**全部走：
  `成熟收获 → grain_bundle/<crop> → 脱粒 → 谷粒 + wet_grass → 1:1 晒干 tfc:straw`；
- TFC 6 种（barley/oat/rice/rye/wheat/maize）也覆盖原收获，不再保留 TFC 直接掉谷粒/秸秆的路径；
- 野草 13 种：保留剪刀掉落，增加湿草分支；未成熟作物破坏用 `extra_products` 补湿草；
- 非 bundle：buckwheat / amaranth / quinoa；sugarcane 不属于谷物捆；
- 旧 raw 只作回退基线。

"""
t = t[:start] + new11 + t[end:]

# Final recommendation
t = t.replace("先做 **A 10 谷物 bundle + 101 个 crop_waste + 10 个 TFC 灌木资源覆盖** 作为 P1/P2，不碰 TFC raw；TFC 29 作物/10 灌木只做资源与加工；A/B 作物做完整六环节。这样能同时满足“加工关联”“具体作物具体实现”“TFC 兼容”三个约束。",
"先做 **A 10 + TFC 6 谷物 bundle→wet_grass、101 个实际 crop_waste、TFC 29 种植/收获覆盖、TFC 10 灌木采收/再生覆盖**；湿草用 B 新物品 `wet_grass`，坚果用 `nut_state` 叶状态，蘑菇全部世界生成、自然专用 4 种禁止菌包。这样同时满足“加工关联”“具体作物具体实现”“不绕过 TFC”三个约束。")

p.write_text(t, encoding="utf-8")
print("292 updated for user directives")
