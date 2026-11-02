from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
old = "## OPEN-001 两种枯死灌木重复（用户 2026-10-29 首次报告）\n\n**状态：recorded / 未处理**"
new = """## OPEN-001 两种枯死灌木重复（用户 2026-10-29 首次报告）

**状态：partially-fixed-static（P2-3，2026-10-29）/ 未实机；有世界生成风险**

- 新增 `neoforge:remove_features` biome modifier；
- 目标 `#minecraft:is_overworld` + 125 个 TFC biome；
- 移除 `tfc:plant/dead_bush` / `tfc:plant/dead_bush_patch`；
- A `dead_cane` 仍存在（没有 placed feature，无法用同一机制过滤）；
- 因此是“移除 TFC 枯死灌木、保留 A 枯死藤蔓”；若方向反了需回退；
- 未实机验证 schema/注入；
- 证据：docs/532、533。"""
if old not in t:
    raise SystemExit("anchor missing")
t = t.replace(old, new, 1)
p.write_text(t, encoding="utf-8")
print("OPEN-001 updated")
