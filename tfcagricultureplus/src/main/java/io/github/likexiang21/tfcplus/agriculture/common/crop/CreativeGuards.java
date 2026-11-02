package io.github.likexiang21.tfcplus.agriculture.common.crop;

import net.neoforged.neoforge.event.entity.player.PlayerInteractEvent;
import net.neoforged.neoforge.event.level.BlockEvent;

/** Shared creative-mode guards so event-based crop byproducts do not drop in creative. */
public final class CreativeGuards {

    public static boolean isCreative(BlockEvent.BreakEvent event) {
        return event.getPlayer() != null && event.getPlayer().isCreative();
    }

    public static boolean isCreative(PlayerInteractEvent event) {
        return event.getEntity() != null && event.getEntity().isCreative();
    }

    private CreativeGuards() {}
}
