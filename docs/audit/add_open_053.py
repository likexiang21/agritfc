from pathlib import Path
p=Path("mod_rebuild/docs/audit/OPEN-ISSUES.md"); t=p.read_text(encoding="utf-8")
t += """

## OPEN-053 其他功能严格评估 P0/P1（2026-10-31）

**状态：fixed-static / 待实机**

- P0 worldgen biome 标签只含 vanilla，TFC 世界不生成蘑菇/坚果树/香料树；已加 85 个 TFC 陆生 biome；
- P1 厨房食物过滤改用 FoodCapability.has；
- P1 锅铲勺油 tryFluidTransfer 参数顺序修正；
- P1 lang 斜杠键改点号；
- P1 菌包/育苗盘 stage 模型区分；
- 证据 docs/698、699。
"""
p.write_text(t,encoding="utf-8"); print("OPEN-053")
p=Path("mod_rebuild/docs/README.md"); t=p.read_text(encoding="utf-8")
needle="| [697-strict-eval-p1-placement-boost-growth-work-report-20261031.md](697-strict-eval-p1-placement-boost-growth-work-report-20261031.md) | 严格评估 P1 收尾工作报告 |"
add="\n| [698-other-features-strict-eval-fixes-20261031.md](698-other-features-strict-eval-fixes-20261031.md) | 其他功能严格评估 P0/P1 修复 |\n| [699-other-features-strict-eval-fixes-work-report-20261031.md](699-other-features-strict-eval-fixes-work-report-20261031.md) | 其他功能严格评估修复工作报告 |"
if needle in t: t=t.replace(needle,needle+add); p.write_text(t,encoding="utf-8"); print("docs")
p=Path("mod_rebuild/README.md"); t=p.read_text(encoding="utf-8")
needle="- [697 号：严格评估 P1 收尾工作报告](docs/697-strict-eval-p1-placement-boost-growth-work-report-20261031.md)"
add="\n- [698 号：其他功能严格评估 P0/P1 修复](docs/698-other-features-strict-eval-fixes-20261031.md)\n- [699 号：其他功能严格评估修复工作报告](docs/699-other-features-strict-eval-fixes-work-report-20261031.md)"
if needle in t: t=t.replace(needle,needle+add); p.write_text(t,encoding="utf-8"); print("root")
