package io.github.likexiang21.tfcplus.agriculture.common.crop;

import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;
import net.minecraft.world.level.block.Block;
import net.neoforged.neoforge.event.level.BlockEvent;

/** Gives the B strawberry crop its initial seed source from the still-present TFC strawberry bush. */
public final class StrawberrySeedDropHandler {

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
        if (!id.equals("tfc:plant/strawberry_bush")) {
            return;
        }
        if (level.random.nextFloat() >= 0.20F) {
            return;
        }
        final Item seed = BuiltInRegistries.ITEM.get(
            ResourceLocation.parse("tfcagricultureplus:seeds/strawberry"));
        if (seed != Items.AIR) {
            Block.popResource(level, event.getPos(), new ItemStack(seed, 1));
        }
    }

    private StrawberrySeedDropHandler() {}
}
