from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-015 二次崩溃：本模组 oven 配方触发 Firmalife JEI 绘制（2026-10-30）

**状态：fixed-static / 待实机**

- 日志：`crash-2026-10-30_22.13.48-client.txt`、`logs/latest.log`；
- 崩溃：`NoClassDefFoundError: net/dries007/tfc/config/TemperatureDisplayStyle` at Firmalife `OvenCategory.draw`；
- 本模组 15 条 `firmalife:oven` 配方把 B 的 raw 面团放进该 JEI 分类，触发绘制路径；
- 修复：15 条全部迁移为 `tfc:heating`（400°C，result_item 保持），删除 `recipe/oven/`；
- 校验：B 数据中 `firmalife:oven` 引用 0，heating 16 条，build 成功；
- 未实机；
- 证据：docs/618、619。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-015 appended")
