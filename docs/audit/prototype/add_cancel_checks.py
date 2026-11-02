from pathlib import Path

base = Path("mod_rebuild/tfcagricultureplus/src/main/java/io/github/likexiang21/tfcplus/agriculture/common/crop")
files = [
    "BushHarvestHandler.java",
    "BushWasteHandler.java",
    "GrainHarvestHandler.java",
    "MacadamiaDropHandler.java",
    "SpiceSeedDropHandler.java",
    "StrawberrySeedDropHandler.java",
    "StrawberryWasteHandler.java",
    "WildNutDropHandler.java",
]
for name in files:
    p = base / name
    lines = p.read_text(encoding="utf-8").splitlines()
    out = []
    inserted = False
    for line in lines:
        out.append(line)
        if not inserted and "public static void onBlockBreak(BlockEvent.BreakEvent event) {" in line:
            out.append("        if (event.isCanceled()) {")
            out.append("            return;")
            out.append("        }")
            inserted = True
    if not inserted:
        raise SystemExit(f"anchor missing in {name}")
    p.write_text("\n".join(out) + "\n", encoding="utf-8")
    print("patched", name)
