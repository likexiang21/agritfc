from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-048 严格评估 P0：统一收获器把 BlockEntity 传成 null（2026-10-31）

**状态：fixed-static / 待实机**

- `UnifiedCropHarvestHandler` 取消玩家破坏后自行补掉落；
- `Block.getDrops(..., null, ...)` 导致 TFC `crop_yield_uniform` 读不到 CropBlockEntity，回落到 min=0；
- 影响 A 76 + TFC 19 个非谷类物种；
- 修复：传 `level.getBlockEntity(pos)`；
- 证据：docs/690、691。

## OPEN-049 严格评估 P1：TFC/Firmalife 覆盖与提示缺口（2026-10-31）

**状态：部分修复 / 仍待处理**

- TFC 前缀豁免改为逐项查表，补 TFC 11 + A 10 分类；
- cane/strawberry/wild_crop 废枝叶补漏；
- 播种门加育苗提示；
- Firmalife 8 香草改为刀具门槛且不重复掉 B 产物；
- **未完成**：Firmalife 另外 12 个 plant 方块仍无 B 侧钩子；
- 证据：docs/690、691。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-048/049 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [689-tfc-firmalife-no-exemption-work-report-20261031.md](689-tfc-firmalife-no-exemption-work-report-20261031.md) | 取消 TFC/Firmalife 豁免工作报告 |"
add = "\n| [690-strict-eval-p0-p1-fixes-20261031.md](690-strict-eval-p0-p1-fixes-20261031.md) | 严格评估 P0/P1 修复 |\n| [691-strict-eval-p0-p1-fixes-work-report-20261031.md](691-strict-eval-p0-p1-fixes-work-report-20261031.md) | 严格评估 P0/P1 修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")

p = Path("mod_rebuild/README.md")
t = p.read_text(encoding="utf-8")
needle = "- [689 号：取消 TFC/Firmalife 豁免工作报告](docs/689-tfc-firmalife-no-exemption-work-report-20261031.md)"
add = "\n- [690 号：严格评估 P0/P1 修复](docs/690-strict-eval-p0-p1-fixes-20261031.md)\n- [691 号：严格评估 P0/P1 修复工作报告](docs/691-strict-eval-p0-p1-fixes-work-report-20261031.md)"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("root links updated")
