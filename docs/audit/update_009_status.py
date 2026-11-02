from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
old = "## OPEN-009 重复木碗与陶碗（用户 2026-10-29 第八个问题）\n\n**状态：recorded / 未处理**"
new = """## OPEN-009 重复木碗与陶碗（用户 2026-10-29 第八个问题）

**状态：fixed-static（P0-2，2026-10-29）/ 未实机**

- 已删除 B 的 `bowl/wood`、`bowl/ceramic` 物品、2 个配方、item model、语言键、创造页入口；
- 移除 `DishEating.transferToBowl` 和 `ServingPlateBlock` 的碗交互；
- 盘装菜仍可直接食用，但不再分装到 B 碗；这是明确的功能缩减。
- 证据：docs/514、515。"""
if old not in t:
    raise SystemExit("anchor missing")
t = t.replace(old, new, 1)
p.write_text(t, encoding="utf-8")
print("OPEN-009 updated")
