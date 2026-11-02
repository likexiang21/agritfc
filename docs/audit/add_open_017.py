from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-017 香料 herb 形态映射缺失（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `SpiceSpecies` 有 9 个 `herb` 形态；
- `AgricultureSpices.newSpiceCrop` 的 switch 没有 `case "herb"`，全部落入 vanilla `CropBlock`，`SpiceCropBlocks.Herb` 未使用；
- 修复：补 `case "herb"`；
- build 成功；
- 证据：docs/626、627。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-017 appended")
