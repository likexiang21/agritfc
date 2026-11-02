from pathlib import Path

p = Path("mod_rebuild/docs/288-crop-production-and-cultivation-chain-20261028.md")
t = p.read_text(encoding="utf-8")
t = t.replace("- 未成熟破坏应有补偿（新鲜草等），见 `117 §6.8 ⑤`；",
              "- 未成熟破坏应有补偿：**潮湿草 `wet_grass`**（可晒成 `tfc:straw`），见 `117 §6.8 ⑤`；")
t = t.replace("未成熟破坏 → 新鲜草补偿", "未成熟破坏 → **潮湿草 `wet_grass`** 补偿")
t = t.replace("主产品 + 次产品一次产出（`tfc:extra_products`）；未成熟破坏 → 新鲜草补偿",
              "主产品 + 次产品一次产出（`tfc:extra_products`）；未成熟破坏 → **潮湿草 `wet_grass`** 补偿；废枝叶 → `green_waste`（绿色堆肥）")
p.write_text(t, encoding="utf-8")

p = Path("mod_rebuild/docs/289-crop-master-plan-20261028.md")
t = p.read_text(encoding="utf-8")
needle = "- 没有“只换贴图/只掉种子”的条目。"
if needle not in t:
    raise SystemExit("289 needle missing")
t = t.replace(needle, needle + "\n- 副产物：**`wet_grass` 潮湿草**（野草收割/未成熟作物补偿，可晒成 `tfc:straw`）；**`green_waste` 废枝叶**（进 `tfc:compost_greens/*` 绿色堆肥）；详见 291 §4.1。")
p.write_text(t, encoding="utf-8")

p = Path("mod_rebuild/docs/290-crop-flow-and-yield-balance-20261028.md")
t = p.read_text(encoding="utf-8")
needle = "- 所有产量目标以 20 次收获的均值/区间验收，不用单次极值。"
if needle not in t:
    raise SystemExit("290 needle missing")
t = t.replace(needle, needle + "\n- 副产物专项：`wet_grass` 潮湿草（1–2 份/次，晒干 1:1 → `tfc:straw`）与 `green_waste` 废枝叶（1–4 份/次，进 `tfc:compost_greens/*`）；不占主产品产量，也不得变成无用途物品。")
p.write_text(t, encoding="utf-8")
print("source docs updated")
