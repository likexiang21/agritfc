from pathlib import Path

p = Path("mod_rebuild/tfcagricultureplus/src/main/java/io/github/likexiang21/tfcplus/agriculture/TFCAgriculturePlus.java")
t = p.read_text(encoding="utf-8")
needle = '''        event.getDispatcher().register(Commands.literal("tfcplusdebug_drops").executes(context -> {
'''
addition = '''        event.getDispatcher().register(Commands.literal("tfcplusdebug_harvest")
            .then(Commands.argument("pos", BlockPosArgument.blockPos()).executes(context -> {
                final ServerPlayer player = context.getSource().getPlayerOrException();
                final BlockPos pos = BlockPosArgument.getLoadedBlockPos(context, "pos");
                player.gameMode.destroyBlock(pos);
                return 1;
            })));
        event.getDispatcher().register(Commands.literal("tfcplusdebug_drops").executes(context -> {
'''
if "tfcplusdebug_harvest" not in t:
    t = t.replace(needle, addition, 1)
p.write_text(t, encoding="utf-8")
print("harvest command added")
