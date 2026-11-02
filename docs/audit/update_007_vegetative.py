from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
old = "**状态：partially-fixed-static（P2-1，2026-10-29）/ 未实机**"
new = "**状态：partially-fixed-static（P2-1 + vegetative items，2026-10-29）/ 未实机**"
# replace only the OPEN-007 occurrence
idx = t.find("## OPEN-007")
j = t.find(old, idx)
if j < 0:
    raise SystemExit("OPEN-007 anchor missing")
t = t[:j] + new + t[j + len(old):]
marker = "- 证据：docs/528、529。"
add = "\n- 2026-10-29 扩展：新增 21 个 `propagation_stock/<species>`，覆盖 CORM/TUBER/RHIZOME/CROWN/DIVISION/RUNNER；产品 1→2 合成，耕地放置；水生作物/母株性状仍缺（docs/542、543）。"
if marker in t and "propagation_stock" not in t:
    t = t.replace(marker, marker + add, 1)
p.write_text(t, encoding="utf-8")
print("OPEN-007 updated")
