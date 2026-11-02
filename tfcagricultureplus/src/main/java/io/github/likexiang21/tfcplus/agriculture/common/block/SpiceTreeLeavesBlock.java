package io.github.likexiang21.tfcplus.agriculture.common.block;

import io.github.likexiang21.tfcplus.agriculture.common.crop.SpiceTreeSpecies;
import com.mojang.serialization.MapCodec;
import net.dries007.tfc.util.calendar.Calendars;
import net.dries007.tfc.util.calendar.Season;
import net.minecraft.core.BlockPos;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.util.RandomSource;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.LeavesBlock;
import net.minecraft.world.level.block.state.BlockState;

/** B spice-tree leaves: autumn drops one spice product; no nut_state property. */
public final class SpiceTreeLeavesBlock extends LeavesBlock {

    private final SpiceTreeSpecies species;

    public SpiceTreeLeavesBlock(SpiceTreeSpecies species, Properties properties) {
        super(properties);
        this.species = species;
        registerDefaultState(stateDefinition.any().setValue(DISTANCE, 7).setValue(PERSISTENT, false));
    }

    @Override
    public MapCodec<? extends LeavesBlock> codec() {
        return simpleCodec(properties -> new SpiceTreeLeavesBlock(species, properties));
    }

    @Override
    protected void randomTick(BlockState state, ServerLevel level, BlockPos pos, RandomSource random) {
        super.randomTick(state, level, pos, random);
        final Season season = Calendars.get(level).getHemispheralCalendarMonthOfYear(false).getSeason();
        if (season == Season.FALL && random.nextFloat() < 0.03F) {
            final Item product = BuiltInRegistries.ITEM.get(ResourceLocation.parse(species.productItemId()));
            Block.popResource(level, pos, new ItemStack(product, 1));
        }
    }
}
