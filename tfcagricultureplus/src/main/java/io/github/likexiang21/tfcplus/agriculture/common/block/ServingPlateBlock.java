package io.github.likexiang21.tfcplus.agriculture.common.block;

import io.github.likexiang21.tfcplus.agriculture.common.blockentity.ServingPlateBlockEntity;
import io.github.likexiang21.tfcplus.agriculture.common.pan.DishEating;
import io.github.likexiang21.tfcplus.agriculture.common.pan.PlateVariant;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgriculturePlates;
import java.util.List;
import net.minecraft.core.BlockPos;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.BlockGetter;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.BaseEntityBlock;
import net.minecraft.world.level.block.RenderShape;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.state.StateDefinition;
import net.minecraft.world.level.storage.loot.LootParams;
import net.minecraft.world.phys.BlockHitResult;
import net.minecraft.world.phys.shapes.CollisionContext;
import net.minecraft.world.phys.shapes.Shapes;
import net.minecraft.world.phys.shapes.VoxelShape;

/** A plate block; the full plate ItemStack (including dish components) lives in its BE. */
public final class ServingPlateBlock extends BaseEntityBlock {
    public ServingPlateBlock(Properties properties) {
        super(properties);
        registerDefaultState(stateDefinition.any().setValue(AgriculturePlates.VARIANT, PlateVariant.WOOD));
    }

    @Override protected com.mojang.serialization.MapCodec<? extends net.minecraft.world.level.block.BaseEntityBlock> codec() {
        return simpleCodec(ServingPlateBlock::new);
    }

    @Override protected void createBlockStateDefinition(StateDefinition.Builder<net.minecraft.world.level.block.Block, BlockState> builder) {
        builder.add(AgriculturePlates.VARIANT);
    }

    @Override public BlockEntity newBlockEntity(BlockPos pos, BlockState state) {
        return new ServingPlateBlockEntity(pos, state);
    }

    @Override public RenderShape getRenderShape(BlockState state) { return RenderShape.MODEL; }

    private static final VoxelShape SHAPE = Shapes.box(0.0625D, 0.0D, 0.0625D, 0.9375D, 0.0625D, 0.9375D);

    @Override
    protected VoxelShape getShape(BlockState state, BlockGetter level, BlockPos pos, CollisionContext context) {
        return SHAPE;
    }

    @Override public void setPlacedBy(Level level, BlockPos pos, BlockState state, LivingEntity placer, ItemStack stack) {
        super.setPlacedBy(level, pos, state, placer, stack);
        if (!level.isClientSide() && level.getBlockEntity(pos) instanceof ServingPlateBlockEntity plate) {
            plate.setPlateStack(stack);
        }
    }

    @Override protected InteractionResult useWithoutItem(BlockState state, Level level, BlockPos pos,
                                                        Player player, BlockHitResult hit) {
        if (level.isClientSide()) return InteractionResult.SUCCESS;
        if (level.getBlockEntity(pos) instanceof ServingPlateBlockEntity plate) {
            return DishEating.eatFromPlateBlock(player, plate)
                ? InteractionResult.CONSUME
                : InteractionResult.PASS;
        }
        return InteractionResult.PASS;
    }

    @Override public List<ItemStack> getDrops(BlockState state, LootParams.Builder params) {
        // Use the loot-context BlockEntity, not a fresh level lookup: vanilla removes the block
        // before playerDestroy/getDrops, but the captured BE is still available in the context.
        final BlockEntity be = params.getOptionalParameter(
            net.minecraft.world.level.storage.loot.parameters.LootContextParams.BLOCK_ENTITY);
        if (be instanceof ServingPlateBlockEntity plate) {
            return List.of(plate.dropStack());
        }
        return List.of(new ItemStack(AgriculturePlates.itemFor(state.getValue(AgriculturePlates.VARIANT)).get()));
    }

    @Override public ItemStack getCloneItemStack(net.minecraft.world.level.LevelReader level, BlockPos pos, BlockState state) {
        if (level.getBlockEntity(pos) instanceof ServingPlateBlockEntity plate) {
            return plate.dropStack();
        }
        return new ItemStack(AgriculturePlates.itemFor(state.getValue(AgriculturePlates.VARIANT)).get());
    }
}
