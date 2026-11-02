package io.github.likexiang21.tfcplus.agriculture.common.crop;

import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureDataComponents;
import net.dries007.tfc.common.TFCTags;
import net.dries007.tfc.common.blockentities.CropBlockEntity;
import net.dries007.tfc.common.blocks.crop.CropHelpers;
import net.dries007.tfc.util.calendar.Calendars;
import net.minecraft.core.BlockPos;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.block.BonemealableBlock;
import net.minecraft.world.level.block.FarmBlock;
import net.minecraft.world.level.block.state.BlockState;
import net.neoforged.neoforge.event.entity.player.PlayerInteractEvent;

/**
 * Applies the seed-treatment stage as a one-shot growth boost after the seed is planted.
 *
 * <p>This does not replace TFC planting: it schedules a check at the clicked position on the
 * next server task, and if the placed crop is Bonemealable it asks the crop to advance.
 * The crop decides whether that is valid, so no crop is forced to grow in an invalid state.
 */
public final class SeedTreatmentGrowthHandler {

    public static void onRightClickBlock(PlayerInteractEvent.RightClickBlock event) {
        if (event.isCanceled()) {
            return;
        }
        if (event.getLevel().isClientSide()) {
            return;
        }
        final ItemStack stack = event.getItemStack();
        final String stage = stack.get(AgricultureDataComponents.SEED_TREATMENT.get());
        if (stage == null || stage.isBlank()) {
            return;
        }
        final String itemId = BuiltInRegistries.ITEM.getKey(stack.getItem()).toString();
        if (!SeedTreatments.isSeedItemId(itemId)) {
            return;
        }
        final String species = CropPropagation.speciesFromSeedId(itemId);
        // If the direct-planting gate will cancel this seed (nursery/tuber/etc.), do not queue a
        // boost for a crop that is never placed.
        if (species != null && !CropPropagation.allowsDirectSowing(species)) {
            return;
        }
        final int boost = SeedTreatments.boostForStage(stage);
        if (boost <= 0 || !(event.getLevel() instanceof ServerLevel level)) {
            return;
        }
        final BlockState clicked = level.getBlockState(event.getPos());
        // Only a seed actually placed on TFC or vanilla farmland should receive the growth boost.
        if (!(clicked.getBlock() instanceof FarmBlock)
            && !clicked.is(TFCTags.Blocks.FARMLANDS)) {
            return;
        }
        final BlockPos target = event.getPos().relative(event.getFace());
        // Never boost an already occupied target (existing crop/torch/etc.).
        if (!level.getBlockState(target).canBeReplaced()) {
            return;
        }
        level.getServer().execute(() -> applyBoost(level, target, boost));
    }

    private static void applyBoost(ServerLevel level, BlockPos pos, int boost) {
        final BlockState state = level.getBlockState(pos);
        // A/TFC crops are driven by CropBlockEntity growth. Advance real TFC growth steps so yield,
        // nutrient use, climate limits and blockstate age stay consistent with normal growth.
        if (level.getBlockEntity(pos) instanceof CropBlockEntity crop) {
            final long now = Calendars.SERVER.getTicks();
            CropHelpers.growthTickStep(level, pos, state, level.random,
                now - CropHelpers.UPDATE_INTERVAL * boost, now, crop);
            return;
        }
        for (int i = 0; i < boost; i++) {
            if (!(state.getBlock() instanceof BonemealableBlock bonemealable)) {
                return;
            }
            if (!bonemealable.isValidBonemealTarget(level, pos, state)) {
                return;
            }
            if (!bonemealable.isBonemealSuccess(level, level.random, pos, state)) {
                return;
            }
            bonemealable.performBonemeal(level, level.random, pos, state);
        }
    }

    private SeedTreatmentGrowthHandler() {}
}
