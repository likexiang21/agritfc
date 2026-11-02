package io.github.likexiang21.tfcplus.agriculture.common.crop;

import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureDataComponents;
import net.minecraft.network.chat.Component;
import net.neoforged.neoforge.event.entity.player.ItemTooltipEvent;

/** Shows the DataComponent treatment stage on ordinary seed stacks. */
public final class SeedTreatmentTooltip {

    public static void onItemTooltip(ItemTooltipEvent event) {
        final String stage = event.getItemStack().get(AgricultureDataComponents.SEED_TREATMENT.get());
        if (stage == null || stage.isBlank()) {
            return;
        }
        event.getToolTip().add(Component.translatable(
            "tooltip.tfcagricultureplus.seed_treatment." + stage));
    }

    private SeedTreatmentTooltip() {}
}
