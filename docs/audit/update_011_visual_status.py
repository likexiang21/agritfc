from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
old = "**状态：partially-fixed-static（P2-2 + model parity，2026-10-29）/ 未实机；需视觉重做**"
new = "**状态：fixed-static-tfc-parity（2026-10-29）/ AFC 扩展未对齐 / 未实机**"
idx = t.find("## OPEN-011")
j = t.find(old, idx)
if j < 0:
    raise SystemExit("OPEN-011 anchor missing")
t = t[:j] + new + t[j + len(old):]
marker = "- 模型对照：TFCW 20 木材 ×3 类型 ×3 资源，blockstate variants 20/20 不同、model parent/texture/item parent 各 60/60 不同；用户对模型层“不尊重原内容”的批评成立，对齐需要视觉/几何重做（docs/544、545）。"
add = "\n- 2026-10-29 视觉对齐：TFC 20 木材复用 TFCW 原模型/blockstate/item model/图标；blockstate 差异 0、item parent 差异 0，model parent/inner 仅命名空间替换；AFC 14 木材为风格扩展，缺 item 图标（docs/561、562）。"
if marker in t and "视觉对齐：TFC 20" not in t:
    t = t.replace(marker, marker + add, 1)
p.write_text(t, encoding="utf-8")
print("OPEN-011 updated")
