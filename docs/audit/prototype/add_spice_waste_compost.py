import json
import pathlib
import re

root = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/data/tfc/tags/item/compost_greens")
s = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/java/io/github/likexiang21/tfcplus/agriculture/common/crop/SpiceSpecies.java").read_text(encoding="utf-8")
entries = re.findall(r'([A-Z_]+)\("([a-z0-9_]+)", "([a-z]+)"\)', s)
print("spice entries", len(entries), entries)

by_cat = {"high": [], "medium": [], "low": []}
for _, spice, form in entries:
    cat = "high" if form == "herb" else "medium"
    by_cat[cat].append("tfcagricultureplus:spice_waste/" + spice)

for cat, extra in by_cat.items():
    p = root / (cat + ".json")
    data = json.loads(p.read_text(encoding="utf-8"))
    merged = data["values"]
    for item in extra:
        if item not in merged:
            merged.append(item)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(p.name, "values", len(merged), "added", len(extra))
