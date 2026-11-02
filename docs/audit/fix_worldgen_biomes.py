import json, pathlib, zipfile
root = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources")
jar = pathlib.Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods\TerraFirmaCraft-NeoForge-1.21.1-4.2.12.jar")
with zipfile.ZipFile(jar) as z:
    ids = sorted(n[len("data/tfc/worldgen/biome/"):-5] for n in z.namelist()
                 if n.startswith("data/tfc/worldgen/biome/") and n.endswith(".json"))
exclude = ("ocean", "lake", "river", "ice_sheet", "subglacial")
land = ["tfc:" + i for i in ids if not any(x in i for x in exclude)]
base = ["#minecraft:is_forest", "#minecraft:is_taiga", "#minecraft:is_jungle"]
print("TFC land biomes", len(land))
for name in ("wild_mushroom_biomes", "nut_tree_biomes", "spice_tree_biomes"):
    p = root / "data/tfcagricultureplus/tags/worldgen/biome" / (name + ".json")
    d = json.loads(p.read_text(encoding="utf-8"))
    values = list(d.get("values", []))
    for v in base + land:
        if v not in values:
            values.append(v)
    d["values"] = values
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(p.name, len(values))
