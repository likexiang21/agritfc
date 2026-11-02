from pathlib import Path

for name in ("NutTreeSaplingBlock.java", "SpiceTreeSaplingBlock.java"):
    p = Path("mod_rebuild/tfcagricultureplus/src/main/java/io/github/likexiang21/tfcplus/agriculture/common/block") / name
    t = p.read_text(encoding="utf-8")
    if "TFCAgriculturePlus.LOGGER" in t:
        print("already", name)
        continue
    t = t.replace(
        "import io.github.likexiang21.tfcplus.agriculture.common.crop.",
        "import io.github.likexiang21.tfcplus.agriculture.TFCAgriculturePlus;\nimport io.github.likexiang21.tfcplus.agriculture.common.crop.",
        1,
    )
    t = t.replace(
        "        final int height = 4 + random.nextInt(2);\n",
        "        int leavesPlaced = 0;\n        final int height = 4 + random.nextInt(2);\n",
        1,
    )
    t = t.replace(
        "                        level.setBlockAndUpdate(leafPos, leaves.defaultBlockState()\n"
        "                            .setValue(net.minecraft.world.level.block.LeavesBlock.PERSISTENT, true));",
        "                        level.setBlockAndUpdate(leafPos, leaves.defaultBlockState()\n"
        "                            .setValue(net.minecraft.world.level.block.LeavesBlock.PERSISTENT, true));\n"
        "                        leavesPlaced++;",
        1,
    )
    t = t.replace(
        "    }\n}\n",
        "        TFCAgriculturePlus.LOGGER.info(\"[TFC Agriculture Plus] grew {} at {}, leaves={}\", species.id(), pos, leavesPlaced);\n    }\n}\n",
        1,
    )
    p.write_text(t, encoding="utf-8")
    print("patched", name)
