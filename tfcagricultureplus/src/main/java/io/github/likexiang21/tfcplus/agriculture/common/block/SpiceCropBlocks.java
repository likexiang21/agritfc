package io.github.likexiang21.tfcplus.agriculture.common.block;

import com.mojang.serialization.MapCodec;
import net.minecraft.core.BlockPos;
import net.minecraft.core.Direction;
import net.minecraft.world.level.BlockGetter;
import net.minecraft.world.level.LevelReader;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.CropBlock;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.phys.shapes.CollisionContext;
import net.minecraft.world.phys.shapes.VoxelShape;

import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureBlocks;

/**
 * Shape-only spice crop variants. They intentionally reuse vanilla CropBlock growth/render
 * mechanics for the first pass; tree/vine support and support blocks are a later gameplay batch.
 */
public final class SpiceCropBlocks {

    public static final class Herb extends TfcFarmlandCropBlock {
        private static final VoxelShape SHAPE = Block.box(2, 0, 2, 14, 10, 14);
        public Herb(Properties properties) { super(properties); }
        @Override public MapCodec<? extends CropBlock> codec() { return simpleCodec(Herb::new); }
        @Override protected VoxelShape getShape(BlockState state, BlockGetter level, BlockPos pos, CollisionContext context) { return SHAPE; }
    }

    public static final class Shrub extends TfcFarmlandCropBlock {
        private static final VoxelShape SHAPE = Block.box(1, 0, 1, 15, 12, 15);
        public Shrub(Properties properties) { super(properties); }
        @Override public MapCodec<? extends CropBlock> codec() { return simpleCodec(Shrub::new); }
        @Override protected VoxelShape getShape(BlockState state, BlockGetter level, BlockPos pos, CollisionContext context) { return SHAPE; }
    }

    public static final class Tree extends TfcFarmlandCropBlock {
        private static final VoxelShape SHAPE = Block.box(3, 0, 3, 13, 16, 13);
        public Tree(Properties properties) { super(properties); }
        @Override public MapCodec<? extends CropBlock> codec() { return simpleCodec(Tree::new); }
        @Override protected VoxelShape getShape(BlockState state, BlockGetter level, BlockPos pos, CollisionContext context) { return SHAPE; }
    }

    public static final class Vine extends TfcFarmlandCropBlock {
        private static final VoxelShape SHAPE = Block.box(5, 0, 5, 11, 16, 11);
        public Vine(Properties properties) { super(properties); }
        @Override public MapCodec<? extends CropBlock> codec() { return simpleCodec(Vine::new); }
        @Override protected VoxelShape getShape(BlockState state, BlockGetter level, BlockPos pos, CollisionContext context) { return SHAPE; }
        @Override protected boolean canSurvive(BlockState state, LevelReader level, BlockPos pos) {
            if (!super.canSurvive(state, level, pos)) {
                return false;
            }
            for (final Direction direction : Direction.Plane.HORIZONTAL) {
                if (level.getBlockState(pos.relative(direction)).is(AgricultureBlocks.SPICE_TRELLIS.get())) {
                    return true;
                }
            }
            return false;
        }
    }

    public static final class Root extends TfcFarmlandCropBlock {
        private static final VoxelShape SHAPE = Block.box(3, 0, 3, 13, 8, 13);
        public Root(Properties properties) { super(properties); }
        @Override public MapCodec<? extends CropBlock> codec() { return simpleCodec(Root::new); }
        @Override protected VoxelShape getShape(BlockState state, BlockGetter level, BlockPos pos, CollisionContext context) { return SHAPE; }
    }

    public static final class Corm extends TfcFarmlandCropBlock {
        private static final VoxelShape SHAPE = Block.box(4, 0, 4, 12, 8, 12);
        public Corm(Properties properties) { super(properties); }
        @Override public MapCodec<? extends CropBlock> codec() { return simpleCodec(Corm::new); }
        @Override protected VoxelShape getShape(BlockState state, BlockGetter level, BlockPos pos, CollisionContext context) { return SHAPE; }
    }

    private SpiceCropBlocks() {}
}
