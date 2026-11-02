from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
old = "## OPEN-006 陶盘 knapping 配方与 TFC 陶碗完全相同（用户 2026-10-29 第五个问题，已按用户澄清修正）\n\n**状态：recorded / 未处理**"
new = """## OPEN-006 陶盘 knapping 配方与 TFC 陶碗完全相同（用户 2026-10-29 第五个问题，已按用户澄清修正）

**状态：fixed-static（P0-1，2026-10-29）/ 未实机**

- 新 pattern：`[" ### ","#####"," ### ","     ","     "]`
- 碰撞扫描：B/TFC/A 无 `tfc:clay` 重复。
- 证据：docs/512、513。"""
if old not in t:
    raise SystemExit("anchor missing")
t = t.replace(old, new, 1)
p.write_text(t, encoding="utf-8")
print("OPEN-006 status updated")
