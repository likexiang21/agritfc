from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-043 满份摆盘食物不返还整块（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- OPEN-042 后所有摆盘食物都只掉切片，满份也不返还整块；
- 修复：`PlaceableFoodBlockEntity` 增加 isFull，getDrops 满份返回方块物品，onRemove 满份不再 dropContents；
- build 成功；
- 证据：docs/680、681。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-043 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [679-placeable-food-loot-duplicate-fix-work-report-20261030.md](679-placeable-food-loot-duplicate-fix-work-report-20261030.md) | 摆盘食物掉落去重修复工作报告 |"
add = "\n| [680-placeable-food-full-return-fix-20261030.md](680-placeable-food-full-return-fix-20261030.md) | 满份摆盘食物返还整块修复 |\n| [681-placeable-food-full-return-fix-work-report-20261030.md](681-placeable-food-full-return-fix-work-report-20261030.md) | 满份摆盘食物返还整块修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
