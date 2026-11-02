from pathlib import Path
import re

OUT = Path("mod_rebuild/docs/291-crop-system-complete-modification-20261028.md")
A_DOC = Path("mod_rebuild/docs/289-crop-master-plan-20261028.md")
B_DOC = Path("mod_rebuild/docs/290-crop-flow-and-yield-balance-20261028.md")


def parse(path):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|([^|]*)\|(.*)\|\s*$", line)
        if not m:
            continue
        crop, sg = m.group(2), m.group(3).strip()
        cells = [x.strip() for x in m.group(4).split("|") if x.strip()]
        rows.append((crop, sg, cells))
    return rows


r289 = parse(A_DOC)
r290 = parse(B_DOC)
base, flow = {}, {}
for crop, sg, cells in r289:
    if len(cells) != 7:
        raise SystemExit(f"289 {crop}: {len(cells)}")
    main, by, prop, nursery, process, outlet, batch = cells
    base[(crop, sg)] = dict(crop=crop, sg=sg, main=main, by=by, prop=prop,
                            nursery=nursery, process=process, outlet=outlet, batch=batch)
for crop, sg, cells in r290:
    if len(cells) != 7:
        raise SystemExit(f"290 {crop}: {len(cells)}")
    flow_name, baseline, raw, seed, processed, by_yield, key = cells
    flow[(crop, sg)] = dict(flow=flow_name.strip("` "), baseline=baseline, raw=raw,
                            seed=seed, processed=processed, by_yield=by_yield, key=key)
if len(base) != 116 or len(flow) != 116 or set(base) != set(flow):
    raise SystemExit("matrix mismatch")
order = [(c, s) for c, s, _ in r289]

spices = [
    ("basil", "草本", "叶", "茎叶渣", "种子", "采种→育苗→移栽", "鲜叶→干燥→研磨", "调料、沙拉、汤", "2–4 株；叶 2–4 份"),
    ("bay_laurel", "灌木/小乔木", "叶", "枝条", "种子/扦插", "育苗→移栽", "采叶→阴干→研磨", "调料、汤、炖菜", "2–3 株；叶 3–6 份"),
    ("cardamom", "根茎草本", "果荚/种子", "茎叶渣", "根茎分株", "分株→育苗→定植", "采果→干燥→脱壳→研磨", "调料、甜点、咖喱", "2–4 株；荚 1–2 份"),
    ("cilantro", "草本", "叶/种子", "茎叶渣", "种子", "采种→育苗/直播", "鲜叶/种子→干燥→研磨", "调料、沙拉、汤", "2–4 株；叶/籽 2–3 份"),
    ("cumin", "草本", "种子", "茎秆", "种子", "采种→直播", "采种→干燥→研磨", "调料、咖喱、烘焙", "2–3 株；籽 1–2 份"),
    ("oregano", "草本", "叶", "茎叶渣", "种子/分株", "育苗/分株→移栽", "采叶→干燥→研磨", "调料、披萨、汤", "2–4 株；叶 2–3 份"),
    ("pimento", "小乔木", "浆果/干果", "枝叶", "种子/扦插", "育苗→移栽", "采果→干燥→研磨", "香料、腌渍、甜点", "2–3 株；果 1–2 份"),
    ("vanilla", "攀援兰", "果荚", "藤蔓", "扦插", "母株→扦插→搭架→定植", "采荚→杀青→发酵→干燥", "香草精、甜点", "1–2 株；荚 1–2 份"),
    ("black_pepper", "攀援藤", "胡椒粒", "藤蔓/叶", "扦插/种子", "母株→扦插→搭架→定植", "采果→浸泡→去皮→干燥→研磨", "黑胡椒/白胡椒、调料", "1–2 株；椒 1–2 份"),
    ("cinnamon", "乔木", "树皮", "枝叶", "种子/萌蘖", "育苗→定植；萌蘖更新", "剥皮→阴干→卷曲→研磨", "桂皮、肉桂粉、甜点", "1–2 株；皮 1–2 份"),
    ("clove", "小乔木", "花蕾", "枝叶", "种子/扦插", "育苗→定植", "采花蕾→干燥", "丁香、腌渍、甜点", "1–2 株；蕾 0.5–1 份"),
    ("nutmeg", "乔木", "种仁/假种皮", "果壳/果肉", "种子/嫁接", "育苗→定植", "采果→去壳→干燥→研磨", "肉豆蔻/肉豆蔻衣、甜点", "1–2 株；仁 1 份"),
    ("saffron", "球茎草本", "柱头", "花瓣/球茎", "球茎分株", "球茎→分级→定植", "采花→取柱头→阴干", "藏红花、调味、染料", "1–2 球；柱头 0.2–0.5 份"),
    ("star_anise", "乔木", "八角果", "枝叶", "种子/扦插", "育苗→定植", "采果→干燥", "八角、卤味、香料", "1–2 株；果 1–2 份"),
    ("rosemary", "灌木", "叶", "枝条", "扦插/种子", "扦插→育苗→定植", "采叶→干燥→研磨", "迷迭香、烤肉、调料", "2–4 株；叶 2–3 份"),
    ("thyme", "草本/小灌木", "叶", "茎叶渣", "种子/分株", "育苗/分株→定植", "采叶→干燥→研磨", "百里香、汤、调料", "2–4 株；叶 2–3 份"),
    ("sage", "草本/小灌木", "叶", "茎叶渣", "种子/扦插", "育苗/扦插→定植", "采叶→干燥→研磨", "鼠尾草、烤肉、调料", "2–4 株；叶 2–3 份"),
    ("dill", "草本", "叶/种子", "茎秆", "种子", "采种→直播/育苗", "叶/种子→干燥→研磨", "莳萝、腌渍、调料", "2–4 株；叶/籽 2–3 份"),
    ("fennel", "草本", "种子/叶/球茎", "茎叶渣", "种子", "采种→育苗→移栽", "种子/叶→干燥→研磨；球茎鲜食", "茴香、调料、蔬菜", "2–4 株；籽 1–2 份"),
    ("mustard", "草本", "种子/叶", "茎叶渣", "种子", "采种→直播", "种子→研磨→制酱；叶鲜食/腌渍", "芥末、芥菜、腌菜", "2–4 株；籽 1–2 份"),
]

nuts = [
    ("acorn（橡子）", "B 新增（挂 oak）", "橡子", "壳斗/壳", "树上结果；树苗繁殖", "成熟→落果/采收→去壳", "干燥→去涩→烤/磨粉/榨油", "食物、饲料、油", "4–8 个/树；壳 2–4"),
    ("chestnut（栗子）", "B 新增（挂 chestnut）", "栗子", "总苞/壳", "树上结果；树苗繁殖", "成熟→落果/采收→去壳", "干燥→去壳→煮/烤/磨粉", "食物、饲料、淀粉", "4–8 个/树；壳 2–4"),
    ("pistachio", "B 新增（乔木）", "开心果", "壳", "种子/嫁接", "育苗→定植", "去壳→干燥→烤/磨粉", "坚果、油、甜点", "4–8 个/树；壳 2–4"),
    ("cashew", "B 新增（乔木）", "腰果", "腰果苹果/壳", "种子/嫁接", "育苗→定植", "去壳→烘烤→去皮", "坚果、腰果酱、油", "4–6 个/树；苹果副产 1–2"),
    ("macadamia", "B 新增（乔木）", "夏威夷果", "壳", "种子/嫁接", "育苗→定植", "去壳→干燥→烤/榨油", "坚果、油、甜点", "4–8 个/树；壳 2–4"),
    ("pine_nut", "B 新增（挂 pine）", "松子", "松塔/壳", "树上结果；松苗繁殖", "成熟→采松塔→取籽", "去壳→干燥→烤/榨油", "坚果、油、 pesto", "2–4 松塔；松子 1–2 份"),
    ("hickory_nut", "B 新增（挂 hickory）", "山核桃", "壳", "树上结果；树苗繁殖", "成熟→落果→去壳", "干燥→去壳→烤/磨粉/榨油", "坚果、油、饲料", "4–8 个/树；壳 2–4"),
    ("beechnut", "B 新增（挂 beech）", "山毛榉坚果", "壳/总苞", "树上结果；树苗繁殖", "成熟→采收→去壳", "干燥→去壳→烤/磨粉/榨油", "坚果、油、饲料", "4–8 个/树；壳 2–4"),
]

existing_nuts = [
    ("almond", "A 已有", "杏仁", "壳", "果树/树苗", "开花结果→采收", "去壳→烤/磨粉/榨油", "食物、油、甜点"),
    ("hazelnut", "A 已有", "榛子", "壳", "果树/树苗", "结果→采收", "去壳→烤/磨粉/榨油", "食物、油、甜点"),
    ("pecan", "A 已有", "碧根果", "壳", "果树/树苗", "结果→采收", "去壳→烤/磨粉/榨油", "食物、油、甜点"),
    ("walnut", "A 已有", "核桃", "壳", "果树/树苗", "结果→采收", "去壳→烤/磨粉/榨油", "食物、油、甜点"),
    ("hardy_chestnut", "AFC 已有", "栗子", "壳", "果树/树苗", "结果→采收", "去壳→煮/烤/磨粉", "食物、淀粉"),
    ("chinquapin", "AFC 已有", "栗子", "壳", "果树/树苗", "结果→采收", "去壳→煮/烤/磨粉", "食物、淀粉"),
]

mushrooms = [
    ("oyster", "平菇", "食用", "菌包", "孢子接种→走菌→出菇→采", "鲜食/干燥/汤", "2–4/潮；2–3 潮"),
    ("shiitake", "香菇", "食用", "菌包", "孢子接种→走菌→出菇→采", "鲜食/干燥/汤/调味", "2–4/潮；2–3 潮"),
    ("button", "双孢菇", "食用", "菌包", "孢子接种→走菌→出菇→采", "鲜食/干燥/汤", "2–4/潮；2–3 潮"),
    ("enoki", "金针菇", "食用", "菌包", "孢子接种→走菌→出菇→采", "鲜食/汤/腌渍", "2–4/潮；2–3 潮"),
    ("wood_ear", "木耳", "食用", "菌包", "孢子接种→走菌→出菇→采", "干燥/泡发/炒制", "2–4/潮；2–3 潮"),
    ("reishi", "灵芝", "药用", "菌包", "孢子接种→走菌→出菇→采", "干燥→切片→煎煮/研磨", "1–2/潮；2–3 潮"),
    ("lions_mane", "猴头菇", "药用/食用", "菌包", "孢子接种→走菌→出菇→采", "鲜食/干燥/煎煮", "1–2/潮；2–3 潮"),
    ("maitake", "舞茸", "食用/药用", "菌包/腐木", "孢子接种→走菌→出菇→采", "鲜食/干燥/煎煮", "2–4/潮；2–3 潮"),
    ("king_oyster", "杏鲍菇", "食用", "菌包", "孢子接种→走菌→出菇→采", "鲜食/烤/干制", "2–3/潮；2–3 潮"),
    ("shimeji", "蟹味菇", "食用", "菌包", "孢子接种→走菌→出菇→采", "鲜食/汤/干制", "2–4/潮；2–3 潮"),
    ("porcini", "牛肝菌", "食用", "菌包+树根/腐木", "接种→走菌→出菇→采", "鲜食/干燥/调味", "1–2/潮；2–3 潮"),
    ("morel", "羊肚菌", "食用", "菌包/林下菌床", "接种→走菌→出菇→采", "鲜食/干燥/调味", "1–2/潮；2–3 潮"),
    ("chanterelle", "鸡油菌", "食用", "菌根菌床/树根", "接种树根→出菇→采", "鲜食/干燥/调味", "1–2/潮；2–3 潮"),
    ("black_truffle", "黑松露", "食用/药用", "树根接种", "接种树根→多年培养→采", "鲜食/研磨/油浸", "1–2/季；极低产"),
    ("turkey_tail", "云芝", "药用", "菌包/腐木", "孢子接种→走菌→出菇→采", "干燥→煎煮/研磨", "1–2/潮；2–3 潮"),
]

a_group_of = {c for c, s in base if s.startswith("A")}
bundle_crops = [
    "millet", "foxtail_millet", "fonio", "spelt", "emmer", "einkorn",
    "pearl_millet", "finger_millet", "sorghum", "jobs_tears",
    "barley", "oat", "rice", "rye", "wheat", "maize",
]
non_bundle_grains = ["buckwheat", "amaranth", "quinoa"]
waste_group = {
    "叶菜/茎菜": ("外叶/老叶", "tfc:compost_greens/high", "饲料/堆肥；部分可腌"),
    "根/块茎/鳞茎": ("茎叶/皮渣", "tfc:compost_greens/medium", "饲料/堆肥；嫩叶可食用"),
    "谷物/禾本": ("秸秆/颖壳", "tfc:compost_browns/low", "饲料/燃料/编织/堆肥"),
    "豆类": ("藤蔓/豆荚", "tfc:compost_greens/high", "饲料/堆肥；部分可扦插"),
    "油料": ("茎秆/荚壳", "tfc:compost_browns/low", "饲料/燃料/堆肥"),
    "纤维": ("麻屑/叶渣", "tfc:compost_browns/high", "纸/燃料/堆肥"),
    "茄果/瓜类": ("老叶/茎藤/瓜瓤", "tfc:compost_greens/medium", "饲料/堆肥；纤维/容器另计"),
    "香草/香料": ("茎叶残渣", "tfc:compost_greens/medium", "堆肥/饲料"),
    "特用": ("茎叶/残渣", "tfc:compost_greens/medium", "按物种；饲料/纤维/堆肥"),
    "水生/其他": ("叶/茎残渣", "tfc:compost_greens/medium", "饲料/堆肥；纤维另计"),
    "浆果特例": ("老叶/匍匐茎残段", "tfc:compost_greens/high", "堆肥/饲料"),
    "叶菜/饲草": ("叶/茎残渣", "tfc:compost_greens/high", "饲料/堆肥"),
    "豆类/油料": ("藤蔓/豆荚", "tfc:compost_greens/high", "饲料/堆肥"),
    "水生/纤维": ("叶/茎残渣", "tfc:compost_greens/low", "纸/堆肥"),
}
waste_override = {
    "cassava": ("叶/皮渣", "tfc:compost_greens/low", "去毒后饲料/堆肥"),
    "taro": ("叶/皮渣", "tfc:compost_greens/low", "必须煮熟去毒后才可饲料/堆肥"),
    "yam": ("叶/皮渣", "tfc:compost_greens/low", "去毒后饲料/堆肥"),
    "hemp": ("麻屑/叶渣", "tfc:compost_browns/high", "纸/燃料/堆肥"),
    "flax": ("麻屑/荚壳", "tfc:compost_browns/high", "纸/燃料/堆肥"),
    "cotton": ("棉秆/叶渣", "tfc:compost_browns/medium", "燃料/堆肥"),
    "sugarcane": ("蔗叶/蔗渣", "tfc:compost_browns/high", "燃料/纸/堆肥"),
    "jute": ("麻屑/叶渣", "tfc:compost_browns/high", "纸/燃料/堆肥"),
    "papyrus": ("叶渣/根茎", "tfc:compost_greens/low", "纸/堆肥"),
    "loofah": ("藤叶/果渣", "tfc:compost_greens/medium", "堆肥；纤维另计"),
    "bottle_gourd": ("藤叶/果壳", "tfc:compost_greens/medium", "堆肥；容器另计"),
    "winter_melon": ("藤叶/瓜瓤", "tfc:compost_greens/medium", "饲料/堆肥"),
    "cantaloupe": ("藤叶/瓜瓤", "tfc:compost_greens/medium", "饲料/堆肥"),
    "pumpkin": ("藤叶/瓜瓤", "tfc:compost_greens/medium", "饲料/堆肥"),
    "melon": ("藤叶/瓜瓤", "tfc:compost_greens/medium", "饲料/堆肥"),
    "squash": ("藤叶/瓜瓤", "tfc:compost_greens/medium", "饲料/堆肥"),
}
lines = []
lines.append("# 291 作物系统完整修改文档（整合稿 v2）\n")
lines.append("> 日期：2026-10-28\n")
lines.append("> 性质：**计划/修改规格**，不是实现。**本轮未推送、未提交远程。**\n")
lines.append("> 整合：`287` 要求、`288` 生产/培育链、`289` 116 条作物矩阵、`290` 流程/产量平衡；并新增 B 香料、坚果、蘑菇。\n")
lines.append("\n## 目录\n")
lines.append("- [1. 范围与统计](#1-范围与统计)\n"
             "- [2. 当前状态与前置问题](#2-当前状态与前置问题)\n"
             "- [3. 设计原则](#3-设计原则)\n"
             "- [4. 生产链](#4-生产链)\n"
             "- [5. 培育链与种子处理](#5-培育链与种子处理)\n"
             "- [6. 流程 profile 与产量平衡](#6-流程-profile-与产量平衡)\n"
             "- [7. A 87 作物矩阵](#7-a-87-作物矩阵)\n"
             "- [8. TFC 29 作物矩阵](#8-tfc-29-作物矩阵)\n"
             "- [9. B 新增农作物/栽培物](#9-b-新增农作物栽培物)\n"
             "- [10. TFC 10 灌木](#10-tfc-10-灌木)\n"
             "- [11. 修改范围清单](#11-修改范围清单)\n"
             "- [12. 实施批次与验收](#12-实施批次与验收)\n"
             "- [13. 未决问题](#13-未决问题)\n"
             "- [14. 来源文档](#14-来源文档)\n")

lines.append("\n## 1. 范围与统计\n")
lines.append("| 类别 | 数量 | 说明 |\n|---|---:|---|\n")
lines.append("| A 作物 | 87 | 以 `crops-manifest.json` 为准；旧文档常写 86 |\n")
lines.append("| TFC 作物 | 29 | TFC 原版 `crop/*` |\n")
lines.append("| TFC 灌木 | 10 | 草莓已经是 A 普通作物（A 也移除了 TFC 草莓灌木的世界生成），不再作为 B 的灌木重做目标 |\n")
lines.append("| 已有作物记录合计 | 116 | A 87 + TFC 29 |\n")
lines.append("| B 新增香料作物 | 20 | basil · bay_laurel · cardamom · cilantro · cumin · oregano · pimento · vanilla · black_pepper · cinnamon · clove · nutmeg · saffron · star_anise · rosemary · thyme · sage · dill · fennel · mustard |\n")
lines.append("| B 新增坚果 | 8 | acorn · chestnut · pistachio · cashew · macadamia · pine_nut · hickory_nut · beechnut；另有 A/AFC 已有 6 种坚果 |\n")
lines.append("| B 新增蘑菇栽培 | 15 | oyster · shiitake · button · enoki · wood_ear · reishi · lions_mane · maitake · king_oyster · shimeji · porcini · morel · chanterelle · black_truffle · turkey_tail |\n")
lines.append("| B 新增记录合计 | 43 | 20 香料 + 8 坚果 + 15 蘑菇；蘑菇是栽培物，不是普通作物 |\n")
lines.append("| 副产物物品 | 1 + 16 + 159 | `wet_grass`（1）+ `grain_bundle/<crop>`（16）+ `crop_waste/<crop>`（159）；坚果壳/菌渣另算 |\n")
lines.append("| 全部作物/栽培记录 | 159 | 116 已有 + 43 B 新增 |\n")
lines.append("\n> 统计口径：A 87 与 TFC 29 是已有内容；8 香料是 Firmalife 搁置项接管/重建，2 坚果是 B 新物品/树产，7 蘑菇是 B 新菌包栽培物。\n")

lines.append("\n## 2. 当前状态与前置问题\n")
lines.append("### 2.1 当前状态\n")
lines.append("- B 没有作物生产/培育链，也没有 116 条作物映射；\n")
lines.append("- A 已有 87 种作物与食物/种子资源；A 还覆盖 6 个 TFC cabbage 模型；\n")
lines.append("- TFC 29 作物仍是原版十字模型与统一 6–10 掉落；\n")
lines.append("- TFC 10 灌木仍在 TFC 灌木管线；草莓已经是 A 普通作物，TFC 草莓灌木被 A 关闭世界生成/隐藏；\n")
lines.append("- B 已有 `in_world`、案板、研钵、干燥架、炒锅，但没有育苗盘、移栽、种子处理、农艺操作；\n")
lines.append("- 香料、坚果、蘑菇三项此前搁置，当前完成度 0。\n")
lines.append("### 2.2 前置问题\n")
lines.append("1. **A/B 资源所有权**：A 持有 6 个 `assets/tfc/models/block/crop/cabbage_age_*.json`；B 的 TFC 29 覆盖会与 A 同路径冲突。\n")
lines.append("2. **TFC EUPL 授权链**：TFC 资源覆盖属于派生风险，EUPL 通知/许可证/来源登记未完成。\n")
lines.append("3. **范围未统一**：A 87、TFC 29、TFC 10 灌木、B 43 新增，四套范围的生产/培育链覆盖口径必须先定。\n")

lines.append("\n## 3. 设计原则\n")
lines.append("1. **每一作物都必须闭环**：主产品、副产品、繁殖、育苗/种子处理、初步加工、出口。\n")
lines.append("2. **不做纯资源重做**：六环节/九工序必须落的方块、物品、BE、`in_world`、DataComponent 上。\n")
lines.append("3. **产量按产率平衡**：TFC raw 保持原值，A raw 可调但需单批评审；优先调加工转化率、副产物、种子返还。\n")
lines.append("4. **不新增无用途产物**：新副产物必须有饲料/堆肥/纸/燃料/油/药等出口。\n")
lines.append("5. **不使用统一模板覆盖所有作物**：至少 27 个流程 profile，并逐作物填写关键工序。\n")
lines.append("6. **兼容优先**：TFC 存档、A 独立可卸载、TFC EUPL 义务必须先满足。\n")

lines.append("\n## 4. 生产链\n")
lines.append("| 族 | 数量 | 主链 |\n|---|---:|---|\n")
lines.append("| A 叶菜/茎菜 | 21 | 切/撕→盐渍→乳酸发酵→晒干 |\n")
lines.append("| A 根/块茎/鳞茎 | 17 | 清洗→去皮→切片→晒干/磨粉/沉淀淀粉；木薯/芋头/山药先去毒 |\n")
lines.append("| A 谷物/禾本 | 12 | 脱粒→扬场→磨粉；麦类制麦芽、稻类碾米 |\n")
lines.append("| A 豆类 | 9 | 干燥→脱荚→浸泡→磨浆/煮制/发酵 |\n")
lines.append("| A 油料 | 4 | 清理→炒/烘→磨→蒸→制饼→压榨 |\n")
lines.append("| A 纤维 | 4 | 沤麻→打麻→梳麻→纺线/织布 |\n")
lines.append("| A 茄果/瓜类 | 10 | 取籽/切片→晒干/磨粉/腌渍/熬酱；丝瓜取络、葫芦做容器 |\n")
lines.append("| A 香草/香料 | 1 | 采叶/花→干燥→研磨→过筛 |\n")
lines.append("| A 特用 | 5 | 五物种五条不同链 |\n")
lines.append("| A 水生/其他 | 3 | 采割→脱粒/晒干/剥壳；纤维类沤制 |\n")
lines.append("| A 浆果特例 | 1 | 草莓匍匐茎苗→果酱/果干 |\n")
lines.append("| TFC 谷物 | 7 | 脱粒→扬场→磨粉/碾米/麦芽 |\n")
lines.append("| TFC 根/块茎/鳞茎 | 7 | 清洗→去皮→切片→晒干/磨粉/淀粉 |\n")
lines.append("| TFC 豆类/油料 | 5 | 干燥→脱荚/清理→浸泡/压榨/磨浆 |\n")
lines.append("| TFC 叶菜/饲草 | 2 | 盐渍/发酵/晒干；饲草晒干打捆 |\n")
lines.append("| TFC 茄果/瓜类 | 6 | 鲜食/晒干/磨粉/熬酱；瓜籽/果肉分开 |\n")
lines.append("| TFC 纤维 | 1 | 沤麻→打麻→梳麻→纺线 |\n")
lines.append("| TFC 水生/纤维 | 1 | 割茎→沤制/剥皮→压片/打麻 |\n")
lines.append("| B 香料 | 20 | 采叶/种子/果荚→干燥→研磨→过筛 |\n")
lines.append("| B 坚果 | 8 | 落果/采收→去壳→干燥→烤/磨粉/榨油 |\n")
lines.append("| B 蘑菇 | 15 | 菌包/菌根接种→走菌→出菇→采→干燥/鲜食/药用 |\n")
lines.append("\n生产链硬约束：每物种主产品+副产品；每产物至少一个加工/使用出口；原有掉落不减少；未成熟破坏补偿；禁止死端。\n")
lines.append("\n### 4.1 副产物出口：潮湿草与废枝叶\n")
lines.append("这两项是**收获/破坏方块时一次产出的副产物**，不是新的作物物种。\n")
lines.append("#### 4.1.1 潮湿草 `wet_grass`\n")
lines.append("| 项 | 设计 |\n|---|---|\n")
lines.append("| 来源 1 | 13 种 TFC 野生草（beachgrass · bluegrass · bromegrass · fountain_grass · orchard_grass · pampas_grass · raddia_grass · red_oat_grass · ryegrass · scutch_grass · switchgrass · tall_fescue_grass · timothy_grass）在非干枯状态被收割 |\n")
lines.append("| 来源 2 | 未成熟作物被破坏时通过 `tfc:extra_products` 补偿产出 |\n")
lines.append("| 干燥 | `wet_grass` → **TFC `tfc:straw`（干草/秸秆）**，走晒架/Firmalife drying mat 或 TFC heating；1:1 干燥，不新增第二条 straw 链 |\n")
lines.append("| 用途 | 饲料、绿色堆肥 `tfc:compost_greens/*`、晒干后编织/燃料/青贮 |\n")
lines.append("| 平衡 | 每次收割 1–2 份湿草；晒干 1:1；不减少原有剪刀掉落；干枯草（`dry_grass` 等）直接走 `tfc:straw`，不产湿草 |\n")
lines.append("| 兼容 | 野草掉落表 `replace=false`，保留剪刀→植物方块；湿草是新增分支，不删除 TFC 的 straw 用途链 |\n")
lines.append("#### 4.1.2 废枝叶：逐作物专属，不设通用 `green_waste`\n")
lines.append("“废枝叶”只是统称，**每个作物一个专属物品 `crop_waste/<crop>`**，不能用一个通用 `green_waste` 覆盖全部。下面逐作物给出类型、堆肥档与其它出口。\n")
lines.append("| 作物 | 来源/组 | 废枝叶物品 | 类型 | 堆肥档 | 其它出口 |\n")
lines.append("|---|---|---|---|---|---|\n")
for crop, sg in order:
    group = sg.split("·", 1)[1] if "·" in sg else sg
    wtype, tag, alt = waste_override.get(crop, waste_group.get(group, ("茎叶残渣", "tfc:compost_greens/medium", "堆肥/饲料")))
    lines.append(f"| `{crop}` | {sg} | `tfcagricultureplus:crop_waste/{crop}` | {wtype} | `{tag}` | {alt} |\n")
lines.append("#### 4.1.3 谷物捆：湿草的加工来源\n")
lines.append("不是所有谷物都直接掉散粒：**长秆谷物先收谷物捆，再脱粒**，脱粒副产才是湿草。\n")
lines.append("| 作物 | 来源 | 谷物捆物品 | 收获 | 脱粒 | 湿草/干燥 | 备注 |\n")
lines.append("|---|---|---|---|---|---|---|\n")
for crop in bundle_crops:
    src = "A" if crop in a_group_of else "TFC"
    lines.append(f"| `{crop}` | {src} | `tfcagricultureplus:grain_bundle/{crop}` | 成熟收获 → 1–2 捆 + 种子 | 脱粒 → 谷粒 + 1–2 `wet_grass` | `wet_grass` 1:1 晒干 → `tfc:straw` | 主产品仍是谷粒；不减少原有谷粒 |\n")
lines.append("非谷物捆（直接脱粒/散粒）：" + " · ".join("`" + c + "`" for c in non_bundle_grains) + "；TFC 的 `sugarcane` 不属于谷物捆。\n")
lines.append("**TFC 兼容**：TFC 29 的 raw 掉落建议不直接改；TFC 谷物是否改走 `grain_bundle` 需单批确认。A 的谷物捆可先落地。\n")
lines.append("#### 4.1.4 废枝叶/菌渣/坚果壳的边界\n")
lines.append("- 坚果壳：不是“绿色废枝叶”，单独走 `nut_shell/<nut>` → `tfc:compost_browns/high` / 燃料；\n")
lines.append("- 蘑菇废菌包：`spent_substrate` → `tfc:compost_browns/medium` / 堆肥，不算绿色枝叶；\n")
lines.append("- 香料废枝叶：`crop_waste/<spice>` → 按 `compost_greens/high|medium`；\n")
lines.append("- 所有 `crop_waste` / 壳 / 菌渣必须有堆肥/饲料/燃料/纸至少一个出口，不得造死物品。\n")

lines.append("\n## 5. 培育链与种子处理\n")
lines.append("### 5.1 种植侧六环节\n")
lines.append("1. 留种/采种：有性种子 + 无性块茎/鳞茎/根茎/扦插/分株/匍匐茎；母株性状用 DataComponent。\n")
lines.append("2. 育苗：育苗盘/苗床方块 + BE，温湿度影响成活。\n")
lines.append("3. 移栽：`in_world` 手持苗右键耕地，校验土壤/气候，缓苗期。\n")
lines.append("4. 生长管理：间苗、培土、搭架、打顶、除草、施肥。\n")
lines.append("5. 收获：主产品+次产品；未成熟破坏补偿 **`wet_grass` 潮湿草**；废枝叶产 **逐作物 `crop_waste/<crop>`**；谷物按 4.1.3 先出谷物捆，脱粒产 `wet_grass`。\n")
lines.append("6. 留种循环：成熟株留种/扦插闭环。\n")
lines.append("### 5.2 加工侧九工序\n")
lines.append("采种→种子干燥→选种/筛种→浸种→催芽→拌种→扦插/分株→育苗→移栽。\n")
lines.append("\n**关键价值**：浸种/催芽缩短生长时间；无性繁殖保留母株性状。\n")

lines.append("\n## 6. 流程 profile 与产量平衡\n")
lines.append("### 6.1 现有产率基线\n")
lines.append("- A/TFC 普通作物：主产品 `0–(6–10)`，种子通常 1（部分 1–2）；\n")
lines.append("- 红/黄甜椒：`4–5 ×2`；\n")
lines.append("- melon/pumpkin：走果实方块掉落，不在 6–10 作物池；\n")
lines.append("- 当前普通作物没有按物种区分产率。\n")
lines.append("### 6.2 约束\n")
lines.append("```text\nseedBack >= 1\nprocessed <= raw\nprocessed >= 1\nbyproduct >= 1\n```\n")
lines.append("- TFC 29 raw 保持原值；A 87 raw 可调但需单批评审；\n")
lines.append("- 平衡优先通过加工转化率、副产物比例、种子返还实现；\n")
lines.append("- 20 次收获均值/区间验收。\n")
lines.append("### 6.3 流程 profile\n")
lines.append("27 个 profile：`leaf-preserve`、`root-starch`、`root-detox`、`root-spice`、`grain-mill`、`grain-rice`、`grain-malt`、`legume-dry`、`legume-oil`、`oil-press`、`fiber-bast`、`fiber-oil`、`fiber-syrup`、`fiber-water`、`fruit-preserve`、`fruit-seed`、`fruit-fiber`、`fruit-container`、`fruit-spice`、`fruit-paste`、`herb-dry`、`water-grain`、`berry-runner`、`leaf-forage`、`sugar`、`special-brew`、`special-triple`。\n")

lines.append("\n## 7. A 87 作物矩阵\n")
lines.append("| # | 作物 | 来源/组 | 主产品 | 副产品 | 繁殖 | 育苗/种子处理 | 初步加工 | 流程 | 产率计划（现/目标/seed/加工/副） | 定制关键步骤 | 出口 | 批次 |\n")
lines.append("|---:|---|---|---|---|---|---|---|---|---|---|---|---|\n")
a_rows = [(i, k) for i, k in enumerate(order, 1) if k[1].startswith("A·")]
for i, key in a_rows:
    x, f = base[key], flow[key]
    yp = f"现:{f['baseline']}<br>目标:{f['raw']}<br>seed:{f['seed']}<br>加工:{f['processed']}<br>副:{f['by_yield']}"
    lines.append(f"| {i} | `{x['crop']}` | {x['sg']} | {x['main']} | {x['by']} | {x['prop']} | {x['nursery']} | {x['process']} | `{f['flow']}` | {yp} | {f['key']} | {x['outlet']} | {x['batch']} |\n")

lines.append("\n## 8. TFC 29 作物矩阵\n")
lines.append("| # | 作物 | 来源/组 | 主产品 | 副产品 | 繁殖 | 育苗/种子处理 | 初步加工 | 流程 | 产率计划（现/目标/seed/加工/副） | 定制关键步骤 | 出口 | 批次 |\n")
lines.append("|---:|---|---|---|---|---|---|---|---|---|---|---|---|\n")
t_rows = [(i, k) for i, k in enumerate(order, 1) if k[1].startswith("TFC·")]
for i, key in t_rows:
    x, f = base[key], flow[key]
    yp = f"现:{f['baseline']}<br>目标:{f['raw']}<br>seed:{f['seed']}<br>加工:{f['processed']}<br>副:{f['by_yield']}"
    lines.append(f"| {i} | `{x['crop']}` | {x['sg']} | {x['main']} | {x['by']} | {x['prop']} | {x['nursery']} | {x['process']} | `{f['flow']}` | {yp} | {f['key']} | {x['outlet']} | {x['batch']} |\n")

lines.append("\n## 9. B 新增农作物/栽培物\n")
lines.append("> 本批是把此前搁置的香料、坚果、蘑菇纳入 B；它们不属于 A 87/TFC 29，必须单独建 ID/标签/手册/产量。\n")
lines.append("### 9.1 香料作物 20 种\n")
lines.append("| # | 物种 | 形态 | 主产品 | 副产品 | 繁殖 | 育苗 | 初步加工 | 出口 | 目标产率 |\n")
lines.append("|---:|---|---|---|---|---|---|---|---|---|\n")
for i, s in enumerate(spices, 1):
    lines.append(f"| {i} | `{s[0]}` | {s[1]} | {s[2]} | {s[3]} | {s[4]} | {s[5]} | {s[6]} | {s[7]} | {s[8]} |\n")
lines.append("### 9.2 坚果\n")
lines.append("| 物种 | 来源 | 主产品 | 副产品 | 繁殖 | 采收/加工 | 出口 | 目标产率 |\n")
lines.append("|---|---|---|---|---|---|---|---|\n")
for n in nuts:
    lines.append(f"| {n[0]} | {n[1]} | {n[2]} | {n[3]} | {n[4]} | {n[5]} | {n[6]} | 4–8 个/树；壳 2–4 |\n")
for n in existing_nuts:
    lines.append(f"| {n[0]} | {n[1]} | {n[2]} | {n[3]} | {n[4]} | {n[5]} | {n[6]} | — |\n")
lines.append("### 9.3 蘑菇栽培 15 种\n")
lines.append("菌包：`stage=0` 空包 → `1` 走菌 → `2` 出菇 → `3` 枯竭；孢子来自 vanilla brown/red mushroom；温湿度复用温室/地窖；收获后废菌包→堆肥。\n")
lines.append("| # | 物种 | 形态/类型 | 载体 | 流程 | 加工/出口 | 目标产率 |\n")
lines.append("|---:|---|---|---|---|---|---|\n")
for i, m in enumerate(mushrooms, 1):
    lines.append(f"| {i} | `{m[0]}` | {m[1]}（{m[2]}） | {m[3]} | {m[4]} | {m[5]} | {m[6]} |\n")
lines.append("### 9.4 新增内容总量\n")
lines.append("- 20 香料 + 8 坚果 + 15 蘑菇 = **43 条新增记录**；\n")
lines.append("- 香料是 Firmalife 搁置项接管/重建 + 新增；坚果是 B 新物品/树产；蘑菇是 B 新菌包/菌根栽培物；\n")
lines.append("- 全部进入 P1/P2 批次，不混入 A 87/TFC 29 的统计；43 条全部必须逐条有产物/副产物/加工/出口。\n")

lines.append("\n## 10. TFC 10 灌木\n")
lines.append("| 物种 | 主产品 | 繁殖 | 初步加工/出口 | 育苗 |\n|---|---|---|---|---|\n")
bush = [
    ("blackberry", "聚合果", "扦插/压条", "果酱、果干、汁", "扦插→育苗→移栽"),
    ("blueberry", "浆果", "种子/扦插", "果酱、果干、汁", "扦插→育苗→移栽"),
    ("bunchberry", "浆果", "种子/分株", "果酱、果干", "分株/种子→育苗→移栽"),
    ("cloudberry", "浆果", "种子/分株", "果酱、果干", "分株→育苗→移栽"),
    ("cranberry", "浆果", "扦插/匍匐茎", "果酱、果干、汁", "匍匐茎→育苗→定植"),
    ("elderberry", "浆果", "种子/扦插", "果酱、糖浆、汁", "扦插→育苗→移栽"),
    ("gooseberry", "浆果", "种子/扦插", "果酱、果干", "扦插→育苗→移栽"),
    ("raspberry", "聚合果", "分株/扦插", "果酱、果干、汁", "分株→育苗→移栽"),
    ("snowberry", "浆果", "种子/分株", "果酱、果干", "分株→育苗→移栽"),
    ("wintergreen", "浆果", "种子/分株", "果酱、干果", "分株→育苗→移栽"),
]
for name, main, prop, process, nursery in bush:
    lines.append(f"| `{name}` | {main} | {prop} | {process} | {nursery} |\n")
lines.append("\n草莓已经由 A 迁移为普通作物，不在 B 的 10 种 TFC 灌木重做范围内；TFC 草莓灌木的世界生成已由 A 的标签 remove 关闭。10 种灌木不得改 A 已有标签；覆盖 TFC 标签只能追加；蜂蜜 `buzzing_leaves` 兼容不能破坏。\n")

lines.append("\n## 11. 修改范围清单\n")
lines.append("| 层 | 修改内容 | 备注 |\n|---|---|---|\n")
lines.append("| 数据 | 159 条记录/产量/产物映射；A 87、TFC 29、B 43 分开 | TFC raw 保持原值 |\n")
lines.append("| 物品 | 处理种子、苗、扦插枝、种薯/种球、孢子/菌种 | 需定 B 新 ID 或 DataComponent |\n")
lines.append("| 副产物 | `wet_grass`；`grain_bundle/<crop>`；每作物 `crop_waste/<crop>`；坚果壳/菌渣另计 | 不设通用废枝叶；湿草来自谷物捆脱粒/野草/未成熟补偿；堆肥按作物分档 |\n")
lines.append("| 方块 | 育苗盘/苗床、种子干燥架、筛选台、浸种/催芽容器、移栽载体、菌包 | 菌包 4 stage；苗床需 BE |\n")
lines.append("| 行为 | 六环节、九工序、农艺操作、留种循环、蘑菇走菌/出菇 | `in_world` + DataComponent + 随机刻 |\n")
lines.append("| 加工 | 27 个 profile 的初加工与副产物出口 | 每个 profile 至少 1 完整链 |\n")
lines.append("| 香料/坚果/蘑菇 | 20+8+15 新内容，独立 ID/标签/手册 | 香料接管 Firmalife 需兼容 |\n")
lines.append("| TFC | 29 作物 + 10 灌木资源覆盖 | 先解决 A cabbage 所有权/EUPL |\n")
lines.append("| 验收 | 159 条记录逐条检查 | 不以静态/贴图替代实机 |\n")

lines.append("\n## 12. 实施批次与验收\n")
lines.append("| 批次 | 内容 | 验收 |\n|---|---|---|\n")
lines.append("| P0 | 数据矩阵/ID/标签/产量带落表；选 1 物种打通全链 | 字段完整、无死端 |\n")
lines.append("| P1 | 种子处理+育苗+移栽+缓苗；`wet_grass` 野草/谷物捆脱粒/干燥；逐作物 `crop_waste` 绿色堆肥标签；香料/坚果开始 | 六环节可执行、seedBack 达标 |\n")
lines.append("| P2 | 各 profile 初加工；蘑菇菌包；坚果去壳/榨油；香料干燥/研磨；潮湿草晒干/废枝叶堆肥验证 | 每 profile 至少 1 完整链 |\n")
lines.append("| P3 | 159 条逐作物覆盖与产量实测调参 | 全记录通过验收 |\n")
lines.append("| P4 | TFC 29+10 灌木资源层接入 | 不改 TFC raw；存档安全 |\n")
lines.append("\n每记录验收：主产品/副产品、繁殖、育苗/种子处理、初步加工、出口、原掉落不减少、20 次收获均值在产量带、与同类无数量级失衡。\n")

lines.append("\n## 13. 未决问题\n")
lines.append("1. A 87 与旧文档 86 的差异收敛。\n")
lines.append("2. A 87、TFC 29、TFC 10 灌木、B 43 新增各自是否共用同一套六环节。\n")
lines.append("3. 育苗盘/移栽是 B 自有方块还是扩展 TFC 行为；需定 API。\n")
lines.append("4. TFC 种子处理后的产物是 B 新物品还是 DataComponent。\n")
lines.append("5. TFC raw 保持原值，A raw 是否允许调整。\n")
lines.append("6. A 的 6 个 TFC cabbage 模型所有权与 TFC EUPL 授权链。\n")
lines.append("7. 蔬菜/油料/纤维双主产的产量分账口径。\n")
lines.append("8. 20 香料中 bay_laurel/pimento/vanilla/cinnamon/clove/nutmeg 等树/藤形态与占地、搭架、气候如何落。\n")
lines.append("9. 15 蘑菇的菌包/菌根配方、温湿度、产量与药用效果强度。\n")
lines.append("10. 8 坚果中 acorn/chestnut/pine_nut/hickory_nut/beechnut 的挂树方式与 A/AFC 已有坚果如何避免重复。\n")
lines.append("11. 野草收割是否把所有非干枯草的 sharp 掉落改为 `wet_grass`（再晒成 straw），还是保留原 straw 并仅追加湿草分支；同时需定 TFC 谷物是否改走 `grain_bundle`。\n")
lines.append("12. 废枝叶已定为**逐作物 `crop_waste/<crop>`**；high/medium/low 的最终分配需按 TFC 碳氮比实测校准，不能用一个通用物品替代。\n")

lines.append("\n## 14. 来源文档\n")
lines.append("- `287-crop-redo-requirements-20261028.md`：原始要求、29 作物/10 灌木、当前缺口；草莓已由 A 迁移为普通作物。\n")
lines.append("- `288-crop-production-and-cultivation-chain-20261028.md`：86 种生产链、六环节/九工序。\n")
lines.append("- `289-crop-master-plan-20261028.md`：116 条逐作物矩阵。\n")
lines.append("- `290-crop-flow-and-yield-balance-20261028.md`：27 profile、产率/平衡。\n")
lines.append("- `archive/117-agriculture-redesign-plan.md` §6.1（香料/蘑菇/坚果搁置项解禁）、§6.8（六环节）、§9.1（新增/接管清单）。\n")

OUT.write_text("".join(lines), encoding="utf-8")
print("wrote", OUT, "A rows", len(a_rows), "TFC rows", len(t_rows), "bytes", OUT.stat().st_size)
