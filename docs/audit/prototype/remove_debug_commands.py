from pathlib import Path
import re

p = Path("mod_rebuild/tfcagricultureplus/src/main/java/io/github/likexiang21/tfcplus/agriculture/TFCAgriculturePlus.java")
t = p.read_text(encoding="utf-8")

# remove listener
t = t.replace("        NeoForge.EVENT_BUS.addListener(TFCAgriculturePlus::registerDebugCommands);\n", "")

# remove method block
start = t.find("    private static void registerDebugCommands(RegisterCommandsEvent event) {")
if start != -1:
    end = t.find("    private void commonSetup(FMLCommonSetupEvent event) {", start)
    if end != -1:
        t = t[:start] + t[end:]

# remove debug-only imports
for line in [
    "import net.minecraft.commands.Commands;\n",
    "import net.minecraft.commands.arguments.coordinates.BlockPosArgument;\n",
    "import net.minecraft.core.BlockPos;\n",
    "import net.minecraft.core.Direction;\n",
    "import net.minecraft.world.InteractionHand;\n",
    "import net.minecraft.world.entity.item.ItemEntity;\n",
    "import net.minecraft.server.level.ServerPlayer;\n",
    "import net.minecraft.world.phys.BlockHitResult;\n",
    "import net.minecraft.world.phys.Vec3;\n",
    "import net.neoforged.neoforge.event.RegisterCommandsEvent;\n",
]:
    t = t.replace(line, "")

p.write_text(t, encoding="utf-8")
print("debug commands removed")
