package io.github.likexiang21.tfcplus.agriculture.common.crop;

import net.dries007.tfc.common.TFCTags;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.network.chat.Component;
import net.minecraft.world.level.block.FarmBlock;
import net.minecraft.world.level.block.state.BlockState;
import net.neoforged.neoforge.event.entity.player.PlayerInteractEvent;

/**
 * Gates A/TFC/B seed planting according to the per-species propagation method.
 *
 * <p>TFC seeds are part of the same table: {@code tfc:seeds/<crop>} is classified as
 * {@link CropPropagation.Method#SEED_DIRECT} and therefore keeps TFC's normal direct sowing.
 * A/B seeds whose species is marked direct fall through; nursery/tuber/rhizome/etc. species are
 * cancelled with a method-specific hint. Seeds from other mods (for example Firmalife) are not
 * silently blocked just because they are not in B's table.
 */
public final class DirectSeedPlantingGate {

    public static void onRightClickBlock(PlayerInteractEvent.RightClickBlock event) {
        if (event.isCanceled()) {
            return;
        }
        final String itemId = BuiltInRegistries.ITEM.getKey(event.getItemStack().getItem()).toString();
        if (!SeedTreatments.isSeedItemId(itemId)) {
            return;
        }
        final BlockState target = event.getLevel().getBlockState(event.getPos());
        if (!isFarmland(target)) {
            return;
        }
        final String species = CropPropagation.speciesFromSeedId(itemId);
        if (species == null) {
            // Not an A/TFC/B seed (Firmalife and other mods own their own planting rules).
            return;
        }
        if (CropPropagation.allowsDirectSowing(species)) {
            return;
        }
        if (event.getEntity() != null) {
            event.getEntity().displayClientMessage(
                Component.translatable("message.tfcagricultureplus.seed_requires_nursery"), true);
        }
        event.setCanceled(true);
    }

    private static boolean isFarmland(BlockState state) {
        return state.getBlock() instanceof FarmBlock || state.is(TFCTags.Blocks.FARMLANDS);
    }

    private DirectSeedPlantingGate() {}
}
