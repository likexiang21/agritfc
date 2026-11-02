from pathlib import Path
import re

p = Path("mod_rebuild/docs/291-crop-system-complete-modification-20261028.md")
t = p.read_text(encoding="utf-8")

# Stats / note
t = t.replace("| B 新增蘑菇栽培 | 15 |", "| B 新增蘑菇 | 15 |")
t = t.replace("> 统计口径：A 87 与 TFC 29 是已有内容；8 香料是 Firmalife 搁置项接管/重建，2 坚果是 B 新物品/树产，7 蘑菇是 B 新菌包栽培物。",
              "> 统计口径：A 87 与 TFC 29 是已有内容；20 香料是 Firmalife 搁置项接管/重建，8 坚果是 B 新物品/树产 + 已有树叶状态，15 蘑菇含野生生成/刷新与可栽培 11/自然专用 4。")

# Rebuild 4.1.3 cleanly.
start = t.find("#### 4.1.3")
end = t.find("#### 4.1.4")
if start < 0 or end < 0:
    raise SystemExit("4.1.3 bounds missing")
a = ["millet", "foxtail_millet", "fonio", "spelt", "emmer", "einkorn",
     "pearl_millet", "finger_millet", "sorghum", "jobs_tears"]
tfc = ["barley", "oat", "rice", "rye", "wheat", "maize"]
rows = []
for crop in a + tfc:
    rows.append(f"| `{crop}` | {'A' if crop in a else 'TFC'} | `tfcagricultureplus:grain_bundle/{crop}` | 成熟收获 → 1–2 捆 + 种子 | 脱粒 → 谷粒 + 1–2 `tfcagricultureplus:wet_grass` | 1:1 晒干 → `tfc:straw` | 覆盖{'A' if crop in a else 'TFC'} 原收获 |")
new = """#### 4.1.3 谷物捆：湿草的加工来源

不是所有谷物都直接掉散粒：**A 10 + TFC 6 长秆谷物先收谷物捆，再脱粒**，脱粒副产才是湿草。

| 作物 | 来源 | 谷物捆物品 | 收获 | 脱粒 | 湿草/干燥 | 备注 |
|---|---|---|---|---|---|---|
""" + "\n".join(rows) + """

TFC 6 种（barley/oat/rice/rye/wheat/maize）**同样走 bundle→脱粒→wet_grass**，覆盖 TFC 原有直接掉谷粒/秸秆的收获流程。

非谷物捆：`buckwheat` / `amaranth` / `quinoa`；TFC `sugarcane` 不属于谷物捆。

"""
t = t[:start] + new + t[end:]

# TFC bushes wording: replace harvest/regrowth, not only resource.
t = t.replace("| TFC | **29 作物替换/覆盖种植+收获+掉落** + 10 灌木资源覆盖 | 先解决 A cabbage 所有权/EUPL；旧存档迁移/回退 |",
              "| TFC | **29 作物替换/覆盖种植+收获+掉落** + **10 灌木替换采收/再生** | 先解决 A cabbage 所有权/EUPL；旧存档迁移/回退 |")
t = t.replace("| 13 | TFC 10 灌木只做资源+采收/加工；草莓已是 A 普通作物 |",
              "| 13 | TFC 10 灌木替换采收/再生流程；草莓已是 A 普通作物 |")
t = t.replace("| P4 | TFC 29 种植/收获/掉落覆盖 + TFC 10 灌木接入 | 覆盖 TFC 原流程；存档迁移/回退方案同步验证 |",
              "| P4 | TFC 29 种植/收获/掉落覆盖 + TFC 10 灌木采收/再生覆盖 | 覆盖 TFC 原流程；存档迁移/回退方案同步验证 |")

p.write_text(t, encoding="utf-8")
print("291 table/scope fixed")
