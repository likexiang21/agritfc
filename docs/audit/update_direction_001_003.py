from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")

old1 = "**状态：partially-fixed-static（P2-3，2026-10-29）/ 未实机；有世界生成风险**"
new1 = "**状态：reverted-by-user-direction（2026-10-29）/ 未实机**"
idx = t.find("## OPEN-001")
j = t.find(old1, idx)
if j < 0:
    raise SystemExit("OPEN-001 anchor missing")
t = t[:j] + new1 + t[j + len(old1):]
marker = "- 证据：docs/532、533。"
add = "\n- 用户 2026-10-29 指令：“枯死灌木读取 TFC 原版处理方式”；已删除 `remove_duplicate_dead_bush.json`，恢复 TFC 原版 worldgen；B 不再过滤（docs/555、556）。"
if marker in t and "读取 TFC 原版处理方式" not in t:
    t = t.replace(marker, marker + add, 1)

old3 = "**状态：partially-fixed-static（P1-2 + sink tank，2026-10-29）/ 未实机**"
new3 = "**状态：partially-fixed-static（P1-2 + sink；用户限定水槽仅取水，2026-10-29）/ 未实机**"
idx = t.find("## OPEN-003")
j = t.find(old3, idx)
if j < 0:
    raise SystemExit("OPEN-003 anchor missing")
t = t[:j] + new3 + t[j + len(old3):]
p.write_text(t, encoding="utf-8")
print("OPEN-001/003 direction updated")
