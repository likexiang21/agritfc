from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-029 锅方块实体渲染内容不同步（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `CookingPanBlockEntity.sync()` 只发方块状态更新，不发 BlockEntity 数据；
- 客户端渲染器读不到 entries，锅里食材不可见；
- 修复：改用 `TFCBlockEntity.markForSync()`；
- build 成功；
- 证据：docs/652、653。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-029 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [651-serving-plate-be-sync-fix-work-report-20261030.md](651-serving-plate-be-sync-fix-work-report-20261030.md) | 盘子方块实体客户端同步修复工作报告 |"
add = "\n| [652-cooking-pan-be-sync-fix-20261030.md](652-cooking-pan-be-sync-fix-20261030.md) | 锅方块实体同步修复 |\n| [653-cooking-pan-be-sync-fix-work-report-20261030.md](653-cooking-pan-be-sync-fix-work-report-20261030.md) | 锅方块实体同步修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
