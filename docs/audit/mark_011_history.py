from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
old = "- 模型对照：TFCW 20 木材 ×3 类型 ×3 资源，blockstate variants 20/20 不同、model parent/texture/item parent 各 60/60 不同；用户对模型层“不尊重原内容”的批评成立，对齐需要视觉/几何重做（docs/544、545）。"
new = "- 历史模型对照：对齐前 blockstate variants 20/20 不同、model parent/texture/item parent 各 60/60 不同（docs/544、545）；该差异已由 561/562 修复。"
if old not in t:
    raise SystemExit("anchor missing")
t = t.replace(old, new, 1)
p.write_text(t, encoding="utf-8")
print("OPEN-011 history marked")
