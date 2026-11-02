from pathlib import Path

p = Path("mod_rebuild/docs/291-crop-system-complete-modification-20261028.md")
t = p.read_text(encoding="utf-8")
t = t.replace("**不产 crop_waste 的 A/TFC 作物**（共 35 条）：", "**不产 crop_waste 的 A/TFC 作物**（共 34 条）：")
t = t.replace("因此 **crop_waste 总数 = 81（A/TFC）+ 20（B 香料）= 101**，不是 159。",
              "因此 **crop_waste 总数 = 82（A/TFC）+ 20（B 香料）= 102**，不是 159。")
t = t.replace("| 副产物物品 | 1 + 16 + 101 |", "| 副产物物品 | 1 + 16 + 102 |")
t = t.replace("（101，按实际副产）", "（102，按实际副产）")
t = t.replace("| 12 | 废枝叶按实际加工；仅 101 条有 `crop_waste`", "| 12 | 废枝叶按实际加工；仅 102 条有 `crop_waste`")
# Insert cabbage into the waste table right after napa_cabbage.
needle = "| `napa_cabbage` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/napa_cabbage` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |"
row = "| `napa_cabbage` | A·叶菜/茎菜 | `tfcagricultureplus:crop_waste/napa_cabbage` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |\n| `cabbage` | TFC·叶菜/饲草 | `tfcagricultureplus:crop_waste/cabbage` | 外叶/老叶 | `tfc:compost_greens/high` | 饲料/堆肥；部分可腌 |"
if needle not in t:
    raise SystemExit("291 napa row missing")
t = t.replace(needle, row)
p.write_text(t, encoding="utf-8")

p = Path("mod_rebuild/docs/292-crop-open-issues-decisions-20261028.md")
t = p.read_text(encoding="utf-8")
t = t.replace("101 条有 crop_waste", "102 条有 crop_waste")
t = t.replace("约 **101**（A 64 + TFC 17 + B 香料 20）", "约 **102**（A 64 + TFC 18 + B 香料 20）")
t = t.replace("- `crop_waste` 数量约 **101**（A 64 + TFC 17 + B 香料 20），不是 159；",
              "- `crop_waste` 数量约 **102**（A 64 + TFC 18 + B 香料 20），不是 159；")
t = t.replace("101 个 crop_waste", "102 个 crop_waste")
p.write_text(t, encoding="utf-8")

p = Path("mod_rebuild/docs/293-crop-code-implementation-technical-20261028.md")
t = p.read_text(encoding="utf-8").replace("101 个 `crop_waste`", "102 个 `crop_waste`")
p.write_text(t, encoding="utf-8")

for name in ("294-crop-p0a-work-report-20261028.md", "296-crop-p0b-work-report-20261028.md"):
    p = Path("mod_rebuild/docs") / name
    t = p.read_text(encoding="utf-8").replace("101 个 crop_waste", "102 个 crop_waste").replace("101 个 `crop_waste`", "102 个 `crop_waste`")
    p.write_text(t, encoding="utf-8")

print("docs counts and cabbage row updated")
