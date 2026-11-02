from pathlib import Path

p = Path("mod_rebuild/docs/291-crop-system-complete-modification-20261028.md")
t = p.read_text(encoding="utf-8")
# Fix accidental double-backtick in waste table cells.
t = t.replace("``tfc:compost", "`tfc:compost")
# Update wet grass sources to put grain bundle first.
old = "| 来源 1 | 13 种 TFC 野生草（beachgrass · bluegrass · bromegrass · fountain_grass · orchard_grass · pampas_grass · raddia_grass · red_oat_grass · ryegrass · scutch_grass · switchgrass · tall_fescue_grass · timothy_grass）在非干枯状态被收割 |"
new = "| 来源 1 | **A 的 10 种长秆谷物**成熟收获 → `grain_bundle/<crop>` → 脱粒 → 谷粒 + `wet_grass`；这是主路径（见 4.1.3） |"
if old not in t:
    raise SystemExit("wet source line missing")
t = t.replace(old, new)
t = t.replace("| 来源 2 | 未成熟作物被破坏时通过 `tfc:extra_products` 补偿产出 |",
              "| 来源 2 | 13 种 TFC 野生草（beachgrass · bluegrass · bromegrass · fountain_grass · orchard_grass · pampas_grass · raddia_grass · red_oat_grass · ryegrass · scutch_grass · switchgrass · tall_fescue_grass · timothy_grass）在非干枯状态被收割 |\n"
              "| 来源 3 | 未成熟作物被破坏时通过 `tfc:extra_products` 补偿产出 |")
p.write_text(t, encoding="utf-8")

p = Path("mod_rebuild/docs/292-crop-open-issues-decisions-20261028.md")
t = p.read_text(encoding="utf-8")
t = t.replace("102 条有 crop_waste", "101 条有 crop_waste")
t = t.replace("约 **102**（A 64 + TFC 18 + B 香料 20），不是 159", "约 **101**（A 64 + TFC 17 + B 香料 20），不是 159")
t = t.replace("A 64 + TFC 18 + B 香料 20", "A 64 + TFC 17 + B 香料 20")
t = t.replace("102 个 crop_waste", "101 个 crop_waste")
p.write_text(t, encoding="utf-8")
print("wet source/double-backtick/292 counts corrected")
