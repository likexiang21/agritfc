from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-032 种子处理右键入口未检查取消（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `SeedTreatmentHandler` / `SeedTreatmentGrowthHandler` 未检查 `event.isCanceled()`；
- 取消场景下仍可能消耗材料、写组件、调度生长；
- 修复：两个入口增加取消早退；
- build 成功；
- 证据：docs/658、659。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-032 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [657-nursery-drop-seed-side-fix-work-report-20261030.md](657-nursery-drop-seed-side-fix-work-report-20261030.md) | 育苗盘客户端掉落种子修复工作报告 |"
add = "\n| [658-seed-treatment-cancel-guards-fix-20261030.md](658-seed-treatment-cancel-guards-fix-20261030.md) | 种子处理右键取消检查修复 |\n| [659-seed-treatment-cancel-guards-fix-work-report-20261030.md](659-seed-treatment-cancel-guards-fix-work-report-20261030.md) | 种子处理右键取消检查修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
