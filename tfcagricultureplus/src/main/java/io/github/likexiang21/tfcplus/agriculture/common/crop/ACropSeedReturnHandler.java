package io.github.likexiang21.tfcplus.agriculture.common.crop;

import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.BlockState;
import net.neoforged.neoforge.event.level.BlockEvent;

/**
 * Seed return for A's 87 crop blocks. Grain crops are excluded because GrainHarvestHandler
 * already returns the seed with the bundle. Additive: original A drops stay untouched.
 */
public final class ACropSeedReturnHandler {

    public static void onBlockBreak(BlockEvent.BreakEvent event) {
        if (CreativeGuards.isCreative(event)) {
            return;
        }
        if (event.isCanceled() || !(event.getLevel() instanceof ServerLevel level)) {
            return;
        }
        final BlockState state = event.getState();
        final String blockId = BuiltInRegistries.BLOCK.getKey(state.getBlock()).toString();
        final String aPrefix = "tfcfarmingplus:crop/";
        if (!blockId.startsWith(aPrefix)) {
            return;
        }
        final String crop = blockId.substring(aPrefix.length());
        if (GrainCrop.fromCropBlockId(blockId) != null) {
            return;
        }
        final int[] ageAndMax = ageAndMax(state);
        if (ageAndMax[0] < 0 || ageAndMax[1] < 0 || ageAndMax[0] < ageAndMax[1]) {
            return;
        }
        final Item seed = BuiltInRegistries.ITEM.get(
            ResourceLocation.parse("tfcfarmingplus:seeds/" + crop));
        if (seed != Items.AIR) {
            Block.popResource(level, event.getPos(), new ItemStack(seed, 1));
        }
    }

    private static int[] ageAndMax(BlockState state) {
        int age = -1;
        int max = -1;
        var ageProperty = state.getProperties().stream()
            .filter(p -> p.getName().equals("age"))
            .findFirst().orElse(null);
        if (ageProperty == null) {
            return new int[]{-1, -1};
        }
        if (state.getValue(ageProperty) instanceof Integer value) {
            age = value;
        }
        for (final BlockState possible : state.getBlock().getStateDefinition().getPossibleStates()) {
            if (possible.getValue(ageProperty) instanceof Integer value) {
                max = Math.max(max, value);
            }
        }
        return new int[]{age, max};
    }

    private ACropSeedReturnHandler() {}
}
