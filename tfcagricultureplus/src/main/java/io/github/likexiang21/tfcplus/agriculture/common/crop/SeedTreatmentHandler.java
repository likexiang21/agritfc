package io.github.likexiang21.tfcplus.agriculture.common.crop;

import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureDataComponents;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureItems;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.neoforged.neoforge.event.entity.player.PlayerInteractEvent;

/**
 * Seed treatment: wet grass/compost advance one stage; wood ash/lime jump to dressed.
 *
 * <p>Items are resolved at use time because this class is loaded during mod construction,
 * before the item registry has been populated.
 */
public final class SeedTreatmentHandler {

    public static void onRightClickItem(PlayerInteractEvent.RightClickItem event) {
        if (event.isCanceled()) {
            return;
        }
        if (event.getLevel().isClientSide()) {
            return;
        }
        final ItemStack stack = event.getItemStack();
        final String id = BuiltInRegistries.ITEM.getKey(stack.getItem()).toString();
        if (!SeedTreatments.isSeedItemId(id)) {
            return;
        }
        final var player = event.getEntity();
        final ItemStack offhand = player.getOffhandItem();
        final Item compost = BuiltInRegistries.ITEM.get(
            ResourceLocation.fromNamespaceAndPath("tfc", "compost"));
        final Item woodAsh = BuiltInRegistries.ITEM.get(
            ResourceLocation.fromNamespaceAndPath("tfc", "powder/wood_ash"));
        final Item lime = BuiltInRegistries.ITEM.get(
            ResourceLocation.fromNamespaceAndPath("tfc", "powder/lime"));
        final String current = stack.getOrDefault(AgricultureDataComponents.SEED_TREATMENT.get(), "");
        final String next;
        if (offhand.is(AgricultureItems.WET_GRASS.get()) || offhand.is(compost)) {
            next = SeedTreatments.next(current);
        } else if (offhand.is(woodAsh) || offhand.is(lime)) {
            next = SeedTreatments.DRESSED;
        } else {
            return;
        }
        if (next.equals(current)) {
            return;
        }
        stack.set(AgricultureDataComponents.SEED_TREATMENT.get(), next);
        if (!player.isCreative()) {
            offhand.shrink(1);
        }
        player.swing(event.getHand(), true);
    }

    private SeedTreatmentHandler() {}
}
