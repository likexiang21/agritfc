from pathlib import Path

base = Path("mod_rebuild/tfcagricultureplus/src/main/java/io/github/likexiang21/tfcplus/agriculture/common/crop")

def inject(name, anchor, guard):
    p = base / name
    t = p.read_text(encoding="utf-8")
    if "CreativeGuards.isCreative" in t:
        return
    if anchor not in t:
        print("ANCHOR MISS", name)
        return
    t = t.replace(anchor, guard + anchor, 1)
    p.write_text(t, encoding="utf-8")
    print("patched", name)

inject("BushWasteHandler.java",
       "        if (!(event.getLevel() instanceof ServerLevel level)) {",
       "        if (CreativeGuards.isCreative(event)) {\n            return;\n        }\n")
inject("BushHarvestHandler.java",
       "        if (!(event.getLevel() instanceof ServerLevel level)) {",
       "        if (CreativeGuards.isCreative(event)) {\n            return;\n        }\n")
inject("CropWasteHandler.java",
       "        if (!(event.getLevel() instanceof ServerLevel level)) {",
       "        if (CreativeGuards.isCreative(event)) {\n            return;\n        }\n")
inject("MacadamiaDropHandler.java",
       "        if (!(event.getLevel() instanceof ServerLevel level)) {",
       "        if (CreativeGuards.isCreative(event)) {\n            return;\n        }\n")
inject("WildNutDropHandler.java",
       "        if (!(event.getLevel() instanceof ServerLevel level)) {",
       "        if (CreativeGuards.isCreative(event)) {\n            return;\n        }\n")
inject("SpiceSeedDropHandler.java",
       "        if (!(event.getLevel() instanceof ServerLevel level)) {",
       "        if (CreativeGuards.isCreative(event)) {\n            return;\n        }\n")
inject("StrawberryWasteHandler.java",
       "        if (!(event.getLevel() instanceof ServerLevel level)) {",
       "        if (CreativeGuards.isCreative(event)) {\n            return;\n        }\n")
inject("StrawberrySeedDropHandler.java",
       "        if (!(event.getLevel() instanceof ServerLevel level)) {",
       "        if (CreativeGuards.isCreative(event)) {\n            return;\n        }\n")
inject("TfcSeedReturnHandler.java",
       "        if (event.isCanceled() || !(event.getLevel() instanceof ServerLevel level)) {",
       "        if (CreativeGuards.isCreative(event)) {\n            return;\n        }\n")
inject("ACropSeedReturnHandler.java",
       "        if (event.isCanceled() || !(event.getLevel() instanceof ServerLevel level)) {",
       "        if (CreativeGuards.isCreative(event)) {\n            return;\n        }\n")
print("done")
