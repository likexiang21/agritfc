from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
old = "## OPEN-003 厨房家具全是同一套皮容器，无功能差异（用户 2026-10-29 第二个问题）\n\n**状态：recorded / 未处理**"
new = """## OPEN-003 厨房家具全是同一套皮容器，无功能差异（用户 2026-10-29 第二个问题）

**状态：partially-fixed-static（P1-2，2026-10-29）/ 未实机**

- 6 种家具按 `StorageKind` 实施不同过滤/堆叠上限：
  - counter 任意/64；
  - half 任意/16；
  - sink 仅流体容器/1；
  - spice_rack 仅 `#tfcagricultureplus:spices`/64；
  - food_display 仅食物/64；
  - fruit_bowl 仅食物/1；
- 6 种独立显示名；
- 仍共用 9 格菜单/屏幕；未实现水箱、保鲜、可视化；
- 未实机。
- 证据：docs/522、523。"""
if old not in t:
    raise SystemExit("anchor missing")
t = t.replace(old, new, 1)
p.write_text(t, encoding="utf-8")
print("OPEN-003 updated")
