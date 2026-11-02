package io.github.likexiang21.tfcplus.agriculture.common.block;

import com.mojang.serialization.MapCodec;
import io.github.likexiang21.tfcplus.agriculture.common.blockentity.MushroomBagBlockEntity;
import io.github.likexiang21.tfcplus.agriculture.common.crop.MushroomSpecies;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureBlockEntities;
import net.minecraft.core.BlockPos;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.network.chat.Component;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.ItemInteractionResult;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.BlockItem;
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
import net.minecraft.world.level.storage.loot.LootParams;
import net.minecraft.world.level.storage.loot.parameters.LootContextParams;
import net.minecraft.world.phys.BlockHitResult;
import net.minecraft.world.phys.shapes.CollisionContext;
import net.minecraft.world.phys.shapes.VoxelShape;
import java.util.List;

/**
 * Four-stage cultivation bag: empty -> colonising -> fruiting -> spent.
 *
 * <p>It accepts only wild mushroom block items of the 11 cultivable species. The four
 * natural-only species are rejected here; there is no alternative bag recipe for them.
 * Species and progress live in {@link MushroomBagBlockEntity}; the blockstate only carries
 * the display stage so the block needs no BER.
 */
public final class MushroomBagBlock extends Block implements EntityBlock {

    public static final IntegerProperty STAGE = IntegerProperty.create("stage", 0, 3);
    private static final VoxelShape SHAPE = Block.box(1.0D, 0.0D, 1.0D, 15.0D, 10.0D, 15.0D);

    public MushroomBagBlock(Properties properties) {
        super(properties);
        registerDefaultState(stateDefinition.any().setValue(STAGE, 0));
    }

    @Override
    protected MapCodec<? extends Block> codec() {
        return simpleCodec(MushroomBagBlock::new);
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
        return new MushroomBagBlockEntity(pos, state);
    }

    @Override
    public List<ItemStack> getDrops(BlockState state, LootParams.Builder params) {
        final BlockEntity be = params.getOptionalParameter(LootContextParams.BLOCK_ENTITY);
        final ItemStack dropped = new ItemStack(state.getBlock().asItem());
        if (be instanceof MushroomBagBlockEntity bag) {
            final net.minecraft.nbt.CompoundTag tag = new net.minecraft.nbt.CompoundTag();
            bag.saveToItem(tag);
            BlockItem.setBlockEntityData(dropped, AgricultureBlockEntities.MUSHROOM_BAG.get(), tag);
        }
        return List.of(dropped);
    }

    @Override
    public <T extends BlockEntity> BlockEntityTicker<T> getTicker(Level level, BlockState state, BlockEntityType<T> type) {
        if (level.isClientSide() || type != AgricultureBlockEntities.MUSHROOM_BAG.get()) {
            return null;
        }
        return (l, p, s, be) -> MushroomBagBlockEntity.serverTick(
            l, p, s, (MushroomBagBlockEntity) be);
    }

    @Override
    protected ItemInteractionResult useItemOn(ItemStack stack, BlockState state, Level level, BlockPos pos,
                                              Player player, InteractionHand hand, BlockHitResult hit) {
        if (level.isClientSide()) {
            return ItemInteractionResult.sidedSuccess(true);
        }
        final BlockState current = level.getBlockState(pos);
        final int stage = current.getValue(STAGE);
        if ((stage == 0 || stage == 3) && stack.getItem() instanceof BlockItem blockItem) {
            final MushroomSpecies species = MushroomSpecies.fromBlockId(
                BuiltInRegistries.BLOCK.getKey(blockItem.getBlock()).toString());
            if (species == null || species.naturalOnly()) {
                return ItemInteractionResult.FAIL;
            }
            if (stage == 3 && level.getBlockEntity(pos) instanceof MushroomBagBlockEntity spentBag && spentBag.maxed()) {
                return ItemInteractionResult.FAIL;
            }
            if (level.getBlockEntity(pos) instanceof MushroomBagBlockEntity bag) {
                bag.inoculate(species);
                if (!player.isCreative()) {
                    stack.shrink(1);
                }
                setStage(level, pos, current, 1);
                return ItemInteractionResult.sidedSuccess(false);
            }
        }
        if (stage == 2) {
            harvest(level, pos, current);
            return ItemInteractionResult.sidedSuccess(false);
        }
        return ItemInteractionResult.PASS_TO_DEFAULT_BLOCK_INTERACTION;
    }

    @Override
    protected InteractionResult useWithoutItem(BlockState state, Level level, BlockPos pos,
                                               Player player, BlockHitResult hit) {
        if (level.isClientSide()) {
            return InteractionResult.sidedSuccess(true);
        }
        if (state.getValue(STAGE) == 2) {
            harvest(level, pos, state);
            return InteractionResult.sidedSuccess(false);
        }
        if (state.getValue(STAGE) == 1 && level.getBlockEntity(pos) instanceof MushroomBagBlockEntity bag) {
            final MushroomSpecies species = bag.species();
            if (species != null) {
                // Growing state is visible on the block; do not open a text popup.
                return InteractionResult.sidedSuccess(false);
            }
        }
        return InteractionResult.PASS;
    }

    private static void harvest(Level level, BlockPos pos, BlockState state) {
        if (!(level.getBlockEntity(pos) instanceof MushroomBagBlockEntity bag)) {
            return;
        }
        final MushroomSpecies species = bag.species();
        if (species == null) {
            return;
        }
        final Block wildBlock = BuiltInRegistries.BLOCK.get(
            net.minecraft.resources.ResourceLocation.parse(species.blockId()));
        if (wildBlock != net.minecraft.world.level.block.Blocks.AIR) {
            final int min = species.bagMinYield();
            final int max = Math.max(min, species.bagMaxYield());
            Block.popResource(level, pos, new ItemStack(wildBlock.asItem(), min + level.random.nextInt(max - min + 1)));
        }
        bag.markSpent();
        setStage(level, pos, state, 3);
    }

    private static void setStage(Level level, BlockPos pos, BlockState state, int stage) {
        level.setBlock(pos, state.setValue(STAGE, stage), Block.UPDATE_CLIENTS | Block.UPDATE_NEIGHBORS);
    }
}
