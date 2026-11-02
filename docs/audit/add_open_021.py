from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-021 TFC 灌木采收不产废枝（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `BushHarvestHandler` / `BushRightClickHarvestHandler` 采收成功后没有掉 `bush_waste`；
- 上一轮取消检查使 `BushWasteHandler` 不再补掉落；
- 修复：两个采收处理器成功后追加 `bush_waste`；
- build 成功；
- 证据：docs/636、637。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-021 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [635-spice-seed-source-filter-fix-work-report-20261030.md](635-spice-seed-source-filter-fix-work-report-20261030.md) | 野草香料种子源过滤修复工作报告 |"
add = "\n| [636-bush-waste-harvest-fix-20261030.md](636-bush-waste-harvest-fix-20261030.md) | TFC 灌木采收废枝修复 |\n| [637-bush-waste-harvest-fix-work-report-20261030.md](637-bush-waste-harvest-fix-work-report-20261030.md) | TFC 灌木采收废枝修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
