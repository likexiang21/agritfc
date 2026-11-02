from pathlib import Path

p = Path("mod_rebuild/tfcagricultureplus/src/main/java/io/github/likexiang21/tfcplus/agriculture/TFCAgriculturePlus.java")
t = p.read_text(encoding="utf-8")
if "tfcplusdebug_use_with" not in t:
    if "import com.mojang.brigadier.arguments.StringArgumentType;" not in t:
        t = t.replace("import net.minecraft.commands.Commands;\n",
                      "import com.mojang.brigadier.arguments.StringArgumentType;\nimport net.minecraft.commands.Commands;\n", 1)
    needle = '''        event.getDispatcher().register(Commands.literal("tfcplusdebug_drops").executes(context -> {
'''
    addition = '''        event.getDispatcher().register(Commands.literal("tfcplusdebug_use_with")
            .then(Commands.argument("pos", BlockPosArgument.blockPos())
                .then(Commands.argument("item", StringArgumentType.string()).executes(context -> {
                    final ServerPlayer player = context.getSource().getPlayerOrException();
                    final BlockPos pos = BlockPosArgument.getLoadedBlockPos(context, "pos");
                    final var item = BuiltInRegistries.ITEM.get(
                        ResourceLocation.parse(StringArgumentType.getString(context, "item")));
                    final ItemStack stack = new ItemStack(item);
                    player.setItemInHand(InteractionHand.MAIN_HAND, stack);
                    player.gameMode.useItemOn(player, player.level(), stack, InteractionHand.MAIN_HAND,
                        new BlockHitResult(Vec3.atCenterOf(pos), Direction.UP, pos, false));
                    return 1;
                }))));
        event.getDispatcher().register(Commands.literal("tfcplusdebug_drops").executes(context -> {
'''
    t = t.replace(needle, addition, 1)
p.write_text(t, encoding="utf-8")
print("use_with command added")
