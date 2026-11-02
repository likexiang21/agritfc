from pathlib import Path
p=Path("mod_rebuild/docs/audit/OPEN-ISSUES.md"); t=p.read_text(encoding="utf-8")
t += """

## OPEN-054 其他功能严格评估 P2：掉落上下文与锅自动化（2026-10-31）

**状态：fixed-static / 待实机**

- ServingPlate/PlaceableFood getDrops 改用 loot 上下文捕获的 BE；
- CookingPan automationView 委托 addIngredient，漏斗食材进入 entries；
- build 成功；证据 docs/700、701。
"""
p.write_text(t,encoding="utf-8"); print("OPEN-054")
p=Path("mod_rebuild/docs/README.md"); t=p.read_text(encoding="utf-8")
needle="| [699-other-features-strict-eval-fixes-work-report-20261031.md](699-other-features-strict-eval-fixes-work-report-20261031.md) | 其他功能严格评估修复工作报告 |"
add="\n| [700-other-features-p2-drop-pan-20261031.md](700-other-features-p2-drop-pan-20261031.md) | 其他功能 P2 掉落/锅自动化修复 |\n| [701-other-features-p2-drop-pan-work-report-20261031.md](701-other-features-p2-drop-pan-work-report-20261031.md) | 其他功能 P2 修复工作报告 |"
if needle in t: t=t.replace(needle,needle+add); p.write_text(t,encoding="utf-8"); print("docs")
p=Path("mod_rebuild/README.md"); t=p.read_text(encoding="utf-8")
needle="- [699 号：其他功能严格评估修复工作报告](docs/699-other-features-strict-eval-fixes-work-report-20261031.md)"
add="\n- [700 号：其他功能 P2 掉落/锅自动化修复](docs/700-other-features-p2-drop-pan-20261031.md)\n- [701 号：其他功能 P2 修复工作报告](docs/701-other-features-p2-drop-pan-work-report-20261031.md)"
if needle in t: t=t.replace(needle,needle+add); p.write_text(t,encoding="utf-8"); print("root")
