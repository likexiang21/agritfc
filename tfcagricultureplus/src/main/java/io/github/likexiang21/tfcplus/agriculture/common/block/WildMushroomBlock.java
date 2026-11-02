package io.github.likexiang21.tfcplus.agriculture.common.block;

import com.mojang.serialization.MapCodec;
import net.minecraft.core.BlockPos;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.tags.BlockTags;
import net.minecraft.tags.TagKey;
import net.minecraft.util.RandomSource;
import net.minecraft.world.level.BlockGetter;
import net.minecraft.world.level.LevelReader;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.BushBlock;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.state.StateDefinition;
import net.minecraft.world.level.block.state.properties.BlockStateProperties;
import net.minecraft.world.level.block.state.properties.IntegerProperty;
import net.minecraft.world.phys.shapes.CollisionContext;
import net.minecraft.world.phys.shapes.VoxelShape;

/**
 * Wild mushroom block.
 *
 * <p>Named after the TFC wild-plant behavior rather than a generic decorative flower:
 * <ul>
 *   <li>three visible growth ages;</li>
 *   <li>random-tick growth and local spread to compatible soil;</li>
 *   <li>no block entity and no cultivation bag here.</li>
 * </ul>
 * The four {@code naturalOnly} species use this same wild block; the future bag system must
 * deliberately exclude them (see MushroomSpecies).
 */
public class WildMushroomBlock extends BushBlock {

    public static final IntegerProperty AGE = BlockStateProperties.AGE_2;
    private static final VoxelShape SHAPE = Block.box(4.0D, 0.0D, 4.0D, 12.0D, 8.0D, 12.0D);
    private static final TagKey<Block> TFC_DIRT =
        BlockTags.create(ResourceLocation.fromNamespaceAndPath("tfc", "dirt"));
    private static final TagKey<Block> TFC_GRASS =
        BlockTags.create(ResourceLocation.fromNamespaceAndPath("tfc", "grass"));

    public WildMushroomBlock(Properties properties) {
        super(properties);
        registerDefaultState(stateDefinition.any().setValue(AGE, 0));
    }

    @Override
    protected MapCodec<? extends BushBlock> codec() {
        return simpleCodec(WildMushroomBlock::new);
    }

    @Override
    protected void createBlockStateDefinition(StateDefinition.Builder<Block, BlockState> builder) {
        builder.add(AGE);
    }

    @Override
    protected VoxelShape getShape(BlockState state, BlockGetter level, BlockPos pos, CollisionContext context) {
        return SHAPE;
    }

    @Override
    protected boolean mayPlaceOn(BlockState state, BlockGetter level, BlockPos pos) {
        return state.is(BlockTags.DIRT)
            || state.is(TFC_DIRT)
            || state.is(TFC_GRASS)
            || state.is(Blocks.GRASS_BLOCK)
            || state.is(Blocks.MOSS_BLOCK)
            || state.is(Blocks.PODZOL)
            || state.is(Blocks.MYCELIUM);
    }

    @Override
    public boolean isRandomlyTicking(BlockState state) {
        return true;
    }

    @Override
    protected void randomTick(BlockState state, ServerLevel level, BlockPos pos, RandomSource random) {
        final int age = state.getValue(AGE);
        if (age < 2) {
            if (random.nextFloat() < 0.18F) {
                level.setBlock(pos, state.setValue(AGE, age + 1), 2);
            }
            return;
        }

        // A mature colony occasionally spreads one young mushroom to nearby compatible soil.
        if (random.nextFloat() < 0.12F) {
            final int dx = random.nextInt(3) - 1;
            final int dz = random.nextInt(3) - 1;
            if (dx == 0 && dz == 0) {
                return;
            }
            final BlockPos target = pos.offset(dx, 0, dz);
            if (level.isEmptyBlock(target) && canSurvive(state.setValue(AGE, 0), level, target)) {
                level.setBlock(target, state.setValue(AGE, 0), 2);
            }
        }
    }

    @Override
    protected boolean canSurvive(BlockState state, LevelReader level, BlockPos pos) {
        return mayPlaceOn(level.getBlockState(pos.below()), level, pos.below());
    }
}
