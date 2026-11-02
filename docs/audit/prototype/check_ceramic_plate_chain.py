import json
from pathlib import Path

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/recipe")
problems = []

def load(rel):
    p = root / rel
    if not p.exists():
        problems.append(("missing", rel))
        return None
    return json.loads(p.read_text(encoding="utf-8"))

# 1. plate knapping must not equal TFC bowl pattern
plate = load("knapping/ceramic/unfired_plate.json")
bowl_pattern = ["#   #", " ### ", "     ", "#   #", " ### "]
if plate and plate.get("pattern") == bowl_pattern:
    problems.append(("plate pattern equals TFC bowl", plate.get("pattern")))
if plate and plate.get("result", {}).get("id") != "tfcagricultureplus:ceramic/unfired_plate":
    problems.append(("plate result", plate.get("result")))

# 2. unfired plate -> fired ceramic plate
heated = load("heating/ceramic/unfired_plate.json")
if heated and heated.get("result_item", {}).get("id") != "tfcagricultureplus:plate/ceramic":
    problems.append(("unfired plate heating", heated.get("result_item")))

# 3. white plate chain
white_unfired = load("crafting/ceramic/white_unfired_plate.json")
if white_unfired:
    ids = [i.get("item") for i in white_unfired.get("ingredients", [])]
    if "tfcagricultureplus:ceramic/unfired_plate" not in ids or "minecraft:white_dye" not in ids:
        problems.append(("white unfired plate inputs", ids))
white_heat = load("heating/ceramic/white_unfired_plate.json")
if white_heat and white_heat.get("result_item", {}).get("id") != "tfcagricultureplus:plate/ceramic_white":
    problems.append(("white plate heating", white_heat.get("result_item")))

# 4. 15 dyed plates all consume white plate
colors = ["black","blue","brown","cyan","gray","green","light_blue","light_gray","lime","magenta","orange","pink","purple","red","yellow"]
for color in colors:
    d = load(f"crafting/plate_ceramic_{color}.json")
    if not d:
        continue
    ids = [i.get("item") for i in d.get("ingredients", [])]
    if "tfcagricultureplus:plate/ceramic_white" not in ids:
        problems.append((f"dyed plate {color} missing white base", ids))
    if d.get("result", {}).get("id") != f"tfcagricultureplus:plate/ceramic_{color}":
        problems.append((f"dyed plate {color} result", d.get("result")))

# 5. duplicate bowl must be gone
for rel in ("crafting/bowl_wood.json", "crafting/bowl_ceramic.json"):
    if (root / rel).exists():
        problems.append(("duplicate bowl recipe remains", rel))

print("ceramic plate chain problems", len(problems))
for p in problems:
    print("PROBLEM", p)
