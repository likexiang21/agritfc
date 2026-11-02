from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
old = "**状态：reverted-by-user-direction（2026-10-29）/ 未实机**\n\n- 新增 `neoforge:remove_features` biome modifier；"
new = "**状态：reverted-by-user-direction（2026-10-29）/ 未实机**\n\n- **本方案的 B 过滤已按用户指令撤销**；以下为历史记录。\n- 曾新增 `neoforge:remove_features` biome modifier；"
if old not in t:
    raise SystemExit("anchor missing")
t = t.replace(old, new, 1)
p.write_text(t, encoding="utf-8")
print("OPEN-001 history marked")
