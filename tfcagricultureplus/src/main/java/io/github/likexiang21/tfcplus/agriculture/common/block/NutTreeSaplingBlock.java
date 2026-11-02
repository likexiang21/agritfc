package io.github.likexiang21.tfcplus.agriculture.common.block;

import com.mojang.serialization.MapCodec;
import io.github.likexiang21.tfcplus.agriculture.common.crop.NutTreeSpecies;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureBlocks;
import net.minecraft.core.BlockPos;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.tags.BlockTags;
import net.minecraft.util.RandomSource;
import net.minecraft.world.level.BlockGetter;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.LevelReader;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.BushBlock;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.state.StateDefinition;
import net.minecraft.world.level.block.state.properties.IntegerProperty;

/** Small deterministic nut tree grower; uses TFC oak logs as the trunk and B nut leaves. */
public final class NutTreeSaplingBlock extends BushBlock {

    public static final IntegerProperty STAGE = IntegerProperty.create("stage", 0, 2);
    private final NutTreeSpecies species;

    public NutTreeSaplingBlock(NutTreeSpecies species, Properties properties) {
        super(properties);
        this.species = species;
        registerDefaultState(stateDefinition.any().setValue(STAGE, 0));
    }

    @Override
    protected MapCodec<? extends BushBlock> codec() {
        return simpleCodec(properties -> new NutTreeSaplingBlock(species, properties));
    }

    @Override
    protected void createBlockStateDefinition(StateDefinition.Builder<Block, BlockState> builder) {
        builder.add(STAGE);
    }

    @Override
    protected boolean mayPlaceOn(BlockState state, BlockGetter level, BlockPos pos) {
        return state.is(net.minecraft.world.level.block.Blocks.DIRT)
            || state.is(net.minecraft.world.level.block.Blocks.GRASS_BLOCK)
            || state.is(BlockTags.DIRT) || super.mayPlaceOn(state, level, pos);
    }

    @Override
    protected boolean canSurvive(BlockState state, LevelReader level, BlockPos pos) {
        return mayPlaceOn(level.getBlockState(pos.below()), level, pos.below());
    }

    @Override
    public void onPlace(BlockState state, net.minecraft.world.level.Level level, BlockPos pos,
                        BlockState oldState, boolean movedByPiston) {
        super.onPlace(state, level, pos, oldState, movedByPiston);
        if (!level.isClientSide()) {
            level.scheduleTick(pos, this, 20);
        }
    }

    @Override
    public void tick(BlockState state, ServerLevel level, BlockPos pos, RandomSource random) {
        final int stage = state.getValue(STAGE);
        if (stage < 2) {
            level.setBlock(pos, state.setValue(STAGE, stage + 1), Block.UPDATE_CLIENTS);
            level.scheduleTick(pos, this, 20);
            return;
        }
        growTree(level, pos, random);
    }

    @Override
    protected void randomTick(BlockState state, ServerLevel level, BlockPos pos, RandomSource random) {
        final int stage = state.getValue(STAGE);
        if (stage < 2) {
            level.setBlock(pos, state.setValue(STAGE, stage + 1), Block.UPDATE_CLIENTS);
            return;
        }
        growTree(level, pos, random);
    }

    private void growTree(ServerLevel level, BlockPos pos, RandomSource random) {
        final Block log = BuiltInRegistries.BLOCK.get(ResourceLocation.parse("tfc:wood/log/oak"));
        if (log == null || log == net.minecraft.world.level.block.Blocks.AIR) {
            return;
        }
        final Block leaves = AgricultureBlocks.NUT_LEAVES.get(species.id()).get();
        final int height = 4 + random.nextInt(2);
        // Refuse to grow into a blocked column instead of overwriting existing builds.
        for (int y = 0; y < height; y++) {
            final BlockState at = level.getBlockState(pos.above(y));
            if (!at.canBeReplaced() && y > 0) {
                return;
            }
        }
        for (int y = 0; y < height; y++) {
            level.setBlockAndUpdate(pos.above(y), log.defaultBlockState());
        }
        final BlockPos top = pos.above(height - 1);
        for (int dy = -2; dy <= 1; dy++) {
            final int radius = dy == 1 ? 1 : 2;
            for (int dx = -radius; dx <= radius; dx++) {
                for (int dz = -radius; dz <= radius; dz++) {
                    if (dx == 0 && dz == 0 && dy < 1) {
                        continue;
                    }
                    final BlockPos leafPos = top.offset(dx, dy, dz);
                    if (level.isEmptyBlock(leafPos) || level.getBlockState(leafPos).canBeReplaced()) {
                        level.setBlockAndUpdate(leafPos, leaves.defaultBlockState()
                            .setValue(net.minecraft.world.level.block.LeavesBlock.PERSISTENT, false));
                    }
                }
            }
        }
    }
}
