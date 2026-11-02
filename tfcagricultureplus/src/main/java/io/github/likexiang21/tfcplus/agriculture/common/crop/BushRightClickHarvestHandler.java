package io.github.likexiang21.tfcplus.agriculture.common.crop;

import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureItems;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureShrubs;
import net.dries007.tfc.common.blocks.plant.fruit.Lifecycle;
import net.dries007.tfc.common.blocks.plant.fruit.SeasonalPlantBlock;
import net.minecraft.core.BlockPos;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.BlockState;
import net.neoforged.neoforge.event.entity.player.PlayerInteractEvent;

/**
 * Replaces right-click picking on the 10 TFC bushes with the same B-controlled
 * product + stateAfterPicking path as the break harvest. Empty-hand picking only.
 */
public final class BushRightClickHarvestHandler {

    public static void onRightClickBlock(PlayerInteractEvent.RightClickBlock event) {
        if (event.isCanceled()) {
            return;
        }
        if (CreativeGuards.isCreative(event)) {
            return;
        }
        if (event.getLevel().isClientSide() || !(event.getLevel() instanceof ServerLevel level)) {
            return;
        }
        if (!event.getItemStack().isEmpty()) {
            return;
        }
        final BlockState state = event.getLevel().getBlockState(event.getPos());
        final String id = BuiltInRegistries.BLOCK.getKey(state.getBlock()).toString();
        if (id.equals("tfc:plant/strawberry_bush")
            && state.getBlock() instanceof SeasonalPlantBlock bush
            && state.getValue(SeasonalPlantBlock.LIFECYCLE) == Lifecycle.FRUITING) {
            event.setCanceled(true);
            final BlockPos pos = event.getPos();
            final ItemStack product = bush.getProductItem(level.random);
            if (!product.isEmpty()) {
                Block.popResource(level, pos, product.copyWithCount(1 + level.random.nextInt(2)));
            }
            if (level.random.nextFloat() < 0.2F) {
                final Item seed = BuiltInRegistries.ITEM.get(
                    ResourceLocation.parse("tfcagricultureplus:seeds/strawberry"));
                if (seed != net.minecraft.world.item.Items.AIR) {
                    Block.popResource(level, pos, new ItemStack(seed, 1));
                }
            }
            final var waste = AgricultureItems.CROP_WASTE.get("strawberry");
            if (waste != null) {
                Block.popResource(level, pos, new ItemStack(waste.get(), 1));
            }
            level.setBlock(pos, bush.stateAfterPicking(state), Block.UPDATE_CLIENTS | Block.UPDATE_NEIGHBORS);
            return;
        }
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

    private BushRightClickHarvestHandler() {}
}
