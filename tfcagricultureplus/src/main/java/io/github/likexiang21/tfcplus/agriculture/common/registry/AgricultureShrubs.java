package io.github.likexiang21.tfcplus.agriculture.common.registry;

import io.github.likexiang21.tfcplus.agriculture.TFCAgriculturePlus;
import io.github.likexiang21.tfcplus.agriculture.common.crop.BushSpecies;
import java.util.LinkedHashMap;
import java.util.Map;
import net.minecraft.world.item.Item;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.neoforge.registries.DeferredHolder;
import net.neoforged.neoforge.registries.DeferredRegister;

/** P0-J: per-TFC-bush harvest residue for the 10 remaining TFC berry bushes. */
public final class AgricultureShrubs {

    public static final DeferredRegister.Items ITEMS =
        DeferredRegister.createItems(TFCAgriculturePlus.MOD_ID);
    public static final Map<String, DeferredHolder<Item, Item>> BUSH_WASTE = new LinkedHashMap<>();

    static {
        for (final BushSpecies bush : BushSpecies.values()) {
            BUSH_WASTE.put(bush.id(), ITEMS.registerSimpleItem(bush.wastePath(), new Item.Properties()));
        }
    }

    public static void register(IEventBus bus) {
        ITEMS.register(bus);
    }

    private AgricultureShrubs() {}
}
