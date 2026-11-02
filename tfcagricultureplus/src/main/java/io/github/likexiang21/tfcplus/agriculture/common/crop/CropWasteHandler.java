package io.github.likexiang21.tfcplus.agriculture.common.crop;

import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureItems;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureSpices;
import java.util.HashMap;
import java.util.Map;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.state.properties.Property;
import net.neoforged.neoforge.event.level.BlockEvent;

/**
 * Adds the real crop-specific green waste byproduct at mature harvest.
 *
 * <p>Unlike {@link GrainHarvestHandler}, this does not cancel the block break: the crop's
 * original main product remains untouched and one {@code crop_waste/<crop>} item is added.
 * Only crops in {@link CropWasteCrops} are affected; grain/oil/fiber/nut crops are absent.
 */
public final class CropWasteHandler {

    private static final Map<Block, Integer> MAX_AGE_CACHE = new HashMap<>();

    public static void onBlockBreak(BlockEvent.BreakEvent event) {
        if (event.isCanceled()) {
            return;
        }
        if (CreativeGuards.isCreative(event)) {
            return;
        }
        if (!(event.getLevel() instanceof ServerLevel level)) {
            return;
        }
        final BlockState state = event.getState();
        final ResourceLocation blockId = BuiltInRegistries.BLOCK.getKey(state.getBlock());
        final String crop = CropWasteCrops.cropFromBlockId(blockId.toString());
        if (crop == null) {
            handleSpiceCrop(level, event, state, blockId.toString());
            return;
        }
        if (blockId.toString().contains(":wild_crop/")) {
            // TFC/A wild crops expose a boolean mature property, not an integer age.
            if (readBoolean(state, "mature") != Boolean.TRUE) {
                return;
            }
            final var wildWaste = AgricultureItems.CROP_WASTE.get(crop);
            if (wildWaste != null) {
                Block.popResource(level, event.getPos(), new ItemStack(wildWaste.get(), 1));
            }
            return;
        }

        final int age = readAge(state);
        final int maxAge = maxAge(state);
        if (age < 0 || maxAge < 0 || age < maxAge) {
            return;
        }
        if ("top".equalsIgnoreCase(readProperty(state, "part"))) {
            return;
        }

        final var waste = AgricultureItems.CROP_WASTE.get(crop);
        if (waste != null) {
            Block.popResource(level, event.getPos(), new ItemStack(waste.get(), 1));
        }
    }

    private static Boolean readBoolean(BlockState state, String name) {
        for (final Property<?> property : state.getProperties()) {
            if (property.getName().equals(name) && state.getValue(property) instanceof Boolean value) {
                return value;
            }
        }
        return null;
    }

    private static int readAge(BlockState state) {
        for (final Property<?> property : state.getProperties()) {
            if (property.getName().equals("age") && state.getValue(property) instanceof Integer value) {
                return value;
            }
        }
        return -1;
    }

    private static void handleSpiceCrop(ServerLevel level, BlockEvent.BreakEvent event,
                                        BlockState state, String blockId) {
        final String spiceId = AgricultureSpices.spiceIdFromCropBlockId(blockId);
        if (spiceId == null || !AgricultureSpices.WASTES.containsKey(spiceId)) {
            return;
        }
        final int age = readAge(state);
        final int maxAge = maxAge(state);
        if (age < 0 || maxAge < 0 || age < maxAge) {
            return;
        }
        Block.popResource(level, event.getPos(), new ItemStack(AgricultureSpices.WASTES.get(spiceId).get(), 1));
    }

    private static int maxAge(BlockState state) {
        return MAX_AGE_CACHE.computeIfAbsent(state.getBlock(), block -> {
            final BlockState definition = block.defaultBlockState();
            for (final Property<?> property : definition.getProperties()) {
                if (!property.getName().equals("age")) {
                    continue;
                }
                int max = -1;
                for (final BlockState possible : block.getStateDefinition().getPossibleStates()) {
                    if (possible.getValue(property) instanceof Integer value) {
                        max = Math.max(max, value);
                    }
                }
                return max;
            }
            return -1;
        });
    }

    private static String readProperty(BlockState state, String name) {
        for (final Property<?> property : state.getProperties()) {
            if (property.getName().equals(name)) {
                return String.valueOf(state.getValue(property));
            }
        }
        return "";
    }

    private CropWasteHandler() {}
}
