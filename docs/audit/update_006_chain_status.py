from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
old = "**状态：fixed-static（P0-1，2026-10-29）/ 未实机**"
new = "**状态：fixed-static（P0-1 + OPEN-006 review，2026-10-29）/ 未实机**"
if old not in t:
    raise SystemExit("status anchor missing")
t = t.replace(old, new, 1)
marker = "- 证据：docs/512、513。"
add = "\n- 链路复核：未烧盘→陶盘；白盘→烧制→15 色染料盘；旧碗转换配方已删除；\n  `check_ceramic_plate_chain.py` problems 0（docs/538、539）。"
if marker in t and "check_ceramic_plate_chain.py" not in t:
    t = t.replace(marker, marker + add, 1)
p.write_text(t, encoding="utf-8")
print("OPEN-006 updated")
