from pathlib import Path
import json, re

DOC = Path("mod_rebuild/docs/291-crop-system-complete-modification-20261028.md")
a = Path("mod_rebuild/docs/289-crop-master-plan-20261028.md")
b = Path("mod_rebuild/docs/290-crop-flow-and-yield-balance-20261028.md")


def parse_matrix(path):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|([^|]*)\|(.*)\|\s*$", line)
        if not m:
            continue
        crop = m.group(2)
        sg = m.group(3).strip()
        cells = [x.strip() for x in m.group(4).split("|")]
        cells = [x for x in cells if x != ""]
        rows.append((crop, sg, cells))
    return rows


r289 = parse_matrix(a)
r290 = parse_matrix(b)
base = {}
for crop, sg, cells in r289:
    if len(cells) != 7:
        raise SystemExit(f"289 parse {crop}: {len(cells)} {cells}")
    main, by, prop, nursery, process, outlet, batch = cells
    base[(crop, sg)] = dict(crop=crop, sg=sg, main=main, by=by, prop=prop,
                            nursery=nursery, process=process, outlet=outlet, batch=batch)
flow = {}
for crop, sg, cells in r290:
    if len(cells) != 7:
        raise SystemExit(f"290 parse {crop}: {len(cells)} {cells}")
    flow_name, baseline, raw, seed, processed, by_yield, key = cells
    flow_name = flow_name.strip("` ")
    flow[(crop, sg)] = dict(flow=flow_name, baseline=baseline, raw=raw, seed=seed,
                            processed=processed, by_yield=by_yield, key=key)

if len(base) != 116 or len(flow) != 116:
    raise SystemExit(f"expected 116 rows, base={len(base)} flow={len(flow)}")
if set(base) != set(flow):
    raise SystemExit("289/290 keys differ")

# group/order as they appear in 289
order = []
for crop, sg, cells in r289:
    order.append((crop, sg))

# production family table
family = [
    ("A 叶菜/茎菜", "21", "切/撕 → 盐渍 → 乳酸发酵 → 晒干；叶球类切丝盐渍"),
    ("A 根/块茎/鳞茎", "17", "清洗 → 去皮 → 切片 → 晒干/磨粉/沉淀淀粉；木薯/芋头/山药先去毒"),
    ("A 谷物/禾本", "12", "脱粒 → 扬场 → 磨粉；麦类可制麦芽，稻类碾米"),
    ("A 豆类", "9", "干燥 → 脱荚 → 浸泡 → 磨浆/煮制/发酵"),
    ("A 油料", "4", "清理 → 炒/烘 → 磨 → 蒸 → 制饼 → 压榨"),
    ("A 纤维", "4", "沤麻 → 打麻 → 梳麻 → 纺线/织布"),
    ("A 茄果/瓜类", "10", "清洗 → 取籽/切片 → 晒干/磨粉/腌渍/熬酱；丝瓜取络、葫芦做容器"),
    ("A 香草/香料", "1", "采叶/花 → 干燥 → 研磨 → 过筛"),
    ("A 特用", "5", "五物种五条不同链：纤维/糖浆/豆/啤酒花/薏米"),
    ("A 水生/其他", "3", "采割 → 脱粒/晒干/剥壳；纤维类沤制/打麻"),
    ("A 浆果特例", "1", "草莓：匍匐茎苗 → 果酱/果干，不按灌木"),
    ("TFC 谷物", "7", "脱粒 → 扬场 → 磨粉/碾米/麦芽；TFC raw 保持原值"),
    ("TFC 根/块茎/鳞茎", "7", "清洗 → 去皮 → 切片 → 晒干/磨粉/淀粉"),
    ("TFC 豆类/油料", "5", "干燥 → 脱荚/清理 → 浸泡/压榨/磨浆"),
    ("TFC 叶菜/饲草", "2", "叶菜盐渍/发酵/晒干；饲草晒干打捆"),
    ("TFC 茄果/瓜类", "6", "鲜食/晒干/磨粉/熬酱；瓜籽/果肉分开"),
    ("TFC 纤维", "1", "沤麻 → 打麻 → 梳麻 → 纺线"),
    ("TFC 水生/纤维", "1", "割茎 → 沤制/剥皮 → 压片/打麻"),
]

bush = [
    ("blackberry", "聚合果", "种子/扦插", "果酱、果干、汁", "扦插/压条→育苗→移栽"),
    ("blueberry", "浆果", "种子/扦插", "果酱、果干、汁", "扦插→育苗→移栽"),
    ("bunchberry", "浆果", "种子/分株", "果酱、果干", "分株/种子→育苗→移栽"),
    ("cloudberry", "浆果", "种子/分株", "果酱、果干", "分株→育苗→移栽"),
    ("cranberry", "浆果", "扦插/匍匐茎", "果酱、果干、汁", "匍匐茎→育苗→定植"),
    ("elderberry", "浆果", "种子/扦插", "果酱、糖浆、汁", "扦插→育苗→移栽"),
    ("gooseberry", "浆果", "种子/扦插", "果酱、果干", "扦插→育苗→移栽"),
    ("raspberry", "聚合果", "分株/扦插", "果酱、果干、汁", "分株→育苗→移栽"),
    ("snowberry", "浆果", "种子/分株", "果酱、果干", "分株→育苗→移栽"),
    ("wintergreen", "浆果", "种子/分株", "果酱、干果", "分株→育苗→移栽"),
    ("strawberry", "浆果/普通作物", "匍匐茎为主，种子为辅", "果酱、果干、冰淇淋", "母株→匍匐茎苗→育苗→移栽"),
]

lines = []
lines.append("# 291 作物系统完整修改文档（整合稿）\n")
lines.append("> 日期：2026-10-28\n")
lines.append("> 性质：**计划/修改规格**，不是实现；本轮未推送任何更改。\n")
lines.append("> 整合来源：`287` 要求、`288` 生产/培育链、`289` 逐作物矩阵、`290` 流程定制/产量平衡。\n")
lines.append("\n## 1. 范围与目标\n")
lines.append("- A 实际 `crops-manifest.json`：**87 种**（旧文档常写 86，以实际为准）；")
lines.append("- TFC 原版作物：**29 种**；")
lines.append("- TFC 原版浆果灌木：**11 种**（草莓改普通作物）；")
lines.append("- 合计 **116 条作物记录 + 11 条灌木记录**；")
lines.append("- 目标：为每一种作物/灌木明确**主产品、副产品、繁殖、育苗/种子处理、初步加工、出口、产量平衡**，全部闭环。\n")
lines.append("## 2. 当前状态\n")
lines.append("- B 目前没有作物/灌木生产链、培育链或 116 条映射；")
lines.append("- A 已有 87 种作物与对应食物/种子资源；A 还覆盖 6 个 TFC cabbage 模型；")
lines.append("- TFC 29 种仍是 TFC 原版十字模型与统一 6–10 掉落；")
lines.append("- 11 种 TFC 灌木仍在 TFC 灌木管线；")
lines.append("- 现有 B 有 `in_world`、案板、研钵、干燥架、炒锅，但没有育苗盘/移栽/种子处理/农艺操作。\n")
lines.append("## 3. 关键前置问题\n")
lines.append("1. **A/B 资源所有权**：A 当前持有 6 个 `assets/tfc/models/block/crop/cabbage_age_*.json`；B 若按 29 作物覆盖 cabbage 会与 A 同路径冲突，必须先决定移交/保留/跳过。")
lines.append("2. **TFC EUPL 授权链**：TFC 资源覆盖属于派生风险；当前 EUPL 通知、许可证文本、来源登记未完成。")
lines.append("3. **范围**：A 87、TFC 29、TFC 11 灌木三套内容需要明确哪些走生产/培育链，哪些只做资源覆盖。\n")
lines.append("## 4. 生产链要求\n")
lines.append("| 族 | 数量 | 主链 |\n|---|---:|---|\n")
for name, cnt, chain in family:
    lines.append(f"| {name} | {cnt} | {chain} |\n")
lines.append("\n生产链硬约束：\n")
lines.append("- 每物种主产品 + 副产品；\n")
lines.append("- 每产物至少一个加工/使用出口；\n")
lines.append("- 原有掉落不减少，只允许 `tfc:extra_products` 增加副产；\n")
lines.append("- 未成熟破坏应有新鲜草等补偿；\n")
lines.append("- 不允许“只有种子/只能生吃/只换贴图”的死端。\n")
lines.append("## 5. 培育链与种子处理\n")
lines.append("### 5.1 种植侧六环节（117 §6.8）\n")
lines.append("1. 留种/采种：有性种子 + 无性块茎/鳞茎/根茎/扦插/分株/匍匐茎；母株性状用 DataComponent；\n")
lines.append("2. 育苗：育苗盘/苗床方块 + BE，温湿度影响成活；\n")
lines.append("3. 移栽：`in_world` 手持苗右键耕地，校验土壤/气候，缓苗期；\n")
lines.append("4. 生长管理：间苗、培土、搭架、打顶、除草、施肥；\n")
lines.append("5. 收获：主产品 + 次产品；未成熟破坏补偿；\n")
lines.append("6. 留种循环：成熟株留种/扦插闭环。\n")
lines.append("### 5.2 加工侧九工序（126 §12.12）\n")
lines.append("采种 → 种子干燥 → 选种/筛种 → 浸种 → 催芽 → 拌种 → 扦插/分株 → 育苗 → 移栽。\n")
lines.append("\n关键价值：**浸种/催芽缩短生长时间**；无性繁殖保留母株性状。\n")
lines.append("## 6. 流程 profile 与产量平衡\n")
lines.append("### 6.1 现有产率基线（实测）\n")
lines.append("- A/TFC 普通作物：主产品 `0–(6–10)`，种子通常 1（部分 1–2）；\n")
lines.append("- 红/黄甜椒：`4–5 ×2`；\n")
lines.append("- melon/pumpkin：走果实方块掉落，不在 6–10 作物池；\n")
lines.append("- 目前普通作物没有按物种区分产率。\n")
lines.append("### 6.2 平衡约束\n")
lines.append("```text\n"
             "seedBack >= 1\n"
             "processed <= raw\n"
             "processed >= 1\n"
             "byproduct >= 1\n"
             "```\n")
lines.append("- TFC 29 raw 保持原值，不轻易改 TFC 掉落；\n")
lines.append("- A 87 raw 目标可按 profile 调整，需单批评审；\n")
lines.append("- 平衡优先通过加工转化率、副产物比例、种子返还实现；\n")
lines.append("- 20 次收获均值/区间验收。\n")
lines.append("### 6.3 逐作物流程与产量表\n")
lines.append("> 完整 116 条见 §7 合并矩阵；本表为所有行的关键字段。\n")
lines.append("\n## 7. 116 条作物完整矩阵\n")
lines.append("| # | 作物 | 来源/组 | 主产品 | 副产品 | 繁殖 | 育苗/种子处理 | 初步加工 | 流程 profile | 产率计划（现/目标/seed/加工/副） | 定制关键步骤 | 出口 | 批次 |\n")
lines.append("|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
for i, key in enumerate(order, 1):
    x = base[key]
    f = flow[key]
    yield_plan = f"现：{f['baseline']}<br>目标：{f['raw']}<br>seed：{f['seed']}<br>加工：{f['processed']}<br>副：{f['by_yield']}"
    lines.append(f"| {i} | `{x['crop']}` | {x['sg']} | {x['main']} | {x['by']} | {x['prop']} | {x['nursery']} | {x['process']} | `{f['flow']}` | {yield_plan} | {f['key']} | {x['outlet']} | {x['batch']} |\n")
lines.append("\n## 8. 11 种 TFC 浆果灌木\n")
lines.append("| 物种 | 主产品 | 繁殖 | 初步加工/出口 | 育苗 |\n|---|---|---|---|---|\n")
for name, main, prop, process, nursery in bush:
    lines.append(f"| `{name}` | {main} | {prop} | {process} | {nursery} |\n")
lines.append("\n要求：\n")
lines.append("- 灌木走 B 的灌木管线，资源覆盖 `assets/tfc/blockstates/plant/<name>_bush.json`；\n")
lines.append("- 与 A 的 12 种同族；不改 A 标签；\n")
lines.append("- 草莓单独做普通作物，不做灌木；\n")
lines.append("- 蜂蜜 `buzzing_leaves` 兼容不能破坏。\n")
lines.append("## 9. 修改范围清单\n")
lines.append("| 层 | 修改内容 | 备注 |\n|---|---|---|\n")
lines.append("| 数据 | 116 条 profile/产量/产物映射；A 87 与 TFC 29 分开 | TFC raw 保持原值 |\n")
lines.append("| 物品 | 处理种子、种子分级、育苗苗、扦插枝、种薯/种球标记 | 需决定新 ID 或 DataComponent |\n")
lines.append("| 方块 | 育苗盘/苗床、种子干燥架、筛选台、浸种/催芽容器、移栽载体 | 优先复用干燥架/barrel |\n")
lines.append("| 行为 | 六环节、九工序、农艺操作、留种循环 | `in_world` + DataComponent |\n")
lines.append("| 加工 | 每 profile 至少一条完整初加工链 | 主/副产物均需出口 |\n")
lines.append("| TFC | 29 作物资源覆盖 + 11 灌木覆盖 | 先解决 A cabbage 所有权/EUPL |\n")
lines.append("| 验收 | 116 作物 + 11 灌木逐条表格检查 | 不以静态/模型替代实机 |\n")
lines.append("## 10. 实施批次\n")
lines.append("| 批次 | 内容 | 验收 |\n|---|---|---|\n")
lines.append("| P0 | 116 条矩阵/profile/ID/标签/产量带落表；选 1 个物种打通全链 | 每个字段有值；无死端 |\n")
lines.append("| P1 | 种子处理 + 育苗 + 移栽 + 缓苗 | 六环节可执行；seedBack 达标 |\n")
lines.append("| P2 | 每个 profile 的初加工与配方 | 每条 profile 至少 1 完整链 |\n")
lines.append("| P3 | 116 条逐作物覆盖 + 产量实测调参 | 全作物通过验收 |\n")
lines.append("| P4 | TFC 29 + 11 灌木资源层接入 | 不改 TFC raw；存档安全 |\n")
lines.append("## 11. 每作物验收\n")
lines.append("每个作物必须：主产品/副产品存在；繁殖方式明确；育苗或种子处理路径明确；至少一条初步加工；至少一个出口；不减少原掉落；20 次收获均值在产量带内；与同类相比无数量级失衡。\n")
lines.append("## 12. 未决问题\n")
lines.append("1. A 87 与旧文档 86 的差异收敛。\n")
lines.append("2. A 87、TFC 29、TFC 11 灌木各自是否共用同一套六环节。\n")
lines.append("3. 育苗盘/移栽是 B 自有方块还是扩展 TFC 行为；需定 API。\n")
lines.append("4. TFC 种子处理后的产物是 B 新物品还是 DataComponent。\n")
lines.append("5. TFC raw 保持原值，A raw 是否允许调整。\n")
lines.append("6. A 的 6 个 TFC cabbage 模型所有权与 TFC EUPL 授权链。\n")
lines.append("7. 蔬菜/油料/纤维双主产的产量分账口径。\n")

DOC.write_text("".join(lines), encoding="utf-8")
print("wrote", DOC, "rows", len(order), "bytes", DOC.stat().st_size)
