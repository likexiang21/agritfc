from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t = t.replace(
    "- 已新增金属罐/陶盘/繁殖材料信息页；仍未新增 B 独立 recipe category；烹饪锅仍是动态组合；",
    "- 已新增金属罐/陶盘/繁殖材料信息页；已为 IN_WORLD 分类添加 axe/saw 催化剂；仍未新增 B 独立 recipe category；烹饪锅仍是动态组合；"
)
t = t.replace("- 证据：docs/526、527。", "- 证据：docs/526、527、552、553、579、580。")
p.write_text(t, encoding="utf-8")
print("OPEN-012 catalysts updated")
