import json
import zipfile
from pathlib import Path

tfc = Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods\TerraFirmaCraft-NeoForge-1.21.1-4.2.12.jar")
with zipfile.ZipFile(tfc) as z:
    biomes = sorted(
        "tfc:" + Path(n).stem
        for n in z.namelist()
        if n.startswith("data/tfc/worldgen/biome/") and n.endswith(".json")
    )

modifier = {
    "type": "neoforge:remove_features",
    "biomes": ["#minecraft:is_overworld"] + biomes,
    "features": [
        "tfc:plant/dead_bush",
        "tfc:plant/dead_bush_patch",
    ],
}
p = Path("mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/neoforge/biome_modifier/remove_duplicate_dead_bush.json")
p.write_text(json.dumps(modifier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("biomes", len(biomes), "file", p)
