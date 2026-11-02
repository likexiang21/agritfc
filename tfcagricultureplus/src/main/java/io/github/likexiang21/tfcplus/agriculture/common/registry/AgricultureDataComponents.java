package io.github.likexiang21.tfcplus.agriculture.common.registry;

import io.github.likexiang21.tfcplus.agriculture.TFCAgriculturePlus;
import com.mojang.serialization.Codec;
import java.util.function.Supplier;
import net.minecraft.core.Registry;
import net.minecraft.core.component.DataComponentType;
import net.minecraft.core.registries.Registries;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.network.codec.ByteBufCodecs;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.neoforge.registries.DeferredRegister;
import net.neoforged.neoforge.registries.DeferredHolder;

/** B-owned data components. Dynamic dishes are encoded as a compound tag. */
public final class AgricultureDataComponents {
    public static final DeferredRegister<DataComponentType<?>> COMPONENTS =
        DeferredRegister.create(Registries.DATA_COMPONENT_TYPE, TFCAgriculturePlus.MOD_ID);

    public static final DeferredHolder<DataComponentType<?>, DataComponentType<CompoundTag>> DISH =
        COMPONENTS.register("dish", () -> DataComponentType.<CompoundTag>builder()
            .persistent(CompoundTag.CODEC)
            .networkSynchronized(ByteBufCodecs.COMPOUND_TAG)
            .build());

    /**
     * Crop identity carried by future crop-derived items (bundle/waste/seed-treatment data).
     * Kept as one string component rather than registering one component type per crop.
     */
    public static final DeferredHolder<DataComponentType<?>, DataComponentType<String>> CROP_ID =
        COMPONENTS.register("crop_id", () -> DataComponentType.<String>builder()
            .persistent(Codec.STRING)
            .networkSynchronized(ByteBufCodecs.STRING_UTF8)
            .build());

    /** Seed treatment stage on the existing seed stack: soaked / germinated / dressed. */
    public static final DeferredHolder<DataComponentType<?>, DataComponentType<String>> SEED_TREATMENT =
        COMPONENTS.register("seed_treatment", () -> DataComponentType.<String>builder()
            .persistent(Codec.STRING)
            .networkSynchronized(ByteBufCodecs.STRING_UTF8)
            .build());

    public static void register(IEventBus bus) {
        COMPONENTS.register(bus);
    }

    private AgricultureDataComponents() {}
}
