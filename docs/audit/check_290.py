from pathlib import Path
import json, re

t = Path("mod_rebuild/docs/290-crop-flow-and-yield-balance-20261028.md").read_text(encoding="utf-8")
rows = [l for l in t.splitlines() if re.match(r"^\| \d+ \| `", l)]
print("rows", len(rows))
bad = []
for l in rows:
    cells = [x.strip() for x in l.strip().strip("|").split("|")]
    if len(cells) != 10:
        bad.append((cells[1] if len(cells) > 1 else "?", len(cells)))
print("bad col count", bad[:10], len(bad))
crops = [x["name"] for x in json.loads(Path("mod_rebuild/tfcfarmingplus/tools/contracts/crops-manifest.json").read_text(encoding="utf-8"))["crops"]]
tfc = ["alfalfa", "barley", "beet", "cabbage", "canola", "carrot", "cassava", "garlic",
       "green_bean", "jute", "lentil", "maize", "melon", "oat", "onion", "papyrus",
       "peanut", "potato", "pumpkin", "radish", "red_bell_pepper", "rice", "rye",
       "soybean", "squash", "sugarcane", "tomato", "wheat", "yellow_bell_pepper"]
text = "\n".join(rows)
missing = [n for n in crops + tfc if ("`" + n + "`") not in text]
print("missing", missing)
flow_values = set(re.findall(r"`([a-z-]+)` \| [0-9]", t))
print("flow-ish values", sorted(flow_values))
