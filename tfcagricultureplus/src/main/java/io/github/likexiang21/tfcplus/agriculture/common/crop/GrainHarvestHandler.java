package io.github.likexiang21.tfcplus.agriculture.common.crop;

import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureItems;
import net.minecraft.core.BlockPos;
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
 * Replaces the harvest drop of mature A/TFC long-stem grain crops:
 * mature crop -> one bundle + one seed; the bundle is threshed later into grain + wet_grass.
 *
 * <p>This is deliberately an event-level replacement, not a resource-only loot-table change:
 * the original block break is cancelled, so the crop's old direct grain/straw drop is not kept.
 * The old behavior remains available through the backup/rollback path of this batch.
 *
 * <p>This handler is intentionally conservative: it only acts on the exact 16 crop block IDs
 * and only at the crop's real maximum age. Immature or unrelated blocks are untouched.
 */
public final class GrainHarvestHandler {

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
        final GrainCrop crop = GrainCrop.fromCropBlockId(blockId.toString());
        if (crop == null) {
            return;
        }

        final int age = readIntProperty(state, "age");
        if (age < 0 || !crop.isMature(age)) {
            return;
        }

        // Double crops: only the bottom half owns the harvest, so breaking the top keeps
        // vanilla/TFC behavior and cannot double-drop.
        final String part = readProperty(state, "part");
        if ("top".equalsIgnoreCase(part)) {
            return;
        }

        event.setCanceled(true);
        final BlockPos pos = event.getPos();

        if ("bottom".equalsIgnoreCase(part)) {
            final BlockPos above = pos.above();
            if ("top".equalsIgnoreCase(readProperty(level.getBlockState(above), "part"))) {
                level.removeBlock(above, false);
            }
        }
        level.removeBlock(pos, false);

        final var bundle = AgricultureItems.GRAIN_BUNDLES.get(crop.id());
        if (bundle != null) {
            Block.popResource(level, pos, new ItemStack(bundle.get(), 1));
        }

        final Item seed = BuiltInRegistries.ITEM.get(ResourceLocation.parse(crop.seedItemId()));
        if (seed != Items.AIR) {
            Block.popResource(level, pos, new ItemStack(seed, 1));
        }
    }

    private static int readIntProperty(BlockState state, String name) {
        for (final Property<?> property : state.getProperties()) {
            if (property.getName().equals(name) && state.getValue(property) instanceof Integer value) {
                return value;
            }
        }
        return -1;
    }

    private static String readProperty(BlockState state, String name) {
        for (final Property<?> property : state.getProperties()) {
            if (property.getName().equals(name)) {
                return String.valueOf(state.getValue(property));
            }
        }
        return "";
    }

    private GrainHarvestHandler() {}
}
