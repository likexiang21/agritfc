from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-038 方块全量列表重复 drying rack（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `registerVariant` 已把 drying rack 放进 `ALL`；
- `all()` / `allIds()` 又追加 `DRYING_RACKS`，导致重复；
- 修复：只追加独立注册的 `TimberBlocks.ALL`；
- build 成功；
- 证据：docs/670、671。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-038 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [669-drying-rack-handler-copy-fix-work-report-20261030.md](669-drying-rack-handler-copy-fix-work-report-20261030.md) | 晾架自动化插入复制修复工作报告 |"
add = "\n| [670-block-list-dedupe-fix-20261030.md](670-block-list-dedupe-fix-20261030.md) | 方块全量列表去重修复 |\n| [671-block-list-dedupe-fix-work-report-20261030.md](671-block-list-dedupe-fix-work-report-20261030.md) | 方块全量列表去重修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
