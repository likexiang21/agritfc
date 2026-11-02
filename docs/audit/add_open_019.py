from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-019 育苗盘接受 TFC 种子但无法移栽（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `NurseryTrayBlockEntity.canAccept` 只检查种子路径，TFC 种子也能放入；
- `SeedlingItem` 只接受 BlockItem，TFC 种子不是 B 作物 BlockItem，移栽失败；
- 修复：canAccept 拒绝 `tfc:` 种子，TFC 保持原版直播；
- build 成功；
- 证据：docs/630、631。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-019 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [629-event-cancel-guards-fix-work-report-20261030.md](629-event-cancel-guards-fix-work-report-20261030.md) | 事件处理器取消状态检查修复工作报告 |"
add = "\n| [630-nursery-tfc-seed-reject-fix-20261030.md](630-nursery-tfc-seed-reject-fix-20261030.md) | 育苗盘 TFC 种子拒绝修复 |\n| [631-nursery-tfc-seed-reject-fix-work-report-20261030.md](631-nursery-tfc-seed-reject-fix-work-report-20261030.md) | 育苗盘 TFC 种子拒绝修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
