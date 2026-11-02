from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-046 20 种香料废枝叶未接入堆肥（2026-10-31 全盘检查）

**状态：fixed-static / 待实机**

- `spice_waste/*` 20 项只有掉落，无配方/标签/堆肥；
- 修复：herb 9 种进 `compost_greens/high`，其余 11 种进 medium；
- build 成功；
- 证据：docs/686、687。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-046 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [685-nut-mushroom-food-def-data-work-report-20261031.md](685-nut-mushroom-food-def-data-work-report-20261031.md) | 坚果/坚果粉/蘑菇食物定义修复工作报告 |"
add = "\n| [686-spice-waste-compost-20261031.md](686-spice-waste-compost-20261031.md) | 香料废枝叶堆肥接入 |\n| [687-spice-waste-compost-work-report-20261031.md](687-spice-waste-compost-work-report-20261031.md) | 香料废枝叶堆肥接入工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
