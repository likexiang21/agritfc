package io.github.likexiang21.tfcplus.agriculture.common.crop;

import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureItems;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureSpices;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;

/** Resolves B's seed/waste items for exact A/TFC/B crop block IDs. */
public final class CropBItemResolver {

    public static Item seedForCropBlock(String blockId) {
        final String spice = AgricultureSpices.spiceIdFromCropBlockId(blockId);
        if (spice != null) {
            final var holder = AgricultureSpices.SEEDS.get(spice);
            return holder == null ? null : holder.get();
        }
        final TfcCropSpecies tfc = TfcCropSpecies.fromBlockId(blockId);
        if (tfc != null) {
            return net.minecraft.core.registries.BuiltInRegistries.ITEM.get(
                net.minecraft.resources.ResourceLocation.parse(tfc.seedItemId()));
        }
        final String aPrefix = "tfcfarmingplus:crop/";
        if (blockId.startsWith(aPrefix)) {
            final String crop = blockId.substring(aPrefix.length());
            return net.minecraft.core.registries.BuiltInRegistries.ITEM.get(
                net.minecraft.resources.ResourceLocation.parse("tfcfarmingplus:seeds/" + crop));
        }
        if (blockId.equals("tfcagricultureplus:crop/strawberry")) {
            return net.minecraft.core.registries.BuiltInRegistries.ITEM.get(
                net.minecraft.resources.ResourceLocation.parse("tfcagricultureplus:seeds/strawberry"));
        }
        return null;
    }

    public static ItemStack wasteForCropBlock(String blockId) {
        final String spice = AgricultureSpices.spiceIdFromCropBlockId(blockId);
        if (spice != null) {
            final var holder = AgricultureSpices.WASTES.get(spice);
            return holder == null ? ItemStack.EMPTY : new ItemStack(holder.get(), 1);
        }
        final String crop = CropWasteCrops.cropFromBlockId(blockId);
        if (crop == null) {
            if (blockId.equals("tfcagricultureplus:crop/strawberry")) {
                final var holder = AgricultureItems.CROP_WASTE.get("strawberry");
                return holder == null ? ItemStack.EMPTY : new ItemStack(holder.get(), 1);
            }
            return ItemStack.EMPTY;
        }
        final var holder = AgricultureItems.CROP_WASTE.get(crop);
        return holder == null ? ItemStack.EMPTY : new ItemStack(holder.get(), 1);
    }

    public static Item productForCropBlock(String blockId) {
        final String spice = AgricultureSpices.spiceIdFromCropBlockId(blockId);
        if (spice == null) {
            return null;
        }
        for (final SpiceSpecies species : SpiceSpecies.values()) {
            if (species.id().equals(spice)) {
                final var holder = AgricultureSpices.PRODUCTS.get(spice);
                return holder == null ? null : holder.get();
            }
        }
        return null;
    }

    public static int productCountForCropBlock(String blockId) {
        final String spice = AgricultureSpices.spiceIdFromCropBlockId(blockId);
        if (spice == null) {
            return 1;
        }
        for (final SpiceSpecies species : SpiceSpecies.values()) {
            if (species.id().equals(spice)) {
                return species.productYield();
            }
        }
        return 1;
    }

    public static ItemStack cormForCropBlock(String blockId) {
        final String spice = AgricultureSpices.spiceIdFromCropBlockId(blockId);
        if (spice == null) {
            return ItemStack.EMPTY;
        }
        final var holder = AgricultureSpices.CORMS.get(spice);
        return holder == null ? ItemStack.EMPTY : new ItemStack(holder.get(), 1);
    }

    public static ItemStack rootForCropBlock(String blockId) {
        final String spice = AgricultureSpices.spiceIdFromCropBlockId(blockId);
        if (spice == null) {
            return ItemStack.EMPTY;
        }
        final var holder = AgricultureSpices.ROOTS.get(spice);
        return holder == null ? ItemStack.EMPTY : new ItemStack(holder.get(), 1);
    }

    public static int seedCountForCropBlock(String blockId) {
        final String spice = AgricultureSpices.spiceIdFromCropBlockId(blockId);
        if (spice == null) {
            return 1;
        }
        for (final SpiceSpecies species : SpiceSpecies.values()) {
            if (species.id().equals(spice)) {
                return species.seedYield();
            }
        }
        return 1;
    }

    public static boolean isGrainBlock(String blockId) {
        return GrainCrop.fromCropBlockId(blockId) != null;
    }

    private CropBItemResolver() {}
}
