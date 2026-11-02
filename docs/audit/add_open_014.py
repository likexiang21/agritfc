from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-014 木工朝向属性初始化导致启动崩溃（2026-10-30 日志）

**状态：fixed-static / 待实机**

- 日志：`crash-2026-10-30_09.33.00-fml.txt`、`logs/latest.log`；
- 首个异常：`TimberPieceBlock.<init>` line 22 在状态定义中设置不存在的 `facing`；
- 根因：`createBlockStateDefinition` 在 `super()` 期间调用，子类 `directional` 字段尚未初始化；
- 修复：拆分为 `TimberPieceBlock`（无 facing）与 `DirectionalTimberPieceBlock`（有 facing），`TimberBlocks` 按 part 选择；
- 日志中的 `unbound value`（debarked_half/serving_plate）是首个注册异常导致的次级错误，需启动确认消失；
- 未实机（无 Java 21/PCL 环境）；
- 证据：docs/616、617。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-014 appended")
