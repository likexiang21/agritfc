from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-022 TFC 灌木废枝重复掉落（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `BushWasteHandler` 注册在 `BushHarvestHandler` 之前；
- 结果灌木破坏时前者先掉一份废枝，后者取消事件再掉一份；
- 修复：`BushWasteHandler` 跳过 `LIFECYCLE == FRUITING`，废枝只由采收处理器掉；
- build 成功；
- 证据：docs/638、639。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-022 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [637-bush-waste-harvest-fix-work-report-20261030.md](637-bush-waste-harvest-fix-work-report-20261030.md) | TFC 灌木采收废枝修复工作报告 |"
add = "\n| [638-bush-waste-duplicate-fix-20261030.md](638-bush-waste-duplicate-fix-20261030.md) | TFC 灌木废枝重复掉落修复 |\n| [639-bush-waste-duplicate-fix-work-report-20261030.md](639-bush-waste-duplicate-fix-work-report-20261030.md) | TFC 灌木废枝重复掉落修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
