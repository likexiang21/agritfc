from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-035 副手锅铲搅拌损坏主手物品（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `CookingPanBlockEntity.stir` 固定扣 `EquipmentSlot.MAINHAND`；
- 副手锅铲不消耗耐久，主手物品被错扣；
- 修复：stir 接收 InteractionHand，按实际手选择槽；
- build 成功；
- 证据：docs/664、665。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-035 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [663-pan-rotten-ingredient-fix-work-report-20261030.md](663-pan-rotten-ingredient-fix-work-report-20261030.md) | 锅腐烂食材拒绝修复工作报告 |"
add = "\n| [664-pan-stir-hand-slot-fix-20261030.md](664-pan-stir-hand-slot-fix-20261030.md) | 锅铲手槽修复 |\n| [665-pan-stir-hand-slot-fix-work-report-20261030.md](665-pan-stir-hand-slot-fix-work-report-20261030.md) | 锅铲手槽修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
