from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-033 锅油勺只模拟不转移（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `PanInteractions.scoopOil` 使用 `tryFluidTransfer(..., false)`，只模拟；
- 副手油不减少、锅油罐不增加，可反复触发；
- 修复：改为 `true` 实际转移；
- build 成功；
- 证据：docs/660、661。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-033 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [659-seed-treatment-cancel-guards-fix-work-report-20261030.md](659-seed-treatment-cancel-guards-fix-work-report-20261030.md) | 种子处理右键取消检查修复工作报告 |"
add = "\n| [660-pan-oil-transfer-fix-20261030.md](660-pan-oil-transfer-fix-20261030.md) | 锅油勺实际转移修复 |\n| [661-pan-oil-transfer-fix-work-report-20261030.md](661-pan-oil-transfer-fix-work-report-20261030.md) | 锅油勺实际转移修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
