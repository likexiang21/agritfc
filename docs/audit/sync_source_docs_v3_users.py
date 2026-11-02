from pathlib import Path

# --- 287 ---
p = Path("mod_rebuild/docs/287-crop-redo-requirements-20261028.md")
t = p.read_text(encoding="utf-8")
t = t.replace("`126` §10.2 A1 的核心口径是 **资源覆盖**：",
              "**2026-10-28 用户新口径：不是资源旁路，TFC 29 要替换/覆盖种植与收获流程。** 资源覆盖只是其中一部分：")
t = t.replace("- **TFC 的方块类和 blockstate 属性不变**（仍是 `age` / `fruiting` / `part` / `stick` 等）；\n- 只换皮 ⇒ **存档安全**；",
              "- TFC 作物的方块类/blockstate 可以被 B 扩展或接管（如新增 `nut_state` 叶状态）；\n- 必须做旧存档迁移与回退，不能再假设“只换皮”。")
t = t.replace("- 验收要求：**原有掉落不能减少**，只能增加次产品；",
              "- 验收要求：**TFC 原种植/收获/掉落被 B 覆盖**；旧 raw 只作回退基线，必须提供迁移；")
t = t.replace("- 副产物：**wet_grass 潮湿草**（野草收割/未成熟补偿，晒干→	fc:straw）与 **green_waste 废枝叶**（→	fc:compost_greens/*）必须有明确掉落/标签/出口，不得忽略。",
              "- 副产物：**`tfcagricultureplus:wet_grass`**（B 新物品；谷物捆脱粒/野草/未成熟补偿；晒干→`tfc:straw`）；废枝叶只在真实产出时逐作物 `crop_waste/<crop>`（→`tfc:compost_greens/*`），不设通用 `green_waste`。")
t = t.replace("1. 29 种在游戏里都长成 B 的风格；\n2. 原有掉落不减少（只是增加次产品）；\n3. 存档里已种的 TFC 作物不消失。",
              "1. 29 种在游戏里都长成 B 的风格；\n2. 29 种的种植/收获/掉落由 B 覆盖，旧流程可回退；\n3. 存档里已种的 TFC 作物不消失，旧状态有迁移默认值。")
t = t.replace("⚠️ 这里存在文档口径差异：`126` A1 把 A1 定义为**只做资源覆盖、方块类不变**，而 `280` 的规划摘要写成“方块/行为、野生生成、标签、手册”全都要做。**后续必须明确哪一份是验收基线**，不能同时按两种口径施工。",
              "**已定案（2026-10-28）：按 `280` 的完整行为口径**；`126 A1` 的“仅资源覆盖、方块类不变”作废。TFC 29 要替换种植/收获/掉落，不是资源旁路。")
t = t.replace("4. 不减少 TFC 原有掉落；\n5. 存档安全：TFC 方块类/状态属性不变；",
              "4. TFC 原掉落可被覆盖，但必须提供旧值回退；\n5. 方块状态可扩展，必须做存档迁移；")
t = t.replace("1. **验收基线**：按 `126` A1 的“资源覆盖、方块类不变”，还是按 `280` 的“含野生生成/方块行为/标签/手册”系统级重做？",
              "1. **验收基线已定**：按 `280` 的完整行为重做；TFC 29 种植/收获/掉落由 B 覆盖。")
t = t.replace("8. **“野外生成/标签”是否属于 B 覆盖范围**：会触碰 TFC worldgen 和标签，影响存档/兼容，必须单独确认。",
              "8. **“野外生成/标签”已纳入 B 覆盖范围**：包含 TFC 作物 worldgen、标签、作物行为，需要迁移方案。")
# Strawberry old unresolved remains
t = t.replace("🛑 **未决冲突**：`117` §5.2 写的目标是 `tfcfarmingplus:crop/strawberry`（A 命名空间），但 B 的红线是不写 `assets/tfcfarmingplus/**` / A 资源。B 实际应使用 B 命名空间（如 `tfcagricultureplus:crop/strawberry`）还是仅仅覆盖 TFC 资源，需要用户确认。",
              "**已定案**：草莓由 A 迁移为普通作物；B 不再新建/迁移草莓，也不把 TFC 草莓灌木列入重做。")
p.write_text(t, encoding="utf-8")

# --- 288 ---
p = Path("mod_rebuild/docs/288-crop-production-and-cultivation-chain-20261028.md")
t = p.read_text(encoding="utf-8")
t = t.replace("- **A1/A2 的 29+10**：TFC 作物/灌木的**视觉与资源覆盖**；草莓已由 A 迁移为普通作物，不在 TFC 灌木重做内；",
              "- **A1/A2 的 29+10**：TFC 作物/灌木的**种植/收获流程替换 + 资源覆盖**；草莓已由 A 迁移为普通作物，不在 TFC 灌木重做内；")
t = t.replace("现有 `280 §11` 只把 29+11 的“资源覆盖”列成缺口，**没有把生产/培育链列进同一批次**；因此看起来“作物重做 = 换贴图”，实际设计是“重做整套种植与加工流程”。",
              "**2026-10-28 已定案**：29+10 必须重做整套种植与加工流程，不能只换贴图；TFC 29 的种植/收获/掉落由 B 覆盖，TFC 10 灌木替换采收/再生。")
t = t.replace("**只覆盖 `assets/tfc/**` 不可能实现六环节。** 这与 `126 A1` 的“资源覆盖、方块类不变”直接冲突。",
              "**只覆盖 `assets/tfc/**` 不可能实现六环节。** 因此 B 必须接管/扩展 TFC 作物行为；`126 A1` 的“资源覆盖、方块类不变”已作废。")
p.write_text(t, encoding="utf-8")

# --- 289 ---
p = Path("mod_rebuild/docs/289-crop-master-plan-20261028.md")
t = p.read_text(encoding="utf-8")
t = t.replace("| P4 | TFC 29 的视觉/资源覆盖与 B 行为接入 | 不影响存档；掉落不减少 |",
              "| P4 | TFC 29 种植/收获/掉落覆盖 + 资源覆盖 | 旧存档迁移/回退；不再要求掉落不减少 |")
t = t.replace("6. 不减少原掉落；", "6. TFC/A 原掉落可被覆盖，但必须保留回退基线；")
t = t.replace("2. TFC 29 与 A 87 是否共用同一套六环节，还是 TFC 29 只做资源覆盖。",
              "2. **已定**：TFC 29 与 A 87 共用同一套六环节；TFC 29 覆盖种植/收获/掉落，不做资源旁路。")
t = t.replace("5. “生产链”覆盖 86 还是 29+86，必须先定，否则无法排期。",
              "5. **已定**：生产链覆盖 A 87 + TFC 29 + B 43。")
p.write_text(t, encoding="utf-8")

# --- 290 ---
p = Path("mod_rebuild/docs/290-crop-flow-and-yield-balance-20261028.md")
t = p.read_text(encoding="utf-8")
t = t.replace("- **TFC 原版不降低 raw 产量**；B 只调整加工转化率与副产物；",
              "- **TFC 29 raw 允许被 B 覆盖**；旧 raw 只作回退基线，不再要求“不降低”；")
t = t.replace("> TFC 行 raw 保留 TFC 原值；A 行按 profile 目标调整，原始掉落改动需单独评审。",
              "> TFC 29 与 A 87 的 raw 都可被 B 覆盖；TFC 行原值仅作回退基线；TFC 谷物走 bundle→wet_grass。")
t = t.replace("- 副产物专项：`wet_grass` 潮湿草（谷物捆脱粒/野草/未成熟补偿，1–2 份/次，晒干 1:1 → `tfc:straw`）；",
              "- 副产物专项：`tfcagricultureplus:wet_grass`（B 新物品；谷物捆脱粒/野草/未成熟补偿，1–2 份/次，晒干 1:1 → `tfc:straw`）；")
t = t.replace("| P4 | TFC 29 资源层接入；不降低 raw 产量 | 视觉+行为兼容 |",
              "| P4 | TFC 29 种植/收获/掉落覆盖 + 资源接入 | 旧 raw 回退/存档迁移 |")
t = t.replace("1. 是否允许修改 A 的原始掉落表；TFC 29 的 raw 掉落建议不动。",
              "1. **已定**：A 与 TFC 29 的原始掉落都可被 B 覆盖；旧值保留为回退基线。")
t = t.replace("5. TFC 29 资源覆盖与 B 生产/培育链的行为层如何合并。",
              "5. **已定**：TFC 29 的种植/收获/掉落行为由 B 覆盖，资源覆盖只是其中一部分。")
p.write_text(t, encoding="utf-8")
print("source docs updated for TFC replacement/new wet grass")
