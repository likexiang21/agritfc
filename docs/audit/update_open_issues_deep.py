from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
text = p.read_text(encoding="utf-8")

text = text.replace(
    "## OPEN-006 陶盘/碗配方冲突且未参考陶罐流程（用户 2026-10-29 第五个问题）",
    "## OPEN-006 陶盘 knapping 配方与 TFC 陶碗完全相同（用户 2026-10-29 第五个问题，已按用户澄清修正）",
)

marker = "## OPEN-007 农业育种/培育流程未按技术文档"
insert = r'''- **直接冲突已确认**：

  B 的 `knapping/ceramic/unfired_plate.json`：

  ```json
  {
    "type": "tfc:knapping",
    "knapping_type": "tfc:clay",
    "pattern": ["#   #", " ### ", "     ", "#   #", " ### "],
    "result": { "count": 1, "id": "tfcagricultureplus:ceramic/unfired_plate" }
  }
  ```

  TFC 的 `data/tfc/recipe/knapping/ceramic/unfired_bowl.json`：

  ```json
  {
    "type": "tfc:knapping",
    "knapping_type": "tfc:clay",
    "pattern": ["#   #", " ### ", "     ", "#   #", " ### "],
    "result": { "count": 4, "id": "tfc:ceramic/unfired_bowl" }
  }
  ```

  两者 **knapping_type + pattern 完全相同**，只是输出不同；这是确定的配方冲突，不是“风格不一致”。

- 已经用静态扫描脚本确认：
  - `mod_rebuild/docs/audit/prototype/find_knapping_collisions.py`

## OPEN-013 7 个研钵 knapping 配方共用同一 `tfc:rock` pattern

**状态：recorded / 未处理**

### 证据

`find_knapping_collisions.py` 还发现 B 的 7 个 pestle：

```text
basalt_pestle
diorite_pestle
gabbro_pestle
granite_pestle
obsidian_pestle
quartzite_pestle
slate_pestle
```

全部使用：

```text
knapping_type = tfc:rock
pattern       = ["  #  ", "  #  ", "  #  ", " ### ", "  #  "]
```

每个结果不同，但 pattern 完全相同。

### 风险

- TFC 自身的 rock 配方也有一组 pattern 重复（例如不同岩石类别的刀头/标枪头），说明 TFC 可能按输入材料或其他规则消歧；
- 但 B 的 7 个 pestle 是否真的能按岩石区分，尚未验证；
- 当前至少是**配方选择语义不明**，属于必须通过 TFC `tfc:knapping` 规则确认的高风险项。

'''
text = text.replace(marker, insert + marker, 1)

text = text.replace(
    "## 动态日志更新（2026-10-29 18:48 后）\n\n- 新 jar 已在 mods 并成功加载；\n- 世界加载完成；\n- 日志停在 `Saving and pausing game...`；\n- 当前 open issues 均来自用户实机截图/静态审查，尚未修改代码。",
    "## 动态日志更新（2026-10-29 18:49 后）\n\n- 新 jar 已在 mods 并成功加载；\n- 世界加载完成；\n- 18:49:12 玩家退出；18:49:13 客户端正常 `Stopping!`；\n- 没有 B 相关 fatal error；\n- 当前 open issues 均来自用户实机截图/静态审查，尚未修改代码。",
)
p.write_text(text, encoding="utf-8")
print("updated OPEN-006/013 and log status")
