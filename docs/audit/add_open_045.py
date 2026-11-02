from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-045 坚果/坚果粉/野生蘑菇没有食物定义（2026-10-31 全盘检查）

**状态：fixed-static / 待实机**

- 8 坚果、8 ground_nut、15 wild_mushroom BlockItem 在 `tfc/food` 无定义；
- `FoodCapability.has` 为 false，不能食用/不进入腐烂营养链；
- 修复：新增 31 个 FoodDefinition；
- build 成功；
- 证据：docs/684、685。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-045 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [683-compost-tags-full-audit-work-report-20261031.md](683-compost-tags-full-audit-work-report-20261031.md) | 废枝叶/湿草/坚果壳堆肥标签修复工作报告 |"
add = "\n| [684-nut-mushroom-food-def-data-20261031.md](684-nut-mushroom-food-def-data-20261031.md) | 坚果/坚果粉/蘑菇食物定义修复 |\n| [685-nut-mushroom-food-def-data-work-report-20261031.md](685-nut-mushroom-food-def-data-work-report-20261031.md) | 坚果/坚果粉/蘑菇食物定义修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
