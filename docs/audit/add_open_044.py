from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-044 废枝叶/湿草/坚果壳未接入 TFC 堆肥标签（2026-10-31 全盘检查）

**状态：fixed-static / 待实机**

- 82 crop_waste、10 bush_waste、wet_grass、8 nut_shell 只有掉落/燃料，没有 TFC 堆肥标签；
- 修复：按文档 291 §4.1.2 分类追加到 `tfc:compost_greens/*` 与 `tfc:compost_browns/high`；
- 保留 TFC 原始 values；
- build 成功；
- 证据：docs/682、683。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-044 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [681-placeable-food-full-return-fix-work-report-20261030.md](681-placeable-food-full-return-fix-work-report-20261030.md) | 满份摆盘食物返还整块修复工作报告 |"
add = "\n| [682-compost-tags-full-audit-20261031.md](682-compost-tags-full-audit-20261031.md) | 废枝叶/湿草/坚果壳堆肥标签修复 |\n| [683-compost-tags-full-audit-work-report-20261031.md](683-compost-tags-full-audit-work-report-20261031.md) | 废枝叶/湿草/坚果壳堆肥标签修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
