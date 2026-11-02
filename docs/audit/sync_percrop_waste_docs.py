from pathlib import Path

p = Path("mod_rebuild/docs/287-crop-redo-requirements-20261028.md")
t = p.read_text(encoding="utf-8")
t = t.replace(
    "- 副产物：**`wet_grass` 潮湿草**（野草收割/未成熟补偿，晒干→`tfc:straw`）与 **`green_waste` 废枝叶**（→`tfc:compost_greens/*`）必须有明确掉落/标签/出口，不得忽略。",
    "- 副产物：**`wet_grass` 潮湿草**（谷物捆脱粒/野草收割/未成熟补偿，晒干→`tfc:straw`）；**废枝叶是统称，逐作物实现 `crop_waste/<crop>`**（→`tfc:compost_greens/*`），不设通用 `green_waste`；谷物另有 `grain_bundle/<crop>` 先收捆再脱粒。"
)
p.write_text(t, encoding="utf-8")

p = Path("mod_rebuild/docs/289-crop-master-plan-20261028.md")
t = p.read_text(encoding="utf-8")
t = t.replace(
    "- 副产物：**`wet_grass` 潮湿草**（野草收割/未成熟作物补偿，可晒成 `tfc:straw`）；**`green_waste` 废枝叶**（进 `tfc:compost_greens/*` 绿色堆肥）；详见 291 §4.1。",
    "- 副产物：**`wet_grass` 潮湿草**（谷物捆脱粒/野草收割/未成熟补偿，可晒成 `tfc:straw`）；**废枝叶逐作物 `crop_waste/<crop>`**（进 `tfc:compost_greens/*`）；谷物另有 `grain_bundle/<crop>`；不设通用废枝叶物品；详见 291 §4.1。"
)
p.write_text(t, encoding="utf-8")

p = Path("mod_rebuild/docs/290-crop-flow-and-yield-balance-20261028.md")
t = p.read_text(encoding="utf-8")
t = t.replace(
    "- 副产物专项：`wet_grass` 潮湿草（1–2 份/次，晒干 1:1 → `tfc:straw`）与 `green_waste` 废枝叶（1–4 份/次，进 `tfc:compost_greens/*`）；不占主产品产量，也不得变成无用途物品。",
    "- 副产物专项：`wet_grass` 潮湿草（谷物捆脱粒/野草/未成熟补偿，1–2 份/次，晒干 1:1 → `tfc:straw`）；废枝叶按作物逐项 `crop_waste/<crop>`（1–4 份/次，进 `tfc:compost_greens/*`）；不设通用绿废料，不占主产品产量。"
)
p.write_text(t, encoding="utf-8")
print("source docs corrected for per-crop waste")
