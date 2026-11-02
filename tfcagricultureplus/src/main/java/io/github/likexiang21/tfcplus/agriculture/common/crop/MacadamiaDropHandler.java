package io.github.likexiang21.tfcplus.agriculture.common.crop;

import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureItems;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.block.Block;
import net.neoforged.neoforge.event.level.BlockEvent;

/**
 * Gives B macadamia nuts a real source from A's existing macadamia fruit-tree leaves.
 * A's leaves are not TFCLeavesBlock, so the TFC leaf mixin cannot cover them; this is a
 * dedicated additive drop hook instead. Pistachio/cashew still need their own trees.
 */
public final class MacadamiaDropHandler {

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
        if (!id.equals("tfcfarmingplus:plant/macadamia_leaves")) {
            return;
        }
        if (level.random.nextFloat() >= 0.05F) {
            return;
        }
        final var nut = AgricultureItems.NUTS.get("macadamia");
        final var shell = AgricultureItems.NUT_SHELLS.get("macadamia");
        if (nut != null) {
            Block.popResource(level, event.getPos(), new ItemStack(nut.get(), 1));
        }
        if (shell != null) {
            Block.popResource(level, event.getPos(), new ItemStack(shell.get(), 1));
        }
    }

    private MacadamiaDropHandler() {}
}
