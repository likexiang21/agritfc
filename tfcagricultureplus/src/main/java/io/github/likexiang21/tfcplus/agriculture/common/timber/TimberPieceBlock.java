package io.github.likexiang21.tfcplus.agriculture.common.timber;

import com.mojang.serialization.MapCodec;
import net.minecraft.core.BlockPos;
import net.minecraft.core.Direction;
import net.minecraft.world.level.*;
import net.minecraft.world.level.block.*;
import net.minecraft.world.level.block.state.*;
import net.minecraft.world.phys.shapes.*;

/** Non-directional timber piece (debarked log). Geometry aligned with TFC Woodworking. */
public final class TimberPieceBlock extends Block {
    public final int pieceKind;

    public TimberPieceBlock(Properties properties, int pieceKind) {
        super(properties);
        this.pieceKind = pieceKind;
    }

    @Override protected MapCodec<? extends Block> codec() { return simpleCodec(p -> new TimberPieceBlock(p, pieceKind)); }

    @Override protected VoxelShape getShape(BlockState state, BlockGetter level, BlockPos pos, CollisionContext context) {
        return Block.box(1, 0, 1, 15, 16, 15);
    }

    static boolean isTimberPiece(Block block) {
        return block instanceof TimberPieceBlock || block instanceof DirectionalTimberPieceBlock;
    }

    @Override protected boolean canSurvive(BlockState state, LevelReader level, BlockPos pos) {
        return isTimberPiece(level.getBlockState(pos.below()).getBlock())
            || Block.canSupportCenter(level, pos.below(), Direction.UP);
    }

    @Override protected BlockState updateShape(BlockState state, Direction direction, BlockState neighbor, LevelAccessor level, BlockPos pos, BlockPos neighborPos) {
        return direction == Direction.DOWN && !canSurvive(state, level, pos) ? Blocks.AIR.defaultBlockState() : state;
    }
}
