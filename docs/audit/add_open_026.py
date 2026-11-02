from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-026 木料堆取空后残留空方块（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `LumberPileBlockEntity.updateState` 将 count 强制为至少 1；
- 取走最后一块木料后留下空库存方块，且破坏无掉落；
- 修复：库存为 0 时 `level.removeBlock(worldPosition, false)`；
- build 成功；
- 证据：docs/646、647。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-026 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [645-spice-crop-codec-fix-work-report-20261030.md](645-spice-crop-codec-fix-work-report-20261030.md) | 香料作物形状子类 codec 修复工作报告 |"
add = "\n| [646-lumber-pile-empty-removal-fix-20261030.md](646-lumber-pile-empty-removal-fix-20261030.md) | 木料堆空方块移除修复 |\n| [647-lumber-pile-empty-removal-fix-work-report-20261030.md](647-lumber-pile-empty-removal-fix-work-report-20261030.md) | 木料堆空方块移除修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
