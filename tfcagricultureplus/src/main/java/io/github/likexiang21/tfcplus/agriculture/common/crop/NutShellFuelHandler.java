package io.github.likexiang21.tfcplus.agriculture.common.crop;

import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureItems;
import net.neoforged.neoforge.event.furnace.FurnaceFuelBurnTimeEvent;

/** Gives nut shells a real furnace use without adding a new fuel item or block. */
public final class NutShellFuelHandler {

    public static void onFuelBurnTime(FurnaceFuelBurnTimeEvent event) {
        for (final var shell : AgricultureItems.NUT_SHELLS.values()) {
            if (event.getItemStack().is(shell.get())) {
                event.setBurnTime(200);
                return;
            }
        }
        for (final var waste : AgricultureItems.CROP_WASTE.values()) {
            if (event.getItemStack().is(waste.get())) {
                event.setBurnTime(100);
                return;
            }
        }
    }

    private NutShellFuelHandler() {}
}
