from pathlib import Path
p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-050 严格评估 P0-2：B 香料/草莓无法在 TFC 耕地存活（2026-10-31）

**状态：fixed-static / 待实机**

- SpiceCropBlocks 6 形态 + STRAWBERRY_CROP 继承原版 CropBlock，mayPlaceOn 只接受 vanilla FarmBlock；
- TFC 耕地是 tfc:farmland/*，不是 vanilla FarmBlock；
- 修复：TfcFarmlandCropBlock 同时接受 FarmBlock 与 TFCTags.Blocks.FARMLANDS；
- 同时修 DirectSeedPlantingGate/SeedTreatmentGrowthHandler 的耕地判断、wild_crop 的 mature、wintergreen ID；
- build 成功；
- 证据：docs/692、693。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-050 appended")
p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [691-strict-eval-p0-p1-fixes-work-report-20261031.md](691-strict-eval-p0-p1-fixes-work-report-20261031.md) | 严格评估 P0/P1 修复工作报告 |"
add = "\n| [692-strict-eval-p0-2-tfc-farmland-20261031.md](692-strict-eval-p0-2-tfc-farmland-20261031.md) | 严格评估 P0-2 TFC 耕地修复 |\n| [693-strict-eval-p0-2-tfc-farmland-work-report-20261031.md](693-strict-eval-p0-2-tfc-farmland-work-report-20261031.md) | 严格评估 P0-2 TFC 耕地修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
p = Path("mod_rebuild/README.md")
t = p.read_text(encoding="utf-8")
needle = "- [691 号：严格评估 P0/P1 修复工作报告](docs/691-strict-eval-p0-p1-fixes-work-report-20261031.md)"
add = "\n- [692 号：严格评估 P0-2 TFC 耕地修复](docs/692-strict-eval-p0-2-tfc-farmland-20261031.md)\n- [693 号：严格评估 P0-2 TFC 耕地修复工作报告](docs/693-strict-eval-p0-2-tfc-farmland-work-report-20261031.md)"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("root links updated")
