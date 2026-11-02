from pathlib import Path

# --- 291 generator corrections ---
p = Path("mod_rebuild/docs/audit/generate_291_v2.py")
t = p.read_text(encoding="utf-8")
t = t.replace("- [10. TFC 11 灌木](#10-tfc-11-灌木)", "- [10. TFC 10 灌木](#10-tfc-10-灌木)")
t = t.replace("| TFC 灌木 | 11 | 草莓单列为普通作物 |",
              "| TFC 灌木 | 10 | 草莓已经是 A 普通作物（A 也移除了 TFC 草莓灌木的世界生成），不再作为 B 的灌木重做目标 |")
t = t.replace("- TFC 11 灌木仍在 TFC 灌木管线；",
              "- TFC 10 灌木仍在 TFC 灌木管线；草莓已经是 A 普通作物，TFC 草莓灌木被 A 关闭世界生成/隐藏；")
t = t.replace("3. **范围未统一**：A 87、TFC 29、TFC 11 灌木、B 17 新增，四套范围的生产/培育链覆盖口径必须先定。",
              "3. **范围未统一**：A 87、TFC 29、TFC 10 灌木、B 43 新增，四套范围的生产/培育链覆盖口径必须先定。")
t = t.replace('lines.append("\\n## 10. TFC 11 灌木\\n")',
              'lines.append("\\n## 10. TFC 10 灌木\\n")')
old_bush = '''    ("strawberry", "浆果/普通作物", "匍匐茎为主，种子为辅", "果酱、果干、冰淇淋", "母株→匍匐茎苗→育苗→移栽"),
]'''
new_bush = ''']'''
if old_bush not in t:
    raise SystemExit("bush strawberry row missing")
t = t.replace(old_bush, new_bush)
t = t.replace("草莓从灌木摘出，按普通作物处理；11 种灌木不得改 A 已有标签；覆盖 TFC 标签只能追加；蜂蜜 `buzzing_leaves` 兼容不能破坏。",
              "草莓已经由 A 迁移为普通作物，不在 B 的 10 种 TFC 灌木重做范围内；TFC 草莓灌木的世界生成已由 A 的标签 remove 关闭。10 种灌木不得改 A 已有标签；覆盖 TFC 标签只能追加；蜂蜜 `buzzing_leaves` 兼容不能破坏。")
t = t.replace("| TFC | 29 作物 + 11 灌木资源覆盖 | 先解决 A cabbage 所有权/EUPL |",
              "| TFC | 29 作物 + 10 灌木资源覆盖 | 先解决 A cabbage 所有权/EUPL |")
t = t.replace("| P4 | TFC 29+11 灌木资源层接入 | 不改 TFC raw；存档安全 |",
              "| P4 | TFC 29+10 灌木资源层接入 | 不改 TFC raw；存档安全 |")
t = t.replace("2. A 87、TFC 29、TFC 11 灌木、B 17 新增各自是否共用同一套六环节。",
              "2. A 87、TFC 29、TFC 10 灌木、B 43 新增各自是否共用同一套六环节。")
t = t.replace("- `287-crop-redo-requirements-20261028.md`：原始要求、29 作物/11 灌木、当前缺口。",
              "- `287-crop-redo-requirements-20261028.md`：原始要求、29 作物/10 灌木、当前缺口；草莓已由 A 迁移为普通作物。")
p.write_text(t, encoding="utf-8")
print("291 generator corrected")

# --- 287 corrections ---
p = Path("mod_rebuild/docs/287-crop-redo-requirements-20261028.md")
t = p.read_text(encoding="utf-8")
t = t.replace("B 覆盖的是 TFC 的 29 种作物和 11 种灌木。",
              "B 覆盖的是 TFC 的 29 种作物和 10 种灌木；草莓已经由 A 迁移为普通作物。")
t = t.replace("### 2.2 TFC 11 种浆果灌木",
              "### 2.2 TFC 10 种浆果灌木（草莓已移出）")
old_bush_list = """实测 13 个 `*_bush` blockstate，减去 2 个枯死态 `dead_berry_bush` / `dead_bush`，剩 **11 种**：

```text
blackberry · blueberry · bunchberry · cloudberry · cranberry ·
elderberry · gooseberry · raspberry · snowberry · strawberry ·
wintergreen
```
"""
new_bush_list = """实测 TFC 有 13 个 `*_bush` blockstate，减去 2 个枯死态 `dead_berry_bush` / `dead_bush`，原本为 11 种。

但 **A 已经把草莓迁移为普通作物**：
- A 的 `crops-manifest.json` 中有 `strawberry`（普通作物）；
- A 有 `crop/strawberry`、`wild_crop/strawberry`、`dead_crop/strawberry`、种子与掉落表；
- A 的 `data/tfc/tags/worldgen/placed_feature/feature/berry_bushes.json` 已 `remove` 了 `tfc:plant/strawberry_bush_patch`，即 TFC 草莓灌木不再自然生成；
- 因此 B 的 TFC 灌木重做目标应为 **10 种，不含草莓**。

```text
blackberry · blueberry · bunchberry · cloudberry · cranberry ·
elderberry · gooseberry · raspberry · snowberry · wintergreen
```
"""
if old_bush_list not in t:
    raise SystemExit("287 bush list missing")
t = t.replace(old_bush_list, new_bush_list)
t = t.replace("⚠️ **草莓在 11 种列表中**，但必须单独处理，见 §4。",
              "⚠️ **草莓不在 B 的 10 种重做范围内**：它是 A 的普通作物；TFC 草莓灌木只被 A 关闭世界生成/隐藏，B 不重复迁移。")
t = t.replace("### 4.1 11 种灌木", "### 4.1 10 种灌木（草莓已迁移）")
t = t.replace("- 11 种灌木外观同族", "- 10 种灌木外观同族")
t = t.replace("### 4.2 草莓：唯一例外", "### 4.2 草莓：已由 A 迁移，不再是 B 的例外任务")
old_strawberry = """- 草莓必须从 TFC 灌木形态中**单独摘出**，做成**普通作物**，不是矮灌木；
- 目标是用耕地作物管线，6 个龄阶段；
- 现状：TFC `tfc:plant/strawberry_bush` 是 `StationaryBerryBushBlock` 3 stage，46 条资源；
- A 的标签曾指向 TFC 草莓，B 必须**绕过而不是改 A**：B 自己覆盖 TFC 的标签，不修改 A 的资源/代码；
- 验收：草莓在野外/农田都表现为普通作物；能进入果酱/干燥/冰淇淋链。"""
new_strawberry = """- **草莓已经由 A 迁移为普通作物**：A 的 manifest、`crop/strawberry`、野生/枯死作物、种子和掉落表均已存在；
- A 的 TFC 世界生成标签已 `remove` `tfc:plant/strawberry_bush_patch`，TFC 草莓灌木不再自然生成；
- 因此 B **不重复创建草莓普通作物**，也不把 TFC 草莓灌木列为 B 的 11/10 种重做目标；
- 验收改为：确认 A 的草莓普通作物仍可种植/生长/收获，B 的 10 种灌木重做不误伤它。"""
if old_strawberry not in t:
    raise SystemExit("287 strawberry block missing")
t = t.replace(old_strawberry, new_strawberry)
t = t.replace("| TFC 11 灌木 | 0 |", "| TFC 10 灌木（不含草莓） | 0 |")
t = t.replace("4. **草莓命名空间**：B 新建 `tfcagricultureplus:crop/strawberry`，还是只覆盖 TFC 资源？不能让 B 写 A 的 `tfcfarmingplus` 资源。",
              "4. **草莓已定案**：A 已是普通作物，B 不再新建/迁移草莓；后续只需确保 B 的灌木重做不误伤 A 草莓。")
t = t.replace("`117 §5.2` 写的目标是 `tfcfarmingplus:crop/strawberry`（A 命名空间），但 B 的红线是不写 `assets/tfcfarmingplus/**` / A 资源。B 实际应使用 B 命名空间（如 `tfcagricultureplus:crop/strawberry`）还是仅仅覆盖 TFC 资源，需要用户确认。",
              "`117 §5.2` 写的 `tfcfarmingplus:crop/strawberry` 已经由 A 落地；B 不应重复实现，也不应把 TFC 灌木形态当作 B 的目标。")
p.write_text(t, encoding="utf-8")
print("287 corrected")

# --- 288 correction ---
p = Path("mod_rebuild/docs/288-crop-production-and-cultivation-chain-20261028.md")
t = p.read_text(encoding="utf-8")
t = t.replace("- **A1/A2 的 29+11**：TFC 作物/灌木的**视觉与资源覆盖**；",
              "- **A1/A2 的 29+10**：TFC 作物/灌木的**视觉与资源覆盖**；草莓已由 A 迁移为普通作物，不在 TFC 灌木重做内；")
p.write_text(t, encoding="utf-8")
print("288 corrected")
