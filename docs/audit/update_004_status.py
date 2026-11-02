from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
old = "## OPEN-004 全部工作方块没有合成表，家具只有低质量占位配方（用户 2026-10-29 第三个问题）\n\n**状态：recorded / 未处理**"
new = """## OPEN-004 全部工作方块没有合成表，家具只有低质量占位配方（用户 2026-10-29 第三个问题）

**状态：partially-fixed-static（P0-3，2026-10-29）/ 未实机**

- 已补 174 个工作方块配方 + 174 个 loot table；
- 覆盖 log_cutting_board / cutting_board（木/石）/ knife_block / drying_rack / mortar / cooking_pan / silkworm_rack；
- `lumber_pile` 为放置设备，不伪造 crafting 配方；
- 家具 204 个占位配方仍在，且 `food_display` 与 `sink_cabinet` 的 shaped 配方完全相同，留 P1；
- 未实机验证 TFC workbench 匹配。
- 证据：docs/516、517。"""
if old not in t:
    raise SystemExit("anchor missing")
t = t.replace(old, new, 1)
p.write_text(t, encoding="utf-8")
print("OPEN-004 updated")
