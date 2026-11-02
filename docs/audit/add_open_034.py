from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-034 锅可直接加入腐烂食材（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `isItemValid` 拒绝腐烂，但玩家右键走 `addIngredient`，该方法只检查 `FoodCapability.has`；
- 修复：`addIngredient` 增加 `isRotten` 检查；
- build 成功；
- 证据：docs/662、663。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-034 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [661-pan-oil-transfer-fix-work-report-20261030.md](661-pan-oil-transfer-fix-work-report-20261030.md) | 锅油勺实际转移修复工作报告 |"
add = "\n| [662-pan-rotten-ingredient-fix-20261030.md](662-pan-rotten-ingredient-fix-20261030.md) | 锅腐烂食材拒绝修复 |\n| [663-pan-rotten-ingredient-fix-work-report-20261030.md](663-pan-rotten-ingredient-fix-work-report-20261030.md) | 锅腐烂食材拒绝修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
