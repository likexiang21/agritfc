from pathlib import Path

p = Path("mod_rebuild/docs/291-crop-system-complete-modification-20261028.md")
t = p.read_text(encoding="utf-8")

# Literal \n in nut section.
t = t.replace("### 9.4 已有乔木坚果：新叶状态与季节挂果\\n", "### 9.4 已有乔木坚果：新叶状态与季节挂果\n")
t = t.replace("已有乔木的坚果不另造一棵树，而是在**原树叶方块上增加新的叶子状态**，按 TFC 季节挂果并随机掉落。\\n", "已有乔木的坚果不另造一棵树，而是在**原树叶方块上增加新的叶子状态**，按 TFC 季节挂果并随机掉落。\n")

# TFC 29 flow replacement details before TFC matrix.
needle = "## 8. TFC 29 作物矩阵\n"
details = """## 8. TFC 29 作物矩阵

**TFC 29 不是资源旁路**：B 要替换/覆盖 TFC 的原种植与收获流程：
- 覆盖 TFC 29 的作物 blockstate/model/loot table，不再保留原 6–10 直掉；
- 种植：种子处理（DataComponent）、B 的育苗/移栽/农艺流程接入 TFC 作物；
- 收获：A/TFC 谷物全部走 `grain_bundle → 脱粒 → 谷粒 + wet_grass`；非谷物按 B 的 profile 出主/副产品；
- TFC 方块行为通过 B 的 block/mixin 接管；旧存档的 TFC 作物状态给默认迁移值；
- 矩阵中的“TFC 原值”只是回退基线，不是最终目标。
"""
if needle not in t:
    raise SystemExit("TFC matrix heading missing")
t = t.replace(needle, details, 1)

# 4.1.3 intro A 10 -> A+TFC 16.
t = t.replace("不是所有谷物都直接掉散粒：**A 的 10 种长秆谷物先收谷物捆，再脱粒**，脱粒副产才是湿草。",
              "不是所有谷物都直接掉散粒：**A 10 + TFC 6 长秆谷物先收谷物捆，再脱粒**，脱粒副产才是湿草。")

# Mushroom table natural-only rows.
t = t.replace("| 11 | `porcini` | 牛肝菌（食用） | 菌包+树根/腐木 | 接种→走菌→出菇→采 | 鲜食/干燥/调味 | 1–2/潮；2–3 潮 |",
              "| 11 | `porcini` | 牛肝菌（食用） | **无（仅野生）** | 自然生成/随机刷新→采 | 鲜食/干燥/调味 | 1–2/季 |")
t = t.replace("| 12 | `morel` | 羊肚菌（食用） | 菌包/林下菌床 | 接种→走菌→出菇→采 | 鲜食/干燥/调味 | 1–2/潮；2–3 潮 |",
              "| 12 | `morel` | 羊肚菌（食用） | **无（仅野生）** | 自然生成/随机刷新→采 | 鲜食/干燥/调味 | 1–2/季 |")
t = t.replace("| 13 | `chanterelle` | 鸡油菌（食用） | 菌根菌床/树根 | 接种树根→出菇→采 | 鲜食/干燥/调味 | 1–2/潮；2–3 潮 |",
              "| 13 | `chanterelle` | 鸡油菌（食用） | **无（仅野生）** | 自然生成/随机刷新→采 | 鲜食/干燥/调味 | 1–2/季 |")
t = t.replace("| 14 | `black_truffle` | 黑松露（食用/药用） | 树根接种 | 接种树根→多年培养→采 | 鲜食/研磨/油浸 | 1–2/季；极低产 |",
              "| 14 | `black_truffle` | 黑松露（食用/药用） | **无（仅野生）** | 自然生成/随机刷新→采 | 鲜食/研磨/油浸 | 1–2/季；极低产 |")

# Step 5 A only.
t = t.replace("A 谷物按 4.1.3 先出谷物捆，脱粒产 `wet_grass`。",
              "A 10 + TFC 6 谷物按 4.1.3 先出谷物捆，脱粒产 `wet_grass`。")

# Scope TFC row.
t = t.replace("| TFC | 29 作物 + 10 灌木资源覆盖 | 先解决 A cabbage 所有权/EUPL |",
              "| TFC | **29 作物替换/覆盖种植+收获+掉落** + 10 灌木资源覆盖 | 先解决 A cabbage 所有权/EUPL；旧存档迁移/回退 |")

# 9.5 total wording.
t = t.replace("- 香料是 Firmalife 搁置项接管/重建 + 新增；坚果是 B 新物品/树产；蘑菇是 B 新菌包/菌根栽培物；",
              "- 香料是 Firmalife 搁置项接管/重建 + 新增；坚果是 B 新物品/树产 + 已有树叶状态；蘑菇含野生生成/刷新与可栽培 11/自然专用 4；")

# Nut implementation: mention leaf block state extension, not separate tree.
t = t.replace("- TFC/A/AFC 已有树叶方块通过 B 的 block/mixin 扩展实现，**不另建重复树**；存档旧叶状态给默认值；",
              "- TFC/A/AFC 已有树叶方块通过 B 的 block/mixin **新增叶状态并覆盖全部 blockstate/model 组合**，**不另建重复树**；旧存档缺省 `nut_state=0`；")

p.write_text(t, encoding="utf-8")
print("291 corrected: TFC override, wet grass ID, mushroom natural, nut leaf state")
