package io.github.likexiang21.tfcplus.agriculture.common.crop;

import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureSpices;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.block.Block;
import net.neoforged.neoforge.event.level.BlockEvent;

/**
 * Low-rate wild spice seed source from vanilla short/tall grass. This gives the 20 B spice
 * crops a non-creative start before dedicated wild spice plants/worldgen are authored.
 *
 * <p>Additive only: the normal grass drop is untouched.
 */
public final class SpiceSeedDropHandler {

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
        final String id = BuiltInRegistries.BLOCK.getKey(event.getState().getBlock()).toString();
        if (!id.equals("minecraft:short_grass") && !id.equals("minecraft:tall_grass")) {
            return;
        }
        if (level.random.nextFloat() >= 0.05F) {
            return;
        }
        final SpiceSpecies[] spices = java.util.Arrays.stream(SpiceSpecies.values())
            .filter(spice -> AgricultureSpices.SEEDS.containsKey(spice.id()))
            .toArray(SpiceSpecies[]::new);
        if (spices.length == 0) {
            return;
        }
        final SpiceSpecies spice = spices[level.random.nextInt(spices.length)];
        final var seed = AgricultureSpices.SEEDS.get(spice.id());
        if (seed != null) {
            Block.popResource(level, event.getPos(), new ItemStack(seed.get(), 1));
        }
    }

    private SpiceSeedDropHandler() {}
}
