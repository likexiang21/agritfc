from pathlib import Path

base = Path("mod_rebuild/tfcagricultureplus/src/main/java/io/github/likexiang21/tfcplus/agriculture/common/crop")

p = base / "BushRightClickHarvestHandler.java"
t = p.read_text(encoding="utf-8")
if "CreativeGuards.isCreative" not in t:
    anchor = "        if (event.getLevel().isClientSide() || !(event.getLevel() instanceof ServerLevel level)) {"
    t = t.replace(anchor, "        if (CreativeGuards.isCreative(event)) {\n            return;\n        }\n" + anchor, 1)
    p.write_text(t, encoding="utf-8")
    print("patched BushRightClickHarvestHandler")

p = base / "GrainHarvestHandler.java"
t = p.read_text(encoding="utf-8")
if "CreativeGuards.isCreative" not in t:
    # insert after the first method opening
    marker = "    public static void onBlockBreak(BlockEvent.BreakEvent event) {\n"
    if marker in t:
        t = t.replace(marker, marker + "        if (CreativeGuards.isCreative(event)) {\n            return;\n        }\n", 1)
        p.write_text(t, encoding="utf-8")
        print("patched GrainHarvestHandler")
    else:
        print("GrainHarvestHandler anchor miss")
