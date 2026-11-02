from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
old = "## OPEN-010 金属罐交互/液体显示失效（用户 2026-10-29 第九个问题）\n\n**状态：recorded / 未处理**"
new = """## OPEN-010 金属罐交互/液体显示失效（用户 2026-10-29 第九个问题）

**状态：partially-fixed-static（P1-1，2026-10-29）/ 未实机**

- 19 个 metal can item model 改为 `tfc:fluid_container`；
- 新增 19 × 2 个 `.filled` 名称键；
- capability/tag/容量未改；
- 未实机验证装入/倒出/图标变化；
- 基础贴图仍借用 TFC 金属板/桶 overlay，属于视觉问题；
- 证据：docs/520、521。"""
if old not in t:
    raise SystemExit("anchor missing")
t = t.replace(old, new, 1)
p.write_text(t, encoding="utf-8")
print("OPEN-010 updated")
