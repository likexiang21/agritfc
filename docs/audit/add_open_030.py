from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-030 育苗盘空盘拒绝所有种子（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `NurseryTrayBlockEntity.canAccept` 写成 `if (seed.isEmpty() || stack.isEmpty()) return false;`；
- 空托盘永远不能放入种子，已有种子反而可接受；
- 修复：改为 `if (!seed.isEmpty() || stack.isEmpty()) return false;`；
- build 成功；
- 证据：docs/654、655。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-030 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [653-cooking-pan-be-sync-fix-work-report-20261030.md](653-cooking-pan-be-sync-fix-work-report-20261030.md) | 锅方块实体同步修复工作报告 |"
add = "\n| [654-nursery-can-accept-fix-20261030.md](654-nursery-can-accept-fix-20261030.md) | 育苗盘 canAccept 条件修复 |\n| [655-nursery-can-accept-fix-work-report-20261030.md](655-nursery-can-accept-fix-work-report-20261030.md) | 育苗盘 canAccept 条件修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
