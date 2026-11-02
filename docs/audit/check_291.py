from pathlib import Path
import json, re

p = Path("mod_rebuild/docs/291-crop-system-complete-modification-20261028.md")
t = p.read_text(encoding="utf-8")
rows = [l for l in t.splitlines() if re.match(r"^\| \d+ \| `", l)]
print("lines", len(t.splitlines()), "rows", len(rows))
print(rows[0][:900])
print(rows[-1][:900])
bad = []
for l in rows:
    c = [x for x in l.strip().strip("|").split("|")]
    if len(c) != 13:
        bad.append((c[1] if len(c) > 1 else "?", len(c)))
print("bad cols", bad[:5], len(bad))
a = [x["name"] for x in json.loads(Path("mod_rebuild/tfcfarmingplus/tools/contracts/crops-manifest.json").read_text(encoding="utf-8"))["crops"]]
tfc = ["alfalfa", "barley", "beet", "cabbage", "canola", "carrot", "cassava", "garlic",
       "green_bean", "jute", "lentil", "maize", "melon", "oat", "onion", "papyrus",
       "peanut", "potato", "pumpkin", "radish", "red_bell_pepper", "rice", "rye",
       "soybean", "squash", "sugarcane", "tomato", "wheat", "yellow_bell_pepper"]
txt = "\n".join(rows)
missing = [n for n in a + tfc if ("`" + n + "`") not in txt]
print("missing", missing)
