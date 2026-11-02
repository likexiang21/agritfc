package io.github.likexiang21.tfcplus.agriculture.common.crop;

import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureShrubs;
import net.dries007.tfc.common.blocks.plant.fruit.Lifecycle;
import net.dries007.tfc.common.blocks.plant.fruit.SeasonalPlantBlock;
import net.minecraft.core.BlockPos;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.BlockState;
import net.neoforged.neoforge.event.level.BlockEvent;

/**
 * Replaces the break-harvest of a fruiting TFC berry bush with a controlled harvest + regrowth:
 * crop the product, leave the bush in its post-pick state, cancel the block break.
 *
 * <p>Non-fruiting bushes keep normal TFC behavior. This is deliberately limited to the exact
 * 10 TFC bush IDs and does not touch A's bushes or strawberry.
 */
public final class BushHarvestHandler {

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
        final String id = net.minecraft.core.registries.BuiltInRegistries.BLOCK
            .getKey(state.getBlock()).toString();
        final BushSpecies species = BushSpecies.fromTfcBushBlockId(id);
        if (species == null || !(state.getBlock() instanceof SeasonalPlantBlock bush)) {
            return;
        }
        if (state.getValue(SeasonalPlantBlock.LIFECYCLE) != Lifecycle.FRUITING) {
            return;
        }

        event.setCanceled(true);
        final BlockPos pos = event.getPos();
        final ItemStack product = bush.getProductItem(level.random);
        if (!product.isEmpty()) {
            Block.popResource(level, pos, product.copyWithCount(1 + level.random.nextInt(2)));
        }
        final var waste = AgricultureShrubs.BUSH_WASTE.get(species.id());
        if (waste != null) {
            Block.popResource(level, pos, new ItemStack(waste.get(), 1));
        }
        level.setBlock(pos, bush.stateAfterPicking(state), Block.UPDATE_CLIENTS | Block.UPDATE_NEIGHBORS);
    }

    private BushHarvestHandler() {}
}
