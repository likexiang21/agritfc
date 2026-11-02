from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-041 创造模式吃盘仍消耗/改份数（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `DishEating.eatFromPlateBlock` / `finishItemUse` 未检查 instabuild；
- 创造模式吃菜仍扣盘/改 dish 份数；
- 修复：两入口在 dish 合法后提前返回；
- build 成功；
- 证据：docs/676、677。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-041 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [675-stacked-plate-eating-fix-work-report-20261030.md](675-stacked-plate-eating-fix-work-report-20261030.md) | 堆叠盘子食用修复工作报告 |"
add = "\n| [676-creative-dish-eating-fix-20261030.md](676-creative-dish-eating-fix-20261030.md) | 创造模式吃盘不消耗修复 |\n| [677-creative-dish-eating-fix-work-report-20261030.md](677-creative-dish-eating-fix-work-report-20261030.md) | 创造模式吃盘不消耗修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
