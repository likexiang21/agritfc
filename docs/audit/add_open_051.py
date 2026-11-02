from pathlib import Path
p=Path("mod_rebuild/docs/audit/OPEN-ISSUES.md"); t=p.read_text(encoding="utf-8")
t += """

## OPEN-051 严格评估收尾：Firmalife 全植物覆盖 + 种子处理 BE（2026-10-31）

**状态：fixed-static / 待实机**

- 新增 14 个 Firmalife crop_waste（cocoa/fig/grape/pineapple/nightshade 等），覆盖 12 个 plant/* + 2 个 grape_string_plant_*；
- 8 香草保留 spice_waste + 刀具门槛；
- 种子处理 boost 对 A/TFC 支持的 CropBlockEntity 直接 setGrowth；
- TfcFarmlandCropBlock 增加 codec；
- build 成功；证据 docs/694、695。
"""
p.write_text(t,encoding="utf-8"); print("OPEN-051")
p=Path("mod_rebuild/docs/README.md"); t=p.read_text(encoding="utf-8")
needle="| [693-strict-eval-p0-2-tfc-farmland-work-report-20261031.md](693-strict-eval-p0-2-tfc-farmland-work-report-20261031.md) | 严格评估 P0-2 TFC 耕地修复工作报告 |"
add="\n| [694-firmalife-full-coverage-boost-codec-20261031.md](694-firmalife-full-coverage-boost-codec-20261031.md) | Firmalife 全植物覆盖、种子处理 BE、codec |\n| [695-firmalife-full-coverage-boost-codec-work-report-20261031.md](695-firmalife-full-coverage-boost-codec-work-report-20261031.md) | Firmalife 全植物覆盖收尾工作报告 |"
if needle in t: t=t.replace(needle,needle+add); p.write_text(t,encoding="utf-8"); print("docs")
p=Path("mod_rebuild/README.md"); t=p.read_text(encoding="utf-8")
needle="- [693 号：严格评估 P0-2 TFC 耕地修复工作报告](docs/693-strict-eval-p0-2-tfc-farmland-work-report-20261031.md)"
add="\n- [694 号：Firmalife 全植物覆盖、种子处理 BE、codec](docs/694-firmalife-full-coverage-boost-codec-20261031.md)\n- [695 号：Firmalife 全植物覆盖收尾工作报告](docs/695-firmalife-full-coverage-boost-codec-work-report-20261031.md)"
if needle in t: t=t.replace(needle,needle+add); p.write_text(t,encoding="utf-8"); print("root")
