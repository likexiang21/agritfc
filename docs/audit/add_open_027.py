from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-027 木料堆 insert all 参数未生效（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `LumberPileBlockEntity.insert` 无论 `all` 真假都只插入 1；
- 修复：`amount = min(held.count, all ? available : 1)`；
- build 成功；
- 证据：docs/648、649。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-027 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [647-lumber-pile-empty-removal-fix-work-report-20261030.md](647-lumber-pile-empty-removal-fix-work-report-20261030.md) | 木料堆空方块移除修复工作报告 |"
add = "\n| [648-lumber-pile-insert-all-fix-20261030.md](648-lumber-pile-insert-all-fix-20261030.md) | 木料堆 insert all 参数修复 |\n| [649-lumber-pile-insert-all-fix-work-report-20261030.md](649-lumber-pile-insert-all-fix-work-report-20261030.md) | 木料堆 insert all 参数修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
