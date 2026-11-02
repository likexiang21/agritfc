from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
old = "## OPEN-004 全部工作方块没有合成表，家具只有低质量占位配方（用户 2026-10-29 第三个问题）\n\n**状态：partially-fixed-static（P0-3，2026-10-29）/ 未实机**"
new = """## OPEN-004 全部工作方块没有合成表，家具只有低质量占位配方（用户 2026-10-29 第三个问题）

**状态：fixed-static-recipes（P0-3 + P2-4，2026-10-29）/ 未实机**

- 工作方块已补 174 条配方 + 173 个有效 loot table（`lumber_pile` 无物品，已删除错误自掉落）；
- 204 条家具占位配方已重做为 6 种不同图案，使用 TFC/AFC lumber、rod、wrought iron sheet、glass；
- 本地 shaped 冲突 groups=347/347，旧的 food_display/sink_cabinet 冲突消失；
- 家具掉落表仍缺；家具功能仍 P1-2 部分分化；
- 未实机。
- 证据：docs/516、517、534、535。"""
if old not in t:
    raise SystemExit("anchor missing")
t = t.replace(old, new, 1)
p.write_text(t, encoding="utf-8")
print("OPEN-004 updated")
