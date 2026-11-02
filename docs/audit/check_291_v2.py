from pathlib import Path
import re, json

p = Path("mod_rebuild/docs/291-crop-system-complete-modification-20261028.md")
t = p.read_text(encoding="utf-8")
rows = [l for l in t.splitlines() if re.match(r"^\| \d+ \| `", l)]
print("lines", len(t.splitlines()), "numbered rows", len(rows))
print("A rows", sum("A·" in l for l in rows), "TFC rows", sum("TFC·" in l for l in rows))
print("spice rows", t.count("| `black_pepper` |"), "nut rows", t.count("| pistachio |"), "mushrooms 15?", t.count("| `turkey_tail` |"))
a = [x["name"] for x in json.loads(Path("mod_rebuild/tfcfarmingplus/tools/contracts/crops-manifest.json").read_text(encoding="utf-8"))["crops"]]
tfc = ["alfalfa", "barley", "beet", "cabbage", "canola", "carrot", "cassava", "garlic",
       "green_bean", "jute", "lentil", "maize", "melon", "oat", "onion", "papyrus",
       "peanut", "potato", "pumpkin", "radish", "red_bell_pepper", "rice", "rye",
       "soybean", "squash", "sugarcane", "tomato", "wheat", "yellow_bell_pepper"]
txt = "\n".join(rows)
print("missing A/TFC", [n for n in a + tfc if ("`" + n + "`") not in txt])
for line in t.splitlines():
    if line.startswith("| B 新增") or line.startswith("| 全部作物"):
        print(line)
