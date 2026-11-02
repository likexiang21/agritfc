from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-028 盘子方块实体缺少客户端同步（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `ServingPlateBlockEntity` 直接继承 `BlockEntity`，没有 getUpdateTag/getUpdatePacket；
- 渲染器依赖 `plateStack`，客户端读不到，菜肴不可见；
- 修复：继承 `TFCBlockEntity`，set/clear 使用 `markForSync()`；
- build 成功；
- 证据：docs/650、651。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-028 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [649-lumber-pile-insert-all-fix-work-report-20261030.md](649-lumber-pile-insert-all-fix-work-report-20261030.md) | 木料堆 insert all 参数修复工作报告 |"
add = "\n| [650-serving-plate-be-sync-fix-20261030.md](650-serving-plate-be-sync-fix-20261030.md) | 盘子方块实体客户端同步修复 |\n| [651-serving-plate-be-sync-fix-work-report-20261030.md](651-serving-plate-be-sync-fix-work-report-20261030.md) | 盘子方块实体客户端同步修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
