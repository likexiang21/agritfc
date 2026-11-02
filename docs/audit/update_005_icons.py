from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t = t.replace("**状态：fixed-static（P0-4，2026-10-29）/ 未实机；贴图未处理**",
              "**状态：fixed-static（P0-4 names + icons，2026-10-29）/ 未实机**")
t = t.replace("- 未改贴图：`crop_waste` 仍共用 `tfc:item/straw`，属于视觉问题。",
              "- 2026-10-29 扩展：82 个 crop_waste 图标映射到已有 A/TFC 作物贴图，不再全部共用 `tfc:item/straw`（docs/563、564）。")
t = t.replace("- 证据：docs/518、519。", "- 证据：docs/518、519、563、564。")
p.write_text(t, encoding="utf-8")
print("OPEN-005 status updated")
