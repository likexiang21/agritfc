from pathlib import Path

p = Path("mod_rebuild/tfcagricultureplus/src/main/java/io/github/likexiang21/tfcplus/agriculture/TFCAgriculturePlus.java")
t = p.read_text(encoding="utf-8")

imports = """package io.github.likexiang21.tfcplus.agriculture;

import net.minecraft.commands.Commands;
import net.minecraft.commands.arguments.coordinates.BlockPosArgument;
import net.minecraft.core.BlockPos;
import net.minecraft.core.Direction;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.phys.BlockHitResult;
import net.minecraft.world.phys.Vec3;
import net.neoforged.neoforge.event.RegisterCommandsEvent;
"""
t = t.replace("package io.github.likexiang21.tfcplus.agriculture;\n", imports, 1)

needle = "        NeoForge.EVENT_BUS.addListener(DirectSeedPlantingGate::onRightClickBlock);\n"
t = t.replace(needle, needle + "        NeoForge.EVENT_BUS.addListener(TFCAgriculturePlus::registerDebugCommands);\n", 1)

method = '''    private static void registerDebugCommands(RegisterCommandsEvent event) {
        event.getDispatcher().register(Commands.literal("tfcplusdebug_use")
            .then(Commands.argument("pos", BlockPosArgument.blockPos()).executes(context -> {
                final ServerPlayer player = context.getSource().getPlayerOrException();
                final BlockPos pos = BlockPosArgument.getLoadedBlockPos(context, "pos");
                player.gameMode.useItemOn(player, player.level(), player.getMainHandItem(), InteractionHand.MAIN_HAND,
                    new BlockHitResult(Vec3.atCenterOf(pos), Direction.UP, pos, false));
                return 1;
            })));
        event.getDispatcher().register(Commands.literal("tfcplusdebug_plant_seedling")
            .then(Commands.argument("pos", BlockPosArgument.blockPos()).executes(context -> {
                final ServerPlayer player = context.getSource().getPlayerOrException();
                final BlockPos pos = BlockPosArgument.getLoadedBlockPos(context, "pos");
                final var seedling = BuiltInRegistries.ITEM.get(
                    ResourceLocation.parse("tfcagricultureplus:seedling"));
                for (final ItemStack stack : player.getInventory().items) {
                    if (stack.getItem() == seedling) {
                        player.setItemInHand(InteractionHand.MAIN_HAND, stack.copy());
                        player.gameMode.useItemOn(player, player.level(), stack, InteractionHand.MAIN_HAND,
                            new BlockHitResult(Vec3.atCenterOf(pos), Direction.UP, pos, false));
                        break;
                    }
                }
                return 1;
            })));
        event.getDispatcher().register(Commands.literal("tfcplusdebug_drops").executes(context -> {
            final ServerPlayer player = context.getSource().getPlayerOrException();
            for (final var stack : player.getInventory().items) {
                if (!stack.isEmpty()) {
                    TFCAgriculturePlus.LOGGER.info("[TFC Agriculture Plus] inventory {} x{}",
                        stack.getItem(), stack.getCount());
                }
            }
            return 1;
        }));
    }

'''
needle2 = "    private void commonSetup(FMLCommonSetupEvent event) {"
t = t.replace(needle2, method + needle2, 1)
p.write_text(t, encoding="utf-8")
print("temporary debug commands re-added")
