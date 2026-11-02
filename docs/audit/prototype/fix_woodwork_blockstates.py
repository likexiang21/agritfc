import json
from pathlib import Path

assets = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus")
TFC = ["acacia","ash","aspen","birch","blackwood","chestnut","douglas_fir","hickory","kapok","mangrove","maple","oak","palm","pine","rosewood","sequoia","spruce","sycamore","white_cedar","willow"]
AFC = ["araucaria","baobab","beech","cypress","eucalyptus","fig","ginkgo","hevea","ipe","ironwood","mahoe","mahogany","teak","tualang"]

facings = {"north": 0, "east": 90, "south": 180, "west": 270}
for wood in TFC + AFC:
    # log: no facing
    p = assets / "blockstates/debarked_log" / f"{wood}.json"
    p.write_text(json.dumps({"variants": {"": {"model": f"tfcagricultureplus:block/debarked_log/{wood}"}}}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for kind in ("debarked_half", "debarked_quarter"):
        variants = {}
        for facing, y in facings.items():
            entry = {"model": f"tfcagricultureplus:block/{kind}/{wood}"}
            if y:
                entry["y"] = y
            variants[f"facing={facing}"] = entry
        p = assets / "blockstates" / kind / f"{wood}.json"
        p.write_text(json.dumps({"variants": variants}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("rewrote blockstates")
