from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-047 TFC/Firmalife 作物/植物被豁免（2026-10-31 用户要求）

**状态：fixed-static / 待实机**

- `DirectSeedPlantingGate` 对 `tfc:` 种子提前返回；育苗盘拒绝 TFC 种子；
- Firmalife 8 个香草植物不在 B 废枝叶链；
- 修复：
  - TFC 种子进入 CropPropagation 表，归 SEED_DIRECT；
  - 育苗盘 + SeedlingItem 支持 tfc:crop 解析；
  - 新增 FirmalifePlantWasteHandler 追加 spice_waste；
  - 未知外部种子不再静默取消；
- build 成功；
- 证据：docs/688、689。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-047 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [687-spice-waste-compost-work-report-20261031.md](687-spice-waste-compost-work-report-20261031.md) | 香料废枝叶堆肥接入工作报告 |"
add = "\n| [688-tfc-firmalife-no-exemption-20261031.md](688-tfc-firmalife-no-exemption-20261031.md) | 取消 TFC/Firmalife 作物与植物豁免 |\n| [689-tfc-firmalife-no-exemption-work-report-20261031.md](689-tfc-firmalife-no-exemption-work-report-20261031.md) | 取消 TFC/Firmalife 豁免工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")

p = Path("mod_rebuild/README.md")
t = p.read_text(encoding="utf-8")
needle = "- [687 号：香料废枝叶堆肥接入工作报告](docs/687-spice-waste-compost-work-report-20261031.md)"
add = "\n- [688 号：取消 TFC/Firmalife 作物与植物豁免](docs/688-tfc-firmalife-no-exemption-20261031.md)\n- [689 号：取消 TFC/Firmalife 豁免工作报告](docs/689-tfc-firmalife-no-exemption-work-report-20261031.md)"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("root links updated")
