package io.github.likexiang21.tfcplus.agriculture.common.crop;

import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureItems;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureSpices;
import net.dries007.tfc.common.TFCTags;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.block.Block;
import net.neoforged.neoforge.event.level.BlockEvent;

/**
 * Firmalife's plants are part of B's residue chain, not an exception.
 *
 * <p>The eight planter herbs append B spice waste and respect Firmalife's knife gate. The remaining
 * Firmalife plant blocks (cocoa/fig/grapes/pineapple/nightshade and the two grape-string plants)
 * append a dedicated B crop-waste item, so every Firmalife plant has a B-side residue outlet.
 */
public final class FirmalifePlantWasteHandler {

    private static final String PLANT_PREFIX = "firmalife:plant/";
    private static final String GRAPE_PREFIX = "firmalife:grape_string_plant_";

    public static void onBlockBreak(BlockEvent.BreakEvent event) {
        if (event.isCanceled() || !(event.getLevel() instanceof ServerLevel level)) {
            return;
        }
        if (CreativeGuards.isCreative(event)) {
            return;
        }
        final String blockId = BuiltInRegistries.BLOCK.getKey(event.getState().getBlock()).toString();
        final String species;
        if (blockId.startsWith(PLANT_PREFIX)) {
            species = blockId.substring(PLANT_PREFIX.length());
        } else if (blockId.startsWith(GRAPE_PREFIX)) {
            species = "grape_string_" + blockId.substring(GRAPE_PREFIX.length());
        } else {
            return;
        }
        if (AgricultureItems.FIRMALIFE_WASTE.contains(species)) {
            final var waste = AgricultureItems.CROP_WASTE.get(species);
            if (waste != null) {
                Block.popResource(level, event.getPos(), new ItemStack(waste.get(), 1));
            }
            return;
        }
        if (event.getPlayer() == null
            || !event.getPlayer().getMainHandItem().is(TFCTags.Items.TOOLS_KNIFE)) {
            return;
        }
        final var waste = AgricultureSpices.WASTES.get(species);
        if (waste != null) {
            Block.popResource(level, event.getPos(), new ItemStack(waste.get(), 1));
        }
    }

    private FirmalifePlantWasteHandler() {}
}
