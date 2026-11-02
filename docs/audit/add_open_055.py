from pathlib import Path
p=Path("mod_rebuild/docs/audit/OPEN-ISSUES.md"); t=p.read_text(encoding="utf-8")
t += """

## OPEN-055 其他功能 P2 清理：创造守卫/自检计数（2026-10-31）

**状态：fixed-static / 待实机**

- FirmalifePlantWasteHandler 加 CreativeGuards；
- 客户端渲染自检 total 加入香料作物与盘子；
- build 成功；证据 docs/702、703。
"""
p.write_text(t,encoding="utf-8"); print("OPEN-055")
p=Path("mod_rebuild/docs/README.md"); t=p.read_text(encoding="utf-8")
needle="| [701-other-features-p2-drop-pan-work-report-20261031.md](701-other-features-p2-drop-pan-work-report-20261031.md) | 其他功能 P2 修复工作报告 |"
add="\n| [702-other-features-p2-guards-count-20261031.md](702-other-features-p2-guards-count-20261031.md) | 其他功能 P2 守卫/自检修复 |\n| [703-other-features-p2-guards-count-work-report-20261031.md](703-other-features-p2-guards-count-work-report-20261031.md) | 其他功能 P2 清理工作报告 |"
if needle in t: t=t.replace(needle,needle+add); p.write_text(t,encoding="utf-8"); print("docs")
p=Path("mod_rebuild/README.md"); t=p.read_text(encoding="utf-8")
needle="- [701 号：其他功能 P2 修复工作报告](docs/701-other-features-p2-drop-pan-work-report-20261031.md)"
add="\n- [702 号：其他功能 P2 守卫/自检修复](docs/702-other-features-p2-guards-count-20261031.md)\n- [703 号：其他功能 P2 清理工作报告](docs/703-other-features-p2-guards-count-work-report-20261031.md)"
if needle in t: t=t.replace(needle,needle+add); p.write_text(t,encoding="utf-8"); print("root")
