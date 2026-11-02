package io.github.likexiang21.tfcplus.agriculture.common.block;

import com.mojang.serialization.MapCodec;
import net.dries007.tfc.common.TFCTags;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.BlockGetter;
import net.minecraft.world.level.block.CropBlock;
import net.minecraft.world.level.block.FarmBlock;
import net.minecraft.world.level.block.state.BlockState;

/**
 * Vanilla-growth crop that can also survive on TFC farmland.
 *
 * <p>TFC's farmland blocks are not vanilla {@link FarmBlock} instances; they are identified by
 * {@link TFCTags.Blocks#FARMLANDS}. Without this override, B's vanilla {@link CropBlock} spice and
 * strawberry blocks pass on {@code minecraft:farmland} but always fail {@code canSurvive} on
 * normal TFC worlds.
 */
public class TfcFarmlandCropBlock extends CropBlock {

    public TfcFarmlandCropBlock(Properties properties) {
        super(properties);
    }

    @Override
    protected boolean mayPlaceOn(BlockState state, BlockGetter level, BlockPos pos) {
        return state.getBlock() instanceof FarmBlock || state.is(TFCTags.Blocks.FARMLANDS);
    }

    @Override
    public MapCodec<? extends CropBlock> codec() {
        return simpleCodec(TfcFarmlandCropBlock::new);
    }
}
