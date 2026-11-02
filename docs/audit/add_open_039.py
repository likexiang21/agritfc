from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-039 种子处理生长 boost 未限制在农田（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `SeedTreatmentGrowthHandler` 只检查种子组件，不检查点击方块是否农田；
- 非农田/已有作物右击也可能触发 applyBoost；
- 修复：只允许 FarmBlock 或 ID 以 farmland 结尾的方块；
- build 成功；
- 证据：docs/672、673。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-039 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [671-block-list-dedupe-fix-work-report-20261030.md](671-block-list-dedupe-fix-work-report-20261030.md) | 方块全量列表去重修复工作报告 |"
add = "\n| [672-seed-growth-farmland-guard-20261030.md](672-seed-growth-farmland-guard-20261030.md) | 种子生长 boost 农田限制修复 |\n| [673-seed-growth-farmland-guard-work-report-20261030.md](673-seed-growth-farmland-guard-work-report-20261030.md) | 种子生长 boost 农田限制修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
