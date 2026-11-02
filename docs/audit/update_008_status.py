from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
old = "## OPEN-008 帕秋莉手册不可读（用户 2026-10-29 第七个问题）\n\n**状态：recorded / 未处理**"
new = """## OPEN-008 帕秋莉手册不可读（用户 2026-10-29 第七个问题）

**状态：partially-fixed-static（P1-3，2026-10-29）/ 未实机**

- 新增作物分类 × 中英；
- 新增 7 个主题 × 中英 = 14 个 entry：
  - 收获/废水
  - 种子与育苗
  - 谷物捆与湿草
  - 香料
  - 坚果与叶状态
  - 蘑菇与菌包
  - TFC 灌木
- 每页单主题、短段落/列表，不暴露原始 ID；
- 未实机检查分页/排版；
- 没有 recipe pages/图片；旧三主题未重写；
- 证据：docs/524、525。"""
if old not in t:
    raise SystemExit("anchor missing")
t = t.replace(old, new, 1)
p.write_text(t, encoding="utf-8")
print("OPEN-008 updated")
