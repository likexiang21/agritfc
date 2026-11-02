import json
from pathlib import Path

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources")
data = root / "data/tfcagricultureplus"
assets = root / "assets/tfcagricultureplus"
families = ["counter_cabinet", "half_cabinet", "sink_cabinet", "spice_rack", "food_display", "fruit_bowl"]
woods = ["acacia","ash","aspen","birch","blackwood","chestnut","douglas_fir","hickory","kapok","mangrove","maple","oak","palm","pine","rosewood","sequoia","spruce","sycamore","white_cedar","willow",
         "araucaria","baobab","beech","cypress","eucalyptus","fig","ginkgo","hevea","ipe","ironwood","mahoe","mahogany","teak","tualang"]
lang = {name: json.loads((assets / "lang" / f"{name}.json").read_text(encoding="utf-8"))
        for name in ("en_us", "zh_cn")}
problems = []
for family in families:
    for wood in woods:
        block_id = f"{family}/{wood}"
        recipe = data / "recipe/kitchen" / family / f"{wood}.json"
        loot = data / "loot_table/blocks" / family / f"{wood}.json"
        for p in (recipe, loot):
            if not p.exists():
                problems.append(f"missing {p}")
        if recipe.exists():
            d = json.loads(recipe.read_text(encoding="utf-8"))
            if d.get("type") != "minecraft:crafting_shaped":
                problems.append(f"{block_id}: recipe type {d.get('type')}")
            if d.get("result", {}).get("id") != f"tfcagricultureplus:{block_id}":
                problems.append(f"{block_id}: recipe result {d.get('result')}")
        if loot.exists():
            d = json.loads(loot.read_text(encoding="utf-8"))
            drops = d.get("pools", [])
            found = False
            for pool in drops:
                for entry in pool.get("entries", []):
                    if entry.get("type") == "minecraft:item" and entry.get("name") == f"tfcagricultureplus:{block_id}":
                        found = True
            if not found:
                problems.append(f"{block_id}: loot does not drop itself")
        for lang_name in ("en_us", "zh_cn"):
            key = f"block.tfcagricultureplus.{family}.{wood}"
            if key not in lang[lang_name]:
                problems.append(f"{block_id}: missing {lang_name} {key}")

print("families", len(families), "woods", len(woods), "expected", len(families) * len(woods))
print("problems", len(problems))
for p in problems[:20]:
    print("BAD", p)
if not problems:
    print("PASS: kitchen furniture recipes/loot")
