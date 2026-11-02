package io.github.likexiang21.tfcplus.agriculture.common.crop;

import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureItems;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.block.Block;
import net.neoforged.neoforge.event.level.BlockEvent;

/**
 * Temporary obtainability source for pistachio/cashew before their dedicated trees exist.
 * These two are the only B nuts without a mapped tree; grass drops keep the B 43 nut set
 * obtainable without pretending the trees are implemented.
 */
public final class WildNutDropHandler {

    private static final String[] NUTS = {"pistachio", "cashew"};

    public static void onBlockBreak(BlockEvent.BreakEvent event) {
        if (event.isCanceled()) {
            return;
        }
        if (CreativeGuards.isCreative(event)) {
            return;
        }
        if (!(event.getLevel() instanceof ServerLevel level)) {
            return;
        }
        final String id = BuiltInRegistries.BLOCK.getKey(event.getState().getBlock()).toString();
        if (!id.equals("minecraft:short_grass") && !id.equals("minecraft:tall_grass")) {
            return;
        }
        if (level.random.nextFloat() >= 0.02F) {
            return;
        }
        final String nutId = NUTS[level.random.nextInt(NUTS.length)];
        final var nut = AgricultureItems.NUTS.get(nutId);
        final var shell = AgricultureItems.NUT_SHELLS.get(nutId);
        if (nut != null) {
            Block.popResource(level, event.getPos(), new ItemStack(nut.get(), 1));
        }
        if (shell != null) {
            Block.popResource(level, event.getPos(), new ItemStack(shell.get(), 1));
        }
    }

    private WildNutDropHandler() {}
}
