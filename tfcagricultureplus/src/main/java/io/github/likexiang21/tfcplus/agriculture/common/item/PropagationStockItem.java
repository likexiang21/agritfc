package io.github.likexiang21.tfcplus.agriculture.common.item;

import io.github.likexiang21.tfcplus.agriculture.common.crop.PropagationStock;
import net.minecraft.core.BlockPos;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.sounds.SoundSource;
import net.minecraft.tags.FluidTags;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.context.BlockPlaceContext;
import net.minecraft.world.item.context.UseOnContext;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.FarmBlock;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.state.properties.IntegerProperty;
import net.minecraft.world.level.block.state.properties.Property;

/** Vegetative planting stock: places the species crop on farmland or shallow water. */
public final class PropagationStockItem extends Item {

    private final PropagationStock.Entry entry;

    public PropagationStockItem(Properties properties, PropagationStock.Entry entry) {
        super(properties);
        this.entry = entry;
    }

    @Override
    public InteractionResult useOn(UseOnContext context) {
        final Level level = context.getLevel();
        final BlockPos clicked = context.getClickedPos();
        final BlockState clickedState = level.getBlockState(clicked);
        final Block block = BuiltInRegistries.BLOCK.get(ResourceLocation.parse(entry.cropBlockId()));
        if (block == null || block == net.minecraft.world.level.block.Blocks.AIR) {
            return InteractionResult.PASS;
        }

        BlockPos cropPos;
        BlockState state;
        final String clickedId = BuiltInRegistries.BLOCK.getKey(clickedState.getBlock()).toString();
        if (clickedState.getBlock() instanceof FarmBlock || clickedId.endsWith("farmland")) {
            cropPos = clicked.above();
            if (!level.isEmptyBlock(cropPos)) return InteractionResult.PASS;
            state = block.defaultBlockState();
        } else if (level.getFluidState(clicked).isSource() && level.getFluidState(clicked).is(FluidTags.WATER)) {
            // Water crops need their fluid property; let the crop block perform normal placement first.
            cropPos = clicked;
            final BlockState placed = block.getStateForPlacement(new BlockPlaceContext(context));
            state = placed == null ? block.defaultBlockState() : placed;
        } else {
            return InteractionResult.PASS;
        }

        for (final Property<?> property : state.getProperties()) {
            if (property instanceof IntegerProperty integer && property.getName().equals("age")) {
                state = state.setValue(integer, 0);
                break;
            }
        }
        if (!state.canSurvive(level, cropPos)) {
            return InteractionResult.PASS;
        }
        if (!level.isClientSide()) {
            level.setBlock(cropPos, state, Block.UPDATE_ALL);
            level.playSound(null, cropPos, SoundEvents.CROP_PLANTED, SoundSource.BLOCKS, 1.0F, 1.0F);
            if (context.getPlayer() != null && !context.getPlayer().getAbilities().instabuild) {
                context.getItemInHand().shrink(1);
            }
        }
        return InteractionResult.sidedSuccess(level.isClientSide());
    }
}
