from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-036 锅可加入腐烂黄油作固态油（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `addSolidOil` 只检查 firmalife:food/butter，未检查 `isRotten`；
- 修复：增加 `FoodCapability.isRotten` 拒绝；
- build 成功；
- 证据：docs/666、667。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-036 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [665-pan-stir-hand-slot-fix-work-report-20261030.md](665-pan-stir-hand-slot-fix-work-report-20261030.md) | 锅铲手槽修复工作报告 |"
add = "\n| [666-pan-rotten-butter-fix-20261030.md](666-pan-rotten-butter-fix-20261030.md) | 锅腐烂黄油拒绝修复 |\n| [667-pan-rotten-butter-fix-work-report-20261030.md](667-pan-rotten-butter-fix-work-report-20261030.md) | 锅腐烂黄油拒绝修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
