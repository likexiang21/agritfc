from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-023 右键/左键交互未检查已取消事件（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `BushRightClickHarvestHandler`、`DirectSeedPlantingGate`、`CuttingBoardLeftClickHandler`、`InWorldRecipeHandler` 未检查 `event.isCanceled()`；
- 保护/取消场景下仍可能收获、取消种植或执行世界内配方；
- 修复：统一增加取消早退；
- build 成功；
- 证据：docs/640、641。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-023 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [639-bush-waste-duplicate-fix-work-report-20261030.md](639-bush-waste-duplicate-fix-work-report-20261030.md) | TFC 灌木废枝重复掉落修复工作报告 |"
add = "\n| [640-interaction-cancel-guards-fix-20261030.md](640-interaction-cancel-guards-fix-20261030.md) | 交互入口取消检查修复 |\n| [641-interaction-cancel-guards-fix-work-report-20261030.md](641-interaction-cancel-guards-fix-work-report-20261030.md) | 交互入口取消检查修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
