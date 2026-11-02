from pathlib import Path

p = Path("mod_rebuild/docs/audit/generate_291_v2.py")
t = p.read_text(encoding="utf-8")

defs = '''bundle_crops = [
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
'''
if "bundle_crops =" not in t:
    t = t.replace("lines = []\n", defs + "lines = []\n", 1)

# Stats generic line
t = t.replace('lines.append("| B 新增副产物物品 | 2 | `wet_grass` 潮湿草（可晒成 `tfc:straw`）+ `green_waste` 废枝叶（绿色堆肥） |\\n")',
              'lines.append("| 副产物物品 | 1 + 16 + 159 | `wet_grass`（1）+ `grain_bundle/<crop>`（16）+ `crop_waste/<crop>`（159）；坚果壳/菌渣另算 |\\n")')

# Replace section by line indices.
lines = t.splitlines()
start = next(i for i, l in enumerate(lines) if "#### 4.1.2" in l)
end = next(i for i, l in enumerate(lines) if "## 5. 培育链" in l)
new = [
    'lines.append("#### 4.1.2 废枝叶：逐作物专属，不设通用 `green_waste`\\n")',
    'lines.append("“废枝叶”只是统称，**每个作物一个专属物品 `crop_waste/<crop>`**，不能用一个通用 `green_waste` 覆盖全部。下面逐作物给出类型、堆肥档与其它出口。\\n")',
    'lines.append("| 作物 | 来源/组 | 废枝叶物品 | 类型 | 堆肥档 | 其它出口 |\\n")',
    'lines.append("|---|---|---|---|---|---|\\n")',
    'for crop, sg in order:',
    '    group = sg.split("·", 1)[1] if "·" in sg else sg',
    '    wtype, tag, alt = waste_override.get(crop, waste_group.get(group, ("茎叶残渣", "tfc:compost_greens/medium", "堆肥/饲料")))',
    '    lines.append(f"| `{crop}` | {sg} | `tfcagricultureplus:crop_waste/{crop}` | {wtype} | `{tag}` | {alt} |\\n")',
    'lines.append("#### 4.1.3 谷物捆：湿草的加工来源\\n")',
    'lines.append("不是所有谷物都直接掉散粒：**长秆谷物先收谷物捆，再脱粒**，脱粒副产才是湿草。\\n")',
    'lines.append("| 作物 | 来源 | 谷物捆物品 | 收获 | 脱粒 | 湿草/干燥 | 备注 |\\n")',
    'lines.append("|---|---|---|---|---|---|---|\\n")',
    'for crop in bundle_crops:',
    '    src = "A" if crop in a_group_of else "TFC"',
    '    lines.append(f"| `{crop}` | {src} | `tfcagricultureplus:grain_bundle/{crop}` | 成熟收获 → 1–2 捆 + 种子 | 脱粒 → 谷粒 + 1–2 `wet_grass` | `wet_grass` 1:1 晒干 → `tfc:straw` | 主产品仍是谷粒；不减少原有谷粒 |\\n")',
    'lines.append("非谷物捆（直接脱粒/散粒）：" + " · ".join("`" + c + "`" for c in non_bundle_grains) + "；TFC 的 `sugarcane` 不属于谷物捆。\\n")',
    'lines.append("**TFC 兼容**：TFC 29 的 raw 掉落建议不直接改；TFC 谷物是否改走 `grain_bundle` 需单批确认。A 的谷物捆可先落地。\\n")',
    'lines.append("#### 4.1.4 废枝叶/菌渣/坚果壳的边界\\n")',
    'lines.append("- 坚果壳：不是“绿色废枝叶”，单独走 `nut_shell/<nut>` → `tfc:compost_browns/high` / 燃料；\\n")',
    'lines.append("- 蘑菇废菌包：`spent_substrate` → `tfc:compost_browns/medium` / 堆肥，不算绿色枝叶；\\n")',
    'lines.append("- 香料废枝叶：`crop_waste/<spice>` → 按 `compost_greens/high|medium`；\\n")',
    'lines.append("- 所有 `crop_waste` / 壳 / 菌渣必须有堆肥/饲料/燃料/纸至少一个出口，不得造死物品。\\n")',
    '',
]
lines[start:end] = new
t = "\n".join(lines) + "\n"

# Step, scope, batch, open q textual replacements.
t = t.replace("废枝叶产 **`green_waste`**", "废枝叶产 **逐作物 `crop_waste/<crop>`**；谷物按 4.1.3 先出谷物捆，脱粒产 `wet_grass`")
t = t.replace('| 副产物 | `wet_grass` 潮湿草、`green_waste` 废枝叶；`wet_grass`→`tfc:straw`；`green_waste`→`tfc:compost_greens/*` | 不新增死物品；不掉落链替换 TFC straw 用途 |',
              '| 副产物 | `wet_grass`；`grain_bundle/<crop>`；每作物 `crop_waste/<crop>`；坚果壳/菌渣另计 | 不设通用废枝叶；湿草来自谷物捆脱粒/野草/未成熟补偿；堆肥按作物分档 |')
t = t.replace("`wet_grass` 野草掉落/干燥；`green_waste` 绿色堆肥标签；香料/坚果开始",
              "`wet_grass` 野草/谷物捆脱粒/干燥；逐作物 `crop_waste` 绿色堆肥标签；香料/坚果开始")
t = t.replace("12. 废枝叶是统一 `green_waste` 还是按作物族拆多种；堆肥档 high/medium/low 的最终分配需按 TFC 碳氮比实测校准。",
              "12. 废枝叶已定为**逐作物 `crop_waste/<crop>`**；high/medium/low 的最终分配需按 TFC 碳氮比实测校准，不能用一个通用物品替代。")
t = t.replace("11. 野草收割是否把所有非干枯草的 sharp 掉落改为 `wet_grass`（再晒成 straw），还是保留原 straw 并仅追加湿草分支；需定兼容口径。",
              "11. 野草收割是否把所有非干枯草的 sharp 掉落改为 `wet_grass`（再晒成 straw），还是保留原 straw 并仅追加湿草分支；同时需定 TFC 谷物是否改走 `grain_bundle`。")

p.write_text(t, encoding="utf-8")
print("patched per-crop waste + grain bundle")
