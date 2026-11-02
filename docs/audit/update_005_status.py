from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
old = "## OPEN-005 农业内容名称差、不可读且有未翻译片段（用户 2026-10-29 第四个问题）\n\n**状态：recorded / 未处理**"
new = """## OPEN-005 农业内容名称差、不可读且有未翻译片段（用户 2026-10-29 第四个问题）

**状态：fixed-static（P0-4，2026-10-29）/ 未实机；贴图未处理**

- 246 个农业名称键/语言改为逐物种人工名称；
- 510 个木材/家具/木工名称键/语言改为“木材名+中文家具名”；
- 中英双语同步；
- 中文 item/block 名称中的 ASCII 原始 ID 为 0；
- 未改贴图：`crop_waste` 仍共用 `tfc:item/straw`，属于视觉问题。
- 证据：docs/518、519。"""
if old not in t:
    raise SystemExit("anchor missing")
t = t.replace(old, new, 1)
p.write_text(t, encoding="utf-8")
print("OPEN-005 updated")
