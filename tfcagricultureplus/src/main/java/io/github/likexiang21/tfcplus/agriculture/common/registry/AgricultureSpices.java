package io.github.likexiang21.tfcplus.agriculture.common.registry;

import io.github.likexiang21.tfcplus.agriculture.TFCAgriculturePlus;
import io.github.likexiang21.tfcplus.agriculture.common.block.SpiceCropBlocks;
import io.github.likexiang21.tfcplus.agriculture.common.crop.SpiceSpecies;
import io.github.likexiang21.tfcplus.agriculture.common.item.CormItem;
import io.github.likexiang21.tfcplus.agriculture.common.item.SpiceRootItem;
import java.util.LinkedHashMap;
import java.util.Map;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.CropBlock;
import net.minecraft.world.level.block.SoundType;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.neoforge.registries.DeferredHolder;
import net.neoforged.neoforge.registries.DeferredRegister;

/**
 * P0-H spice crop foundation.
 *
 * <p>This pass gives every spice a real plant -> grow -> harvest loop (vanilla CropBlock
 * mechanics) and a seed/product item. The 20 species' tree/vine/corm forms are recorded in
 * {@link SpiceSpecies} but are not yet implemented as distinct block classes; that specialization
 * remains a follow-up and is explicitly reported as a boundary rather than claimed complete.
 */
public final class AgricultureSpices {

    public static final DeferredRegister.Blocks BLOCKS =
        DeferredRegister.createBlocks(TFCAgriculturePlus.MOD_ID);
    public static final DeferredRegister.Items ITEMS =
        DeferredRegister.createItems(TFCAgriculturePlus.MOD_ID);

    public static final Map<String, DeferredHolder<Block, ? extends Block>> CROPS = new LinkedHashMap<>();
    public static final Map<String, DeferredHolder<Item, Item>> SEEDS = new LinkedHashMap<>();
    public static final Map<String, DeferredHolder<Item, Item>> PRODUCTS = new LinkedHashMap<>();
    public static final Map<String, DeferredHolder<Item, Item>> WASTES = new LinkedHashMap<>();
    public static final Map<String, DeferredHolder<Item, Item>> GROUND = new LinkedHashMap<>();
    public static final Map<String, DeferredHolder<Item, Item>> CORMS = new LinkedHashMap<>();
    public static final Map<String, DeferredHolder<Item, Item>> ROOTS = new LinkedHashMap<>();

    static {
        for (final SpiceSpecies species : SpiceSpecies.values()) {
            final boolean tree = "tree".equals(species.form());
            final DeferredHolder<Block, Block> crop;
            if (tree) {
                crop = null;
            } else {
                crop = BLOCKS.register(species.cropPath(), () -> newSpiceCrop(species,
                    BlockBehaviour.Properties.of()
                        .mapColor(net.minecraft.world.level.material.MapColor.PLANT)
                        .noCollission()
                        .randomTicks()
                        .instabreak()
                        .sound(SoundType.CROP)));
                CROPS.put(species.id(), crop);
                final DeferredHolder<Block, Block> registeredCrop = crop;
                SEEDS.put(species.id(), ITEMS.register(species.seedPath(),
                    () -> new BlockItem(registeredCrop.get(), new Item.Properties())));
            }
            PRODUCTS.put(species.id(), ITEMS.registerSimpleItem(species.productPath(), new Item.Properties()));
            WASTES.put(species.id(), ITEMS.registerSimpleItem(species.wastePath(), new Item.Properties()));
            GROUND.put(species.id(), ITEMS.registerSimpleItem("ground_spice/" + species.id(),
                new Item.Properties()));
            if ("corm".equals(species.form())) {
                CORMS.put(species.id(), ITEMS.register("spice_corm/" + species.id(),
                    () -> new CormItem(species.id(), new Item.Properties())));
            }
            if ("root".equals(species.form())) {
                ROOTS.put(species.id(), ITEMS.register("spice_root/" + species.id(),
                    () -> new SpiceRootItem(species.id(), new Item.Properties())));
            }
        }
    }

    private static Block newSpiceCrop(SpiceSpecies species, BlockBehaviour.Properties properties) {
        return switch (species.form()) {
            case "herb" -> new SpiceCropBlocks.Herb(properties);
            case "tree" -> new SpiceCropBlocks.Tree(properties);
            case "vine" -> new SpiceCropBlocks.Vine(properties);
            case "shrub" -> new SpiceCropBlocks.Shrub(properties);
            case "root" -> new SpiceCropBlocks.Root(properties);
            case "corm" -> new SpiceCropBlocks.Corm(properties);
            default -> new net.minecraft.world.level.block.CropBlock(properties);
        };
    }

    public static String spiceIdFromCropBlockId(String blockId) {
        final String prefix = TFCAgriculturePlus.MOD_ID + ":spice_crop/";
        return blockId != null && blockId.startsWith(prefix) ? blockId.substring(prefix.length()) : null;
    }

    public static void register(IEventBus bus) {
        BLOCKS.register(bus);
        ITEMS.register(bus);
    }

    private AgricultureSpices() {}
}
