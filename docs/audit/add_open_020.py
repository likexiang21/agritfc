from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-020 野草香料种子源包含无种子树种（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `SpiceSeedDropHandler` 从全部 20 个 SpiceSpecies 随机；
- 5 个 tree 形态无 `AgricultureSpices.SEEDS` 条目，掉落被静默跳过；
- 修复：只从 `SEEDS.containsKey` 的物种随机；
- build 成功；
- 证据：docs/634、635。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-020 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [633-jei-guard-failure-handling-work-report-20261030.md](633-jei-guard-failure-handling-work-report-20261030.md) | JEI 兼容保护自身失败处理工作报告 |"
add = "\n| [634-spice-seed-source-filter-fix-20261030.md](634-spice-seed-source-filter-fix-20261030.md) | 野草香料种子源过滤修复 |\n| [635-spice-seed-source-filter-fix-work-report-20261030.md](635-spice-seed-source-filter-fix-work-report-20261030.md) | 野草香料种子源过滤修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
