from pathlib import Path
p=Path("mod_rebuild/docs/audit/OPEN-ISSUES.md"); t=p.read_text(encoding="utf-8")
t += """

## OPEN-052 严格评估 P1 收尾：放置覆盖、boost 目标校验、growthTickStep（2026-10-31）

**状态：fixed-static / 待实机**

- SeedlingItem/CormItem/SpiceRootItem 增加 canBeReplaced 检查，避免覆盖已有方块；
- SeedTreatmentGrowthHandler 只对种子生效、只对可替换目标、非直种不排队；
- 种子处理 boost 改用 TFC CropHelpers.growthTickStep，不再 setGrowth；
- build 成功；证据 docs/696、697。
"""
p.write_text(t,encoding="utf-8"); print("OPEN-052")
p=Path("mod_rebuild/docs/README.md"); t=p.read_text(encoding="utf-8")
needle="| [695-firmalife-full-coverage-boost-codec-work-report-20261031.md](695-firmalife-full-coverage-boost-codec-work-report-20261031.md) | Firmalife 全植物覆盖收尾工作报告 |"
add="\n| [696-strict-eval-p1-placement-boost-growth-20261031.md](696-strict-eval-p1-placement-boost-growth-20261031.md) | 严格评估 P1 放置/boost/growth 修复 |\n| [697-strict-eval-p1-placement-boost-growth-work-report-20261031.md](697-strict-eval-p1-placement-boost-growth-work-report-20261031.md) | 严格评估 P1 收尾工作报告 |"
if needle in t: t=t.replace(needle,needle+add); p.write_text(t,encoding="utf-8"); print("docs")
p=Path("mod_rebuild/README.md"); t=p.read_text(encoding="utf-8")
needle="- [695 号：Firmalife 全植物覆盖收尾工作报告](docs/695-firmalife-full-coverage-boost-codec-work-report-20261031.md)"
add="\n- [696 号：严格评估 P1 放置/boost/growth 修复](docs/696-strict-eval-p1-placement-boost-growth-20261031.md)\n- [697 号：严格评估 P1 收尾工作报告](docs/697-strict-eval-p1-placement-boost-growth-work-report-20261031.md)"
if needle in t: t=t.replace(needle,needle+add); p.write_text(t,encoding="utf-8"); print("root")
