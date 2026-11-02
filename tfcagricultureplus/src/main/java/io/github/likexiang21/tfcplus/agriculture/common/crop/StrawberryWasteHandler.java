package io.github.likexiang21.tfcplus.agriculture.common.crop;

import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureItems;
import net.dries007.tfc.common.blocks.plant.fruit.Lifecycle;
import net.dries007.tfc.common.blocks.plant.fruit.SeasonalPlantBlock;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.block.Block;
import net.neoforged.neoforge.event.level.BlockEvent;

/**
 * Strawberry was migrated out of the TFC 10-bush set into A's ordinary crop record, but TFC's
 * strawberry bush still exists. This hook gives the A 87 strawberry record its real crop_waste
 * source without pretending it is one of the 10 TFC bushes.
 */
public final class StrawberryWasteHandler {

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
        final var waste = AgricultureItems.CROP_WASTE.get("strawberry");
        if (waste != null) {
            Block.popResource(level, event.getPos(), new ItemStack(waste.get(), 1));
        }
    }

    private StrawberryWasteHandler() {}
}
