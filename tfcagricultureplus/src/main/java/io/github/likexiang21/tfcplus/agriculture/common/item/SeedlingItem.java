package io.github.likexiang21.tfcplus.agriculture.common.item;

import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureDataComponents;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.context.UseOnContext;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.state.properties.IntegerProperty;
import org.jetbrains.annotations.Nullable;

/**
 * Generic seedling produced by the nursery tray. The original seed's item ID is stored in the
 * CROP_ID component; transplant resolves it to a BlockItem, or to a TFC crop block when the TFC
 * seed item itself is not a BlockItem, and places the crop only when the target is valid.
 */
public final class SeedlingItem extends Item {

    public SeedlingItem(Properties properties) {
        super(properties);
    }

    @Override
    public InteractionResult useOn(UseOnContext context) {
        final Level level = context.getLevel();
        if (level.isClientSide()) {
            return InteractionResult.sidedSuccess(true);
        }
        final ItemStack stack = context.getItemInHand();
        final String seedId = stack.get(AgricultureDataComponents.CROP_ID.get());
        if (seedId == null || seedId.isBlank()) {
            return InteractionResult.FAIL;
        }
        final BlockState cropState = cropStateForSeed(seedId);
        if (cropState == null) {
            return InteractionResult.FAIL;
        }
        final var pos = context.getClickedPos().relative(context.getClickedFace());
        if (!level.getBlockState(pos).canBeReplaced()) {
            return InteractionResult.PASS;
        }
        if (!cropState.canSurvive(level, pos)) {
            return InteractionResult.FAIL;
        }
        level.setBlockAndUpdate(pos, cropState);
        final String treatment = stack.get(AgricultureDataComponents.SEED_TREATMENT.get());
        if (level instanceof net.minecraft.server.level.ServerLevel serverLevel) {
            final int boost = io.github.likexiang21.tfcplus.agriculture.common.crop.SeedTreatments.boostForStage(treatment);
            if (boost > 0) {
                serverLevel.getServer().execute(() -> applyBoost(serverLevel, pos, boost));
            }
        }
        if (context.getPlayer() == null || !context.getPlayer().isCreative()) {
            stack.shrink(1);
        }
        return InteractionResult.sidedSuccess(false);
    }

    /**
     * Resolves a seed item to the block state a nursery seedling should place.
     *
     * <p>TFC seeds are not {@link BlockItem}s, so the TFC crop block is resolved from the stable
     * {@code tfc:crop/<species>} ID. A/B and Firmalife BlockItem seeds keep the generic path.
     */
    @Nullable
    public static BlockState cropStateForSeed(String seedItemId) {
        if (seedItemId == null || seedItemId.isBlank()) {
            return null;
        }
        final Item seed = BuiltInRegistries.ITEM.get(ResourceLocation.parse(seedItemId));
        final BlockState state;
        if (seed instanceof BlockItem blockItem) {
            state = blockItem.getBlock().defaultBlockState();
        } else if (seedItemId.startsWith("tfc:seeds/")) {
            final String species = seedItemId.substring("tfc:seeds/".length());
            final Block block = BuiltInRegistries.BLOCK.get(
                ResourceLocation.parse("tfc:crop/" + species));
            if (block == null || block == net.minecraft.world.level.block.Blocks.AIR) {
                return null;
            }
            state = block.defaultBlockState();
        } else if (seedItemId.startsWith("tfcfarmingplus:seeds/")) {
            final String species = seedItemId.substring("tfcfarmingplus:seeds/".length());
            final Block block = BuiltInRegistries.BLOCK.get(
                ResourceLocation.parse("tfcfarmingplus:crop/" + species));
            if (block == null || block == net.minecraft.world.level.block.Blocks.AIR) {
                return null;
            }
            state = block.defaultBlockState();
        } else {
            return null;
        }
        return withZeroAge(state);
    }

    public static boolean canResolveSeed(String seedItemId) {
        return cropStateForSeed(seedItemId) != null;
    }

    private static BlockState withZeroAge(BlockState state) {
        for (final var property : state.getProperties()) {
            if (property instanceof IntegerProperty integer && property.getName().equals("age")) {
                return state.setValue(integer, 0);
            }
        }
        return state;
    }

    private static void applyBoost(net.minecraft.server.level.ServerLevel level, net.minecraft.core.BlockPos pos, int boost) {
        final BlockState state = level.getBlockState(pos);
        if (level.getBlockEntity(pos) instanceof net.dries007.tfc.common.blockentities.CropBlockEntity crop) {
            final long now = net.dries007.tfc.util.calendar.Calendars.SERVER.getTicks();
            net.dries007.tfc.common.blocks.crop.CropHelpers.growthTickStep(level, pos, state,
                level.random, now - net.dries007.tfc.common.blocks.crop.CropHelpers.UPDATE_INTERVAL * boost, now, crop);
            return;
        }
        for (int i = 0; i < boost; i++) {
            final BlockState current = level.getBlockState(pos);
            if (!(current.getBlock() instanceof net.minecraft.world.level.block.BonemealableBlock bonemealable)) {
                return;
            }
            if (!bonemealable.isValidBonemealTarget(level, pos, current)
                || !bonemealable.isBonemealSuccess(level, level.random, pos, current)) {
                return;
            }
            bonemealable.performBonemeal(level, level.random, pos, current);
        }
    }

    public static ItemStack forSeed(String seedItemId) {
        final ItemStack stack = new ItemStack(io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureItems.SEEDLING.get());
        stack.set(AgricultureDataComponents.CROP_ID.get(), seedItemId);
        return stack;
    }
}
