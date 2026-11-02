from pathlib import Path

p = Path("mod_rebuild/tfcagricultureplus/src/main/java/io/github/likexiang21/tfcplus/agriculture/TFCAgriculturePlus.java")
t = p.read_text(encoding="utf-8")
for imp in [
    "import net.minecraft.core.Direction;",
    "import net.minecraft.world.phys.BlockHitResult;",
    "import net.minecraft.world.phys.Vec3;",
]:
    if imp not in t:
        t = t.replace("import net.minecraft.core.BlockPos;\n", "import net.minecraft.core.BlockPos;\n" + imp + "\n", 1)

needle = '''        event.getDispatcher().register(Commands.literal("tfcplusdebug_drops").executes(context -> {
'''
addition = '''        event.getDispatcher().register(Commands.literal("tfcplusdebug_use")
            .then(Commands.argument("pos", BlockPosArgument.blockPos()).executes(context -> {
                final ServerPlayer player = context.getSource().getPlayerOrException();
                final BlockPos pos = BlockPosArgument.getLoadedBlockPos(context, "pos");
                final var state = player.level().getBlockState(pos);
                state.use(player.level(), player,
                    new BlockHitResult(Vec3.atCenterOf(pos), Direction.UP, pos, false));
                return 1;
            })));
        event.getDispatcher().register(Commands.literal("tfcplusdebug_drops").executes(context -> {
'''
if "tfcplusdebug_use" not in t:
    t = t.replace(needle, addition, 1)
p.write_text(t, encoding="utf-8")
print("use command added")
