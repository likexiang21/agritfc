from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-042 摆盘食物破坏时整块与切片同时掉落（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `PlaceableFoodBlock` 默认 loot table 掉整块，`onRemove` 又掉剩余切片；
- 修复：`getDrops` 返回空，剩余食物只由 BE dropContents 掉；
- build 成功；
- 证据：docs/678、679。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-042 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [677-creative-dish-eating-fix-work-report-20261030.md](677-creative-dish-eating-fix-work-report-20261030.md) | 创造模式吃盘不消耗修复工作报告 |"
add = "\n| [678-placeable-food-loot-duplicate-fix-20261030.md](678-placeable-food-loot-duplicate-fix-20261030.md) | 摆盘食物掉落去重修复 |\n| [679-placeable-food-loot-duplicate-fix-work-report-20261030.md](679-placeable-food-loot-duplicate-fix-work-report-20261030.md) | 摆盘食物掉落去重修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
