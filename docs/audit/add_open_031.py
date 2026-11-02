from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-031 育苗盘客户端也掉落种子（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `NurseryTrayBlockEntity.dropSeed` 未检查 `level.isClientSide()`；
- 客户端移除方块时生成客户端幽灵物品并清空客户端 BE；
- 修复：非服务端直接 return；
- build 成功；
- 证据：docs/656、657。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-031 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [655-nursery-can-accept-fix-work-report-20261030.md](655-nursery-can-accept-fix-work-report-20261030.md) | 育苗盘 canAccept 条件修复工作报告 |"
add = "\n| [656-nursery-drop-seed-side-fix-20261030.md](656-nursery-drop-seed-side-fix-20261030.md) | 育苗盘客户端掉落种子修复 |\n| [657-nursery-drop-seed-side-fix-work-report-20261030.md](657-nursery-drop-seed-side-fix-work-report-20261030.md) | 育苗盘客户端掉落种子修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
