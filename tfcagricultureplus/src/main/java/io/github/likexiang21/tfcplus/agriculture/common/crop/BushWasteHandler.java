package io.github.likexiang21.tfcplus.agriculture.common.crop;

import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureShrubs;
import net.dries007.tfc.common.blocks.plant.fruit.Lifecycle;
import net.dries007.tfc.common.blocks.plant.fruit.SeasonalPlantBlock;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.BlockState;
import net.neoforged.neoforge.event.level.BlockEvent;

/**
 * Adds actual bush residue to the 10 remaining TFC berry bushes.
 *
 * <p>This is a byproduct hook only: the original TFC berry/lifecycle drops are not cancelled.
 * Replacing the full TFC bush harvest/regrowth lifecycle remains a separate, larger batch.
 */
public final class BushWasteHandler {

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
        final BlockState state = event.getState();
        // Fruiting bushes are cancelled and harvested by BushHarvestHandler, which owns the
        // single waste drop. Skipping here also avoids a duplicate when this listener runs first.
        if (state.hasProperty(SeasonalPlantBlock.LIFECYCLE)
            && state.getValue(SeasonalPlantBlock.LIFECYCLE) == Lifecycle.FRUITING) {
            return;
        }
        final ResourceLocation blockId = BuiltInRegistries.BLOCK.getKey(state.getBlock());
        final BushSpecies bush = BushSpecies.fromTfcBushBlockId(blockId.toString());
        if (bush == null) {
            return;
        }
        final var waste = AgricultureShrubs.BUSH_WASTE.get(bush.id());
        if (waste != null) {
            Block.popResource(level, event.getPos(), new ItemStack(waste.get(), 1));
        }
    }

    private BushWasteHandler() {}
}
