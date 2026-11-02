package io.github.likexiang21.tfcplus.agriculture.mixin;

import io.github.likexiang21.tfcplus.agriculture.common.crop.NutBearingTree;
import net.dries007.tfc.common.blocks.wood.TFCLeavesBlock;
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
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.state.StateDefinition;
import net.minecraft.world.level.block.state.properties.IntegerProperty;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Unique;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/**
 * Adds a season-driven nut state to existing TFC leaves.
 *
 * <p>State values: 0 none, 1 flower, 2 green, 3 ripe. Spring -> 1, summer -> 2, autumn -> 3,
 * winter -> 0. Ripe leaves randomly drop their mapped nut. The blockstate JSONs are expanded by
 * the B resource generator for every TFC leaf wood, so every state has a model variant.
 */
@Mixin(value = TFCLeavesBlock.class, remap = false)
public abstract class TFCLeavesNutStateMixin {

    @Unique
    private static final IntegerProperty TFCAP_NUT_STATE = IntegerProperty.create("nut_state", 0, 3);

    @Inject(method = "createBlockStateDefinition", at = @At("TAIL"))
    private void tfcap$addNutState(StateDefinition.Builder<Block, BlockState> builder, CallbackInfo ci) {
        builder.add(TFCAP_NUT_STATE);
    }

    @Inject(method = "randomTick", at = @At("HEAD"))
    private void tfcap$seasonalNutTick(BlockState state, ServerLevel level, BlockPos pos,
                                       RandomSource random, CallbackInfo ci) {
        final ResourceLocation leafId = BuiltInRegistries.BLOCK.getKey(state.getBlock());
        final NutBearingTree tree = NutBearingTree.fromLeafBlockId(leafId.toString());
        if (tree == null) {
            return;
        }

        final Season season = Calendars.get(level).getHemispheralCalendarMonthOfYear(false).getSeason();
        final int target = switch (season) {
            case SPRING -> 1;
            case SUMMER -> 2;
            case FALL -> 3;
            case WINTER -> 0;
        };
        final int current = state.getValue(TFCAP_NUT_STATE);
        if (current != target) {
            level.setBlock(pos, state.setValue(TFCAP_NUT_STATE, target),
                Block.UPDATE_CLIENTS | Block.UPDATE_NEIGHBORS);
        }

        if (target == 3 && random.nextFloat() < 0.03F) {
            final Item nut = BuiltInRegistries.ITEM.get(ResourceLocation.parse(tree.nutItemId()));
            if (nut != net.minecraft.world.item.Items.AIR) {
                Block.popResource(level, pos, new ItemStack(nut, 1));
            }
            final Item shell = BuiltInRegistries.ITEM.get(ResourceLocation.parse(tree.shellItemId()));
            if (shell != net.minecraft.world.item.Items.AIR) {
                Block.popResource(level, pos, new ItemStack(shell, 1));
            }
        }
    }
}
