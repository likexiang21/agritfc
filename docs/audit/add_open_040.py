from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-040 堆叠盘子食用会丢盘/状态串改（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `DishEating.finishItemUse` 对堆叠盘调用 `setCount(1)` 丢盘；
- `PanDishData.write(stack, rest)` 改整堆份数；
- 修复：堆叠时拆一张盘子、原 stack shrink(1)、单盘写 rest/清空后放回背包；
- build 成功；
- 证据：docs/674、675。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-040 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [673-seed-growth-farmland-guard-work-report-20261030.md](673-seed-growth-farmland-guard-work-report-20261030.md) | 种子生长 boost 农田限制修复工作报告 |"
add = "\n| [674-stacked-plate-eating-fix-20261030.md](674-stacked-plate-eating-fix-20261030.md) | 堆叠盘子食用修复 |\n| [675-stacked-plate-eating-fix-work-report-20261030.md](675-stacked-plate-eating-fix-work-report-20261030.md) | 堆叠盘子食用修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
