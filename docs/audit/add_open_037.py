from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-037 晾架自动化插入直接别名调用方物品栈（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `RackItemHandler.insertItem` 把调用方 stack 直接交给 `ItemStackHandler`；
- 空槽实际插入时可能别名同一对象；
- 修复：先 `stack.copy()` 再插入；
- build 成功；
- 证据：docs/668、669。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-037 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [667-pan-rotten-butter-fix-work-report-20261030.md](667-pan-rotten-butter-fix-work-report-20261030.md) | 锅腐烂黄油拒绝修复工作报告 |"
add = "\n| [668-drying-rack-handler-copy-fix-20261030.md](668-drying-rack-handler-copy-fix-20261030.md) | 晾架自动化插入复制修复 |\n| [669-drying-rack-handler-copy-fix-work-report-20261030.md](669-drying-rack-handler-copy-fix-work-report-20261030.md) | 晾架自动化插入复制修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
