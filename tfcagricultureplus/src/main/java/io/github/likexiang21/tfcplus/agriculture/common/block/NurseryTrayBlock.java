package io.github.likexiang21.tfcplus.agriculture.common.block;

import com.mojang.serialization.MapCodec;
import io.github.likexiang21.tfcplus.agriculture.common.blockentity.NurseryTrayBlockEntity;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureBlockEntities;
import net.minecraft.core.BlockPos;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.ItemInteractionResult;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.BlockGetter;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.EntityBlock;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraft.world.level.block.entity.BlockEntityTicker;
import net.minecraft.world.level.block.entity.BlockEntityType;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.state.StateDefinition;
import net.minecraft.world.level.block.state.properties.IntegerProperty;
import net.minecraft.world.phys.BlockHitResult;
import net.minecraft.world.phys.shapes.CollisionContext;
import net.minecraft.world.phys.shapes.VoxelShape;

/** One-seed nursery tray: empty -> growing -> ready. */
public final class NurseryTrayBlock extends Block implements EntityBlock {

    public static final IntegerProperty STAGE = IntegerProperty.create("stage", 0, 2);
    private static final VoxelShape SHAPE = Block.box(0.0D, 0.0D, 0.0D, 16.0D, 4.0D, 16.0D);

    public NurseryTrayBlock(Properties properties) {
        super(properties);
        registerDefaultState(stateDefinition.any().setValue(STAGE, 0));
    }

    @Override
    protected MapCodec<? extends Block> codec() {
        return simpleCodec(NurseryTrayBlock::new);
    }

    @Override
    protected void createBlockStateDefinition(StateDefinition.Builder<Block, BlockState> builder) {
        builder.add(STAGE);
    }

    @Override
    protected VoxelShape getShape(BlockState state, BlockGetter level, BlockPos pos, CollisionContext context) {
        return SHAPE;
    }

    @Override
    public BlockEntity newBlockEntity(BlockPos pos, BlockState state) {
        return new NurseryTrayBlockEntity(pos, state);
    }

    @Override
    public <T extends BlockEntity> BlockEntityTicker<T> getTicker(Level level, BlockState state, BlockEntityType<T> type) {
        if (level.isClientSide() || type != AgricultureBlockEntities.NURSERY_TRAY.get()) {
            return null;
        }
        return (l, p, s, be) -> NurseryTrayBlockEntity.serverTick(l, p, s, (NurseryTrayBlockEntity) be);
    }

    @Override
    protected ItemInteractionResult useItemOn(ItemStack stack, BlockState state, Level level, BlockPos pos,
                                              Player player, InteractionHand hand, BlockHitResult hit) {
        if (level.isClientSide()) {
            return ItemInteractionResult.sidedSuccess(true);
        }
        if (!(level.getBlockEntity(pos) instanceof NurseryTrayBlockEntity tray)) {
            return ItemInteractionResult.PASS_TO_DEFAULT_BLOCK_INTERACTION;
        }
        if (state.getValue(STAGE) == 0 && tray.canAccept(stack)) {
            tray.insert(stack);
            if (!player.isCreative()) {
                stack.shrink(1);
            }
            level.setBlock(pos, state.setValue(STAGE, 1), 3);
            return ItemInteractionResult.sidedSuccess(false);
        }
        if (state.getValue(STAGE) == 2) {
            final ItemStack seedling = tray.takeSeedling();
            if (!seedling.isEmpty()) {
                if (!player.getInventory().add(seedling)) {
                    player.drop(seedling, false);
                }
                level.setBlock(pos, state.setValue(STAGE, 0), 3);
                return ItemInteractionResult.sidedSuccess(false);
            }
        }
        return ItemInteractionResult.PASS_TO_DEFAULT_BLOCK_INTERACTION;
    }

    @Override
    protected InteractionResult useWithoutItem(BlockState state, Level level, BlockPos pos,
                                               Player player, BlockHitResult hit) {
        if (level.isClientSide()) {
            return InteractionResult.sidedSuccess(true);
        }
        if (state.getValue(STAGE) == 2 && level.getBlockEntity(pos) instanceof NurseryTrayBlockEntity tray) {
            final ItemStack seedling = tray.takeSeedling();
            if (!seedling.isEmpty()) {
                if (!player.getInventory().add(seedling)) {
                    player.drop(seedling, false);
                }
                level.setBlock(pos, state.setValue(STAGE, 0), 3);
                return InteractionResult.sidedSuccess(false);
            }
        }
        return InteractionResult.PASS;
    }

    @Override
    protected void onRemove(BlockState state, Level level, BlockPos pos, BlockState replacement, boolean moving) {
        if (!state.is(replacement.getBlock()) && level.getBlockEntity(pos) instanceof NurseryTrayBlockEntity tray) {
            if (tray.ready()) {
                final ItemStack seedling = tray.takeSeedling();
                if (!seedling.isEmpty()) {
                    net.minecraft.world.Containers.dropItemStack(level, pos.getX() + 0.5,
                        pos.getY() + 0.5, pos.getZ() + 0.5, seedling);
                }
            } else {
                tray.dropSeed();
            }
        }
        super.onRemove(state, level, pos, replacement, moving);
    }
}
