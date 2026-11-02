from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
old3 = "**状态：partially-fixed-static（P1-2，2026-10-29）/ 未实机**"
# only replace the first occurrence in OPEN-003 section
idx = t.find("## OPEN-003")
j = t.find("**状态：partially-fixed-static（P1-2，2026-10-29）/ 未实机**", idx)
if j < 0:
    raise SystemExit("OPEN-003 status anchor missing")
t = t[:j] + "**状态：partially-fixed-static（P1-2 + sink tank，2026-10-29）/ 未实机**" + t[j + len("**状态：partially-fixed-static（P1-2，2026-10-29）/ 未实机**"):]

old4 = "- 家具掉落表仍缺；家具功能仍 P1-2 部分分化；"
new4 = "- 204 个家具 loot table 已复核存在（每个掉落自身）；家具功能仍 P1-2 部分分化；"
if old4 in t:
    t = t.replace(old4, new4, 1)
# add sink tank evidence after OPEN-003 evidence line
marker = "- 证据：docs/522、523。"
add = "\n- 2026-10-29 扩展：sink_cabinet 增加 4000 mB 水罐 + block capability（docs/540、541）。"
if marker in t and "4000 mB 水罐" not in t:
    t = t.replace(marker, marker + add, 1)
p.write_text(t, encoding="utf-8")
print("OPEN-003/004 updated")
