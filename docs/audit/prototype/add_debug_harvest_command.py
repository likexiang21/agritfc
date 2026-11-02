from pathlib import Path

p = Path("mod_rebuild/tfcagricultureplus/src/main/java/io/github/likexiang21/tfcplus/agriculture/TFCAgriculturePlus.java")
t = p.read_text(encoding="utf-8")

imports = """package io.github.likexiang21.tfcplus.agriculture;

import net.minecraft.commands.Commands;
import net.minecraft.commands.arguments.coordinates.BlockPosArgument;
import net.minecraft.core.BlockPos;
import net.minecraft.server.level.ServerPlayer;
import net.neoforged.neoforge.event.RegisterCommandsEvent;
"""
t = t.replace("package io.github.likexiang21.tfcplus.agriculture;\n", imports, 1)

needle = "        NeoForge.EVENT_BUS.addListener(DirectSeedPlantingGate::onRightClickBlock);\n"
t = t.replace(needle, needle + "        NeoForge.EVENT_BUS.addListener(TFCAgriculturePlus::registerDebugCommands);\n", 1)

method = '''    private static void registerDebugCommands(RegisterCommandsEvent event) {
        event.getDispatcher().register(Commands.literal("tfcplusdebug_harvest")
            .then(Commands.argument("pos", BlockPosArgument.blockPos()).executes(context -> {
                final ServerPlayer player = context.getSource().getPlayerOrException();
                final BlockPos pos = BlockPosArgument.getLoadedBlockPos(context, "pos");
                player.gameMode.destroyBlock(pos);
                return 1;
            })));
    }

'''
needle2 = "    private void commonSetup(FMLCommonSetupEvent event) {"
t = t.replace(needle2, method + needle2, 1)

p.write_text(t, encoding="utf-8")
print("debug command added")
