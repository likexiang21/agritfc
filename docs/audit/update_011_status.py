from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
old = "## OPEN-011 木工内容移植不尊重原有内容和配方（用户 2026-10-29 第十个问题）\n\n**状态：recorded / 未处理**"
new = """## OPEN-011 木工内容移植不尊重原有内容和配方（用户 2026-10-29 第十个问题）

**状态：partially-fixed-static（P2-2，2026-10-29）/ 未实机**

- 对照 TFC Woodworking 1.2.4 的 40 条 wood/stripped_wood 配方；
- B 的 40 条复制配方 type/pattern/result/key 结构一致（problems 0）；
- 发现 `lumber_pile` 没有方块物品，却错误补了自掉落表；已删除并修正 P0-3 的 174→173；
- AFC 14 木材 28 条为 B 扩展，不是原配方；
- 未逐项对照模型/碰撞/交互/音效，未实机；
- 证据：docs/530、531。"""
if old not in t:
    raise SystemExit("anchor missing")
t = t.replace(old, new, 1)
p.write_text(t, encoding="utf-8")
print("OPEN-011 updated")
