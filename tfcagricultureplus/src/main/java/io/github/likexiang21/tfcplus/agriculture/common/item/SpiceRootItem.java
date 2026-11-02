package io.github.likexiang21.tfcplus.agriculture.common.item;

import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureSpices;
import net.minecraft.core.BlockPos;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.context.UseOnContext;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.state.BlockState;

/** Plantable root propagule for root-form spices. */
public final class SpiceRootItem extends Item {

    private final String spiceId;

    public SpiceRootItem(String spiceId, Properties properties) {
        super(properties);
        this.spiceId = spiceId;
    }

    @Override
    public InteractionResult useOn(UseOnContext context) {
        final Level level = context.getLevel();
        if (level.isClientSide()) {
            return InteractionResult.sidedSuccess(true);
        }
        final var crop = AgricultureSpices.CROPS.get(spiceId);
        if (crop == null) {
            return InteractionResult.FAIL;
        }
        final BlockPos pos = context.getClickedPos().relative(context.getClickedFace());
        if (!level.getBlockState(pos).canBeReplaced()) {
            return InteractionResult.PASS;
        }
        final BlockState state = crop.get().defaultBlockState();
        if (!state.canSurvive(level, pos)) {
            return InteractionResult.FAIL;
        }
        level.setBlockAndUpdate(pos, state);
        final ItemStack stack = context.getItemInHand();
        if (context.getPlayer() == null || !context.getPlayer().isCreative()) {
            stack.shrink(1);
        }
        return InteractionResult.sidedSuccess(false);
    }
}
