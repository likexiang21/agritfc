from pathlib import Path

p = Path("mod_rebuild/docs/audit/generate_291_v2.py")
t = p.read_text(encoding="utf-8")

# Stats rows after B new records count.
needle = 'lines.append("| B 新增记录合计 | 43 | 20 香料 + 8 坚果 + 15 蘑菇；蘑菇是栽培物，不是普通作物 |\\n")'
add = needle + '\nlines.append("| B 新增副产物物品 | 2 | `wet_grass` 潮湿草（可晒成 `tfc:straw`）+ `green_waste` 废枝叶（绿色堆肥） |\\n")'
if needle not in t:
    raise SystemExit("stats needle missing")
t = t.replace(needle, add)

# Production byproduct section after hard constraints.
needle = 'lines.append("\\n生产链硬约束：每物种主产品+副产品；每产物至少一个加工/使用出口；原有掉落不减少；未成熟破坏补偿；禁止死端。\\n")'
section = needle + r'''
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
lines.append("#### 4.1.2 废枝叶 `green_waste`\n")
lines.append("| 项 | 设计 |\n|---|---|\n")
lines.append("| 来源 | 叶菜外叶/老叶、果菜茎叶、根菜茎叶/皮渣、豆类藤蔓/豆荚、瓜类藤叶；按作物副产率 `extra_products` 产出 |\n")
lines.append("| 分类 | 叶菜/豆藤/嫩茎 → `tfc:compost_greens/high`；果菜茎叶/根菜皮 → `medium`；木质化茎/老藤 → `low`；晒干后的木质残体才进 `tfc:compost_browns/low` |\n")
lines.append("| 绿色堆肥 | 直接进 TFC `compost_greens/*`（不是 `browns`）；`replace=false` 只追加，不清空 TFC 条目 |\n")
lines.append("| 其它出口 | 可食用嫩叶（块茎类）、饲料、纤维、药用；不可食用部分才堆肥 |\n")
lines.append("| 防死物品 | 废枝叶统一为 `green_waste`（可带作物来源组件），必须有堆肥/饲料/燃料至少一个出口；不得为每作物造一个无用途垃圾物品 |\n")
lines.append("| 平衡 | 每作物副产 1–4 份；不挤占主产品；20 次收获均值验收 |\n")
'''
if needle not in t:
    raise SystemExit("production needle missing")
t = t.replace(needle, section)

# Harvest step mention.
t = t.replace("5. 收获：主产品+次产品；未成熟破坏补偿。",
              "5. 收获：主产品+次产品；未成熟破坏补偿 **`wet_grass` 潮湿草**；废枝叶产 **`green_waste`**。")

# Modification scope rows.
needle = 'lines.append("| 物品 | 处理种子、苗、扦插枝、种薯/种球、孢子/菌种 | 需定 B 新 ID 或 DataComponent |\\n")'
add = needle + '\nlines.append("| 副产物 | `wet_grass` 潮湿草、`green_waste` 废枝叶；`wet_grass`→`tfc:straw`；`green_waste`→`tfc:compost_greens/*` | 不新增死物品；不掉落链替换 TFC straw 用途 |\\n")'
if needle not in t:
    raise SystemExit("scope needle missing")
t = t.replace(needle, add)

# Batches.
t = t.replace('| P1 | 种子处理+育苗+移栽+缓苗；香料/坚果开始 | 六环节可执行、seedBack 达标 |',
              '| P1 | 种子处理+育苗+移栽+缓苗；`wet_grass` 野草掉落/干燥；`green_waste` 绿色堆肥标签；香料/坚果开始 | 六环节可执行、seedBack 达标 |')
t = t.replace('| P2 | 各 profile 初加工；蘑菇菌包；坚果去壳/榨油；香料干燥/研磨 | 每 profile 至少 1 完整链 |',
              '| P2 | 各 profile 初加工；蘑菇菌包；坚果去壳/榨油；香料干燥/研磨；潮湿草晒干/废枝叶堆肥验证 | 每 profile 至少 1 完整链 |')

# Open questions.
needle = 'lines.append("10. 坚果 acorn/chestnut 是挂树果实还是独立树作物；与 A/AFC 已有坚果如何避免重复。\\n")'
add = needle + '\nlines.append("11. 野草收割是否把所有非干枯草的 sharp 掉落改为 `wet_grass`（再晒成 straw），还是保留原 straw 并仅追加湿草分支；需定兼容口径。\\n")\nlines.append("12. 废枝叶是统一 `green_waste` 还是按作物族拆多种；堆肥档 high/medium/low 的最终分配需按 TFC 碳氮比实测校准。\\n")'
if needle not in t:
    raise SystemExit("open needle missing")
t = t.replace(needle, add)

p.write_text(t, encoding="utf-8")
print("wet grass / green waste added")
