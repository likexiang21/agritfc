import pathlib
import re
import zipfile

root = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources")
tfc = pathlib.Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods\TerraFirmaCraft-NeoForge-1.21.1-4.2.12.jar")
fl = pathlib.Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\mods\Firmalife-NeoForge-1.21.1-3.0.15.jar")

source = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/java/io/github/likexiang21/tfcplus/agriculture/common/crop/TfcCropSpecies.java").read_text(encoding="utf-8")
tfc_ids = re.findall(r'\("([a-z0-9_]+)"\)', source)

with zipfile.ZipFile(tfc) as z:
    tfc_names = set(z.namelist())
    missing = []
    for crop in tfc_ids:
        if f"assets/tfc/blockstates/crop/{crop}.json" not in tfc_names:
            missing.append("blockstate " + crop)
        if f"assets/tfc/models/item/seeds/{crop}.json" not in tfc_names:
            missing.append("seed model " + crop)
    print("TFC crops", len(tfc_ids), "missing", missing)

firmalife_plants = ["basil", "bay_laurel", "cardamom", "cilantro", "cumin", "oregano", "pimento", "vanilla"]
with zipfile.ZipFile(fl) as z:
    fl_names = set(z.namelist())
    for plant in firmalife_plants:
        b = f"assets/firmalife/blockstates/plant/{plant}.json"
        print("FL plant", plant, b in fl_names)

for plant in firmalife_plants:
    p = root / "assets/tfcagricultureplus/models/item/spice_waste" / (plant + ".json")
    print("B waste model", plant, p.exists())
