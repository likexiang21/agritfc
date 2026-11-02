package io.github.likexiang21.tfcplus.agriculture.common.block;

import io.github.likexiang21.tfcplus.agriculture.common.crop.NutTreeSpecies;
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
import net.minecraft.world.level.block.state.StateDefinition;
import net.minecraft.world.level.block.state.properties.IntegerProperty;

/** B nut-tree leaves with a season-driven nut_state and a ripe-state nut/shell drop. */
public final class NutLeavesBlock extends LeavesBlock {

    public static final IntegerProperty NUT_STATE = IntegerProperty.create("nut_state", 0, 3);
    private final NutTreeSpecies species;

    public NutLeavesBlock(NutTreeSpecies species, Properties properties) {
        super(properties);
        this.species = species;
        registerDefaultState(stateDefinition.any()
            .setValue(DISTANCE, 7)
            .setValue(PERSISTENT, false)
            .setValue(NUT_STATE, 0));
    }

    @Override
    public MapCodec<? extends LeavesBlock> codec() {
        return simpleCodec(properties -> new NutLeavesBlock(species, properties));
    }

    @Override
    protected void createBlockStateDefinition(StateDefinition.Builder<Block, BlockState> builder) {
        super.createBlockStateDefinition(builder);
        builder.add(NUT_STATE);
    }

    @Override
    protected void randomTick(BlockState state, ServerLevel level, BlockPos pos, RandomSource random) {
        super.randomTick(state, level, pos, random);
        final Season season = Calendars.get(level).getHemispheralCalendarMonthOfYear(false).getSeason();
        final int target = switch (season) {
            case SPRING -> 1;
            case SUMMER -> 2;
            case FALL -> 3;
            case WINTER -> 0;
        };
        if (state.getValue(NUT_STATE) != target) {
            level.setBlock(pos, state.setValue(NUT_STATE, target), Block.UPDATE_CLIENTS | Block.UPDATE_NEIGHBORS);
        }
        if (target == 3 && random.nextFloat() < 0.03F) {
            final Item nut = BuiltInRegistries.ITEM.get(ResourceLocation.parse(species.nutItemId()));
            final Item shell = BuiltInRegistries.ITEM.get(ResourceLocation.parse(species.shellItemId()));
            Block.popResource(level, pos, new ItemStack(nut, 1));
            Block.popResource(level, pos, new ItemStack(shell, 1));
        }
    }
}
