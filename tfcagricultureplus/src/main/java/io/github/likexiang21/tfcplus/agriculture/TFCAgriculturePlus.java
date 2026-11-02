package io.github.likexiang21.tfcplus.agriculture;

import com.mojang.brigadier.arguments.StringArgumentType;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.item.ItemStack;

import io.github.likexiang21.tfcplus.agriculture.common.crop.ACropSeedReturnHandler;
import io.github.likexiang21.tfcplus.agriculture.common.crop.BushHarvestHandler;
import io.github.likexiang21.tfcplus.agriculture.common.crop.BushRightClickHarvestHandler;
import io.github.likexiang21.tfcplus.agriculture.common.crop.BushWasteHandler;
import io.github.likexiang21.tfcplus.agriculture.common.crop.CropWasteHandler;
import io.github.likexiang21.tfcplus.agriculture.common.crop.DirectSeedPlantingGate;
import io.github.likexiang21.tfcplus.agriculture.common.crop.FirmalifePlantWasteHandler;
import io.github.likexiang21.tfcplus.agriculture.common.crop.GrainHarvestHandler;
import io.github.likexiang21.tfcplus.agriculture.common.crop.MacadamiaDropHandler;
import io.github.likexiang21.tfcplus.agriculture.common.crop.NutShellFuelHandler;
import io.github.likexiang21.tfcplus.agriculture.common.crop.SeedTreatmentHandler;
import io.github.likexiang21.tfcplus.agriculture.common.crop.SeedTreatmentGrowthHandler;
import io.github.likexiang21.tfcplus.agriculture.common.crop.SeedTreatmentTooltip;
import io.github.likexiang21.tfcplus.agriculture.common.crop.SpiceSeedDropHandler;
import io.github.likexiang21.tfcplus.agriculture.common.crop.StrawberryWasteHandler;
import io.github.likexiang21.tfcplus.agriculture.common.crop.StrawberrySeedDropHandler;
import io.github.likexiang21.tfcplus.agriculture.common.crop.TfcSeedReturnHandler;
import io.github.likexiang21.tfcplus.agriculture.common.crop.UnifiedCropHarvestHandler;
import io.github.likexiang21.tfcplus.agriculture.common.crop.WildNutDropHandler;
import io.github.likexiang21.tfcplus.agriculture.common.item.MetalCanItem;
import io.github.likexiang21.tfcplus.agriculture.common.recipe.AgricultureRecipeSerializers;
import io.github.likexiang21.tfcplus.agriculture.common.recipe.AgricultureRecipeTypes;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureBlockEntities;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureBlocks;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureCreativeTab;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureDataComponents;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureFoodTraits;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureItems;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureMenuTypes;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgriculturePlates;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureSpatulas;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureShrubs;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureSpices;
import io.github.likexiang21.tfcplus.agriculture.common.registry.WoodworkingSounds;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.fml.ModContainer;
import net.neoforged.fml.ModList;
import net.neoforged.fml.common.Mod;
import net.neoforged.fml.event.lifecycle.FMLCommonSetupEvent;
import net.neoforged.neoforge.capabilities.Capabilities;
import net.neoforged.neoforge.capabilities.RegisterCapabilitiesEvent;
import net.neoforged.neoforge.common.NeoForge;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * B 层入口 —— TFC Agriculture Plus（`tfcagricultureplus`）。
 *
 * <p>定位：建立在 A 层（TFC Farming Plus）之上的**食品加工重制层**。
 * 设计文档：`moddev/docs/126-b-module-implementation.md`。
 *
 * <p>🛑 红线 5（126 §〇.3）：**检测不到 A 时硬失败**，不静默降级 ——
 * B 的绝大多数内容都建立在 A 的 86 物种与方块之上，缺了 A 会得到一堆无意义的内容。
 *
 * <p>⚠️ 日志一律 ASCII：本机控制台是 GBK，中文会乱码（A 层踩过）。
 */
@Mod(TFCAgriculturePlus.MOD_ID)
public final class TFCAgriculturePlus {

    public static final String MOD_ID = "tfcagricultureplus";
    public static final Logger LOGGER = LoggerFactory.getLogger("TFC Agriculture Plus");

    /** A 层的 mod id —— B 的硬前置。 */
    public static final String A_MOD_ID = "tfcfarmingplus";

    public TFCAgriculturePlus(IEventBus modBus, ModContainer container) {
        // 🛑 红线 5：硬失败（不静默降级）
        if (!ModList.get().isLoaded(A_MOD_ID)) {
            throw new IllegalStateException(
                "[tfcagricultureplus] Missing required dependency: tfcfarmingplus (TFC Farming Plus). "
                    + "Do NOT install this mod standalone.");
        }

        // 注册表：**顺序敏感**（与 A 的既有顺序一致：Blocks -> Items -> BEs -> CreativeTab）
        AgricultureBlocks.register(modBus);
        AgricultureItems.register(modBus);
        AgricultureSpices.register(modBus);
        AgricultureShrubs.register(modBus);
        AgriculturePlates.register(modBus);
        AgricultureSpatulas.register(modBus);
        WoodworkingSounds.register(modBus);
        AgricultureFoodTraits.register(modBus);
        AgricultureDataComponents.register(modBus);
        AgricultureBlockEntities.register(modBus);
        AgricultureMenuTypes.MENUS.register(modBus);
        AgricultureCreativeTab.register(modBus);

        // Runtime registry smoke counts: these are printed before any resource/world load.
        LOGGER.info("[TFC Agriculture Plus] registries: spiceCrops={}, spiceTrees={}, cropWaste={}, wildMushrooms={}",
            AgricultureSpices.CROPS.size(), AgricultureBlocks.SPICE_TREE_SAPLINGS.size(),
            AgricultureItems.CROP_WASTE.size(), AgricultureBlocks.WILD_MUSHROOMS.size());

        // 🆕 配方基建（批次 1 rev3：为后续加工配方 + JEI 适配打基础）
        // 顺序：Serializer 先于 Type（类型被引用时 serializer 必须已存在）
        AgricultureRecipeSerializers.register(modBus);
        AgricultureRecipeTypes.register(modBus);

        modBus.addListener(this::commonSetup);
        modBus.addListener(this::registerCapabilities);

        // P0-B: replace mature long-stem grain harvest with bundle + seed.
        // Game-bus listener, not a resource-only loot-table edit; see GrainHarvestHandler.
        NeoForge.EVENT_BUS.addListener(GrainHarvestHandler::onBlockBreak);
        // P0-X: B-controlled harvest for every non-grain A/TFC/B crop block.
        NeoForge.EVENT_BUS.addListener(UnifiedCropHarvestHandler::onBlockBreak);
        // P0-B: add actual per-crop green waste at mature harvest; original drops stay.
        NeoForge.EVENT_BUS.addListener(CropWasteHandler::onBlockBreak);
        // P0-J: add real residue to the 10 remaining TFC berry bushes; original drops stay.
        NeoForge.EVENT_BUS.addListener(BushWasteHandler::onBlockBreak);
        // TFC/Firmalife plants are not exempt: Firmalife herb blocks contribute B spice waste.
        NeoForge.EVENT_BUS.addListener(FirmalifePlantWasteHandler::onBlockBreak);
        // P0-AJ: strawberry is A's ordinary crop record, not one of the TFC 10 bushes.
        NeoForge.EVENT_BUS.addListener(StrawberryWasteHandler::onBlockBreak);
        // P0-AM: initial B strawberry seed source from TFC strawberry bush.
        NeoForge.EVENT_BUS.addListener(StrawberrySeedDropHandler::onBlockBreak);
        // P0-O: fruiting TFC bush break becomes harvest + regrowth instead of block removal.
        NeoForge.EVENT_BUS.addListener(BushHarvestHandler::onBlockBreak);
        // P0-AE: empty-hand right-click picking uses the same TFC stateAfterPicking path.
        NeoForge.EVENT_BUS.addListener(BushRightClickHarvestHandler::onRightClickBlock);
        // P0-L: seed + wet grass in offhand advances a DataComponent treatment stage.
        NeoForge.EVENT_BUS.addListener(SeedTreatmentHandler::onRightClickItem);
        // P0-AI: show the treatment stage on the seed tooltip.
        NeoForge.EVENT_BUS.addListener(SeedTreatmentTooltip::onItemTooltip);
        // P0-N: treated seed applies a bounded growth boost after planting.
        NeoForge.EVENT_BUS.addListener(SeedTreatmentGrowthHandler::onRightClickBlock);
        // P0-Q: guarantee one seed back from mature non-grain TFC crops.
        NeoForge.EVENT_BUS.addListener(TfcSeedReturnHandler::onBlockBreak);
        // P0-W: seed return for A's 87 crop blocks (grains handled by the bundle path).
        NeoForge.EVENT_BUS.addListener(ACropSeedReturnHandler::onBlockBreak);
        // P0-U: low-rate wild spice seed source from vanilla grass, before wild spice worldgen.
        NeoForge.EVENT_BUS.addListener(SpiceSeedDropHandler::onBlockBreak);
        // P0-Z: B macadamia from A's existing macadamia fruit-tree leaves.
        NeoForge.EVENT_BUS.addListener(MacadamiaDropHandler::onBlockBreak);
        // P0-AD: temporary grass source for pistachio/cashew until their trees exist.
        NeoForge.EVENT_BUS.addListener(WildNutDropHandler::onBlockBreak);
        // P0-AF: nut shells and crop waste are valid low-tier furnace fuel.
        NeoForge.EVENT_BUS.addListener(NutShellFuelHandler::onFuelBurnTime);
        // P0-V: direct seed planting is replaced by nursery -> seedling -> transplant.
        NeoForge.EVENT_BUS.addListener(DirectSeedPlantingGate::onRightClickBlock);

        LOGGER.info("[TFC Agriculture Plus] loaded, dependency A version = {}",
            ModList.get().getModContainerById(A_MOD_ID)
                .map(c -> c.getModInfo().getVersion().toString()).orElse("?"));
    }

    /** Expose every TFC InventoryBlockEntity through the standard item capability. */
    private void registerCapabilities(RegisterCapabilitiesEvent event) {
        event.registerBlockEntity(Capabilities.ItemHandler.BLOCK, AgricultureBlockEntities.CUTTING_BOARD.get(),
            (be, side) -> be.getSidedInventory(side));
        event.registerBlockEntity(Capabilities.ItemHandler.BLOCK, AgricultureBlockEntities.LOG_CUTTING_BOARD.get(),
            (be, side) -> be.getSidedInventory(side));
        event.registerBlockEntity(Capabilities.ItemHandler.BLOCK, AgricultureBlockEntities.MORTAR.get(),
            (be, side) -> be.getSidedInventory(side));
        event.registerBlockEntity(Capabilities.ItemHandler.BLOCK, AgricultureBlockEntities.DRYING_RACK.get(),
            (be, side) -> be.getSidedInventory(side));
        event.registerBlockEntity(Capabilities.ItemHandler.BLOCK, AgricultureBlockEntities.KNIFE_BLOCK.get(),
            (be, side) -> be.getSidedInventory(side));
        event.registerBlockEntity(Capabilities.ItemHandler.BLOCK, AgricultureBlockEntities.LUMBER_PILE.get(),
            (be, side) -> be.bItemHandler());
        event.registerBlockEntity(Capabilities.ItemHandler.BLOCK, AgricultureBlockEntities.SILKWORM_RACK.get(),
            (be, side) -> be.getSidedInventory(side));
        event.registerBlockEntity(Capabilities.ItemHandler.BLOCK, AgricultureBlockEntities.PLACEABLE_FOOD.get(),
            (be, side) -> be.getInventory());
        event.registerBlockEntity(Capabilities.ItemHandler.BLOCK, AgricultureBlockEntities.KITCHEN_STORAGE.get(),
            (be, side) -> be.bItemHandler());
        event.registerBlockEntity(Capabilities.FluidHandler.BLOCK, AgricultureBlockEntities.KITCHEN_STORAGE.get(),
            (be, side) -> be.sinkTank());
        event.registerBlockEntity(Capabilities.FluidHandler.BLOCK, AgricultureBlockEntities.COOKING_PAN.get(),
            (be, side) -> be.oilTank());
        for (final var can : AgricultureItems.METAL_CANS.values()) {
            event.registerItem(Capabilities.FluidHandler.ITEM,
                (stack, context) -> stack.getItem() instanceof MetalCanItem item
                    ? new net.dries007.tfc.common.component.fluid.FluidContainerHandler(stack, item.containerInfo())
                    : null,
                can.get());
        }
    }

    private void commonSetup(FMLCommonSetupEvent event) {
        event.enqueueWork(() -> {
            // Later batches hook in here: override registry self-check / recipe type registration / in_world handler
            io.github.likexiang21.tfcplus.agriculture.common.timber.TimberBlocks.registerPlacement();
        });
    }
}
