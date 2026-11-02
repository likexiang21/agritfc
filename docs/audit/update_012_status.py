from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
old = "## OPEN-012 JEI 可读性差且未表现新增加工（用户 2026-10-29 第十一个问题）\n\n**状态：recorded / 未处理**"
new = """## OPEN-012 JEI 可读性差且未表现新增加工（用户 2026-10-29 第十一个问题）

**状态：partially-fixed-static（P1-4，2026-10-29）/ 未实机**

- 34 个 B 晾架加入 Firmalife drying JEI catalyst；
- 10 个设备信息页（中英双语）：
  cooking_pan / nursery_tray / mushroom_bag / silkworm_rack / drying_rack /
  cutting_board / log_cutting_board / knife_block / mortar / kitchen_storage；
- 新增 20 个 JEI 信息语言键；
- 仍未新增 B 独立 recipe category；烹饪锅仍是动态组合；
- 未实机确认显示；
- 证据：docs/526、527。"""
if old not in t:
    raise SystemExit("anchor missing")
t = t.replace(old, new, 1)
p.write_text(t, encoding="utf-8")
print("OPEN-012 updated")
