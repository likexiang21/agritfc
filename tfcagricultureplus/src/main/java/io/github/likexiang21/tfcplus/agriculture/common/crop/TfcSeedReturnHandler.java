package io.github.likexiang21.tfcplus.agriculture.common.crop;

import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.state.properties.Property;
import net.neoforged.neoforge.event.level.BlockEvent;

/**
 * Guarantees one seed back from a mature TFC crop, except for the six grain crops already
 * handled by GrainHarvestHandler. This is additive: original TFC drops are not cancelled.
 */
public final class TfcSeedReturnHandler {

    public static void onBlockBreak(BlockEvent.BreakEvent event) {
        if (CreativeGuards.isCreative(event)) {
            return;
        }
        if (event.isCanceled() || !(event.getLevel() instanceof ServerLevel level)) {
            return;
        }
        final BlockState state = event.getState();
        final String blockId = BuiltInRegistries.BLOCK.getKey(state.getBlock()).toString();
        final TfcCropSpecies crop = TfcCropSpecies.fromBlockId(blockId);
        if (crop == null || crop.alreadyHandledByGrainBundle()) {
            return;
        }
        if ("top".equalsIgnoreCase(readProperty(state, "part"))) {
            return;
        }
        final int[] ageAndMax = ageAndMax(state);
        if (ageAndMax[0] < 0 || ageAndMax[1] < 0 || ageAndMax[0] < ageAndMax[1]) {
            return;
        }
        final Item seed = BuiltInRegistries.ITEM.get(ResourceLocation.parse(crop.seedItemId()));
        if (seed != Items.AIR) {
            Block.popResource(level, event.getPos(), new ItemStack(seed, 1));
        }
    }

    private static int[] ageAndMax(BlockState state) {
        int age = -1;
        int max = -1;
        Property<?> ageProperty = null;
        for (final Property<?> property : state.getProperties()) {
            if (property.getName().equals("age")) {
                ageProperty = property;
                if (state.getValue(property) instanceof Integer value) {
                    age = value;
                }
                break;
            }
        }
        if (ageProperty != null) {
            for (final BlockState possible : state.getBlock().getStateDefinition().getPossibleStates()) {
                if (possible.getValue(ageProperty) instanceof Integer value) {
                    max = Math.max(max, value);
                }
            }
        }
        return new int[]{age, max};
    }

    private static String readProperty(BlockState state, String name) {
        for (final Property<?> property : state.getProperties()) {
            if (property.getName().equals(name)) {
                return String.valueOf(state.getValue(property));
            }
        }
        return "";
    }

    private TfcSeedReturnHandler() {}
}
