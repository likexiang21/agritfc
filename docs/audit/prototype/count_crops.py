import pathlib
import re

base = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/java/io/github/likexiang21/tfcplus/agriculture/common/crop")

s = (base / "CropWasteCrops.java").read_text(encoding="utf-8")
vals = re.findall(r'"([a-z0-9_]+)"', s)
print("crop waste count", len(set(vals)), "tokens", len(vals))

s2 = (base / "CropPropagation.java").read_text(encoding="utf-8")
vals2 = re.findall(r'"([a-z0-9_]+)"', s2)
print("propagation tokens", len(set(vals2)))

for f in ("TfcCropSpecies.java", "GrainCrop.java", "BushSpecies.java", "NutBearingTree.java", "SpiceSpecies.java", "MushroomSpecies.java"):
    txt = (base / f).read_text(encoding="utf-8")
    vals = re.findall(r'"([a-z0-9_]+)"', txt)
    print(f, len(set(vals)), "unique")
