package io.github.likexiang21.tfcplus.agriculture.common.blockentity;

import io.github.likexiang21.tfcplus.agriculture.common.block.KitchenStorageBlock;
import io.github.likexiang21.tfcplus.agriculture.common.container.BContainer;

import io.github.likexiang21.tfcplus.agriculture.TFCAgriculturePlus;
import io.github.likexiang21.tfcplus.agriculture.common.menu.KitchenStorageMenu;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureBlockEntities;
import net.dries007.tfc.common.blockentities.InventoryBlockEntity;
import net.dries007.tfc.common.component.food.FoodCapability;
import net.minecraft.core.BlockPos;
import net.minecraft.core.HolderLookup;
import net.minecraft.core.registries.Registries;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.tags.TagKey;
import net.minecraft.world.Containers;
import net.minecraft.world.entity.player.Inventory;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.inventory.AbstractContainerMenu;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.material.Fluids;
import net.neoforged.neoforge.capabilities.Capabilities;
import net.neoforged.neoforge.fluids.FluidStack;
import net.neoforged.neoforge.fluids.capability.templates.FluidTank;
import net.neoforged.neoforge.items.ItemStackHandler;
import org.jetbrains.annotations.Nullable;

/**
 * Shared TFC inventory contract for the first kitchen furniture batch.
 *
 * <p>The block kind is not decorative: each kind has its own slot filter and stack limit.
 * All kinds keep the same nine-slot menu and screen contract, but only accept the items
 * that make sense for that piece of furniture.
 */
public final class KitchenStorageBlockEntity extends InventoryBlockEntity<ItemStackHandler> implements BContainer {
    public static final int SLOTS = 9;

    private static final TagKey<Item> SPICES = TagKey.create(
        Registries.ITEM,
        ResourceLocation.fromNamespaceAndPath(TFCAgriculturePlus.MOD_ID, "spices"));

    private final KitchenStorageBlock.StorageKind kind;
    @Nullable
    private final FluidTank sinkTank;

    public KitchenStorageBlockEntity(BlockPos pos, BlockState state) {
        super(AgricultureBlockEntities.KITCHEN_STORAGE.get(), pos, state,
            defaultInventory(SLOTS), TFCAgriculturePlus.MOD_ID);
        this.kind = state.getBlock() instanceof KitchenStorageBlock block
            ? block.storageKind()
            : KitchenStorageBlock.StorageKind.COUNTER_CABINET;
        this.sinkTank = kind == KitchenStorageBlock.StorageKind.SINK_CABINET
            ? new FluidTank(4000, (FluidStack fluid) -> fluid.getFluid().isSame(Fluids.WATER))
            : null;
    }

    public KitchenStorageBlock.StorageKind kind() {
        return kind;
    }

    /** Only sink cabinets expose a water tank; all other kinds return null. */
    @Nullable
    public FluidTank sinkTank() {
        return sinkTank;
    }

    @Override
    public void loadAdditional(CompoundTag nbt, HolderLookup.Provider provider) {
        super.loadAdditional(nbt, provider);
        if (sinkTank != null && nbt.contains("sink_tank")) {
            sinkTank.readFromNBT(provider, nbt.getCompound("sink_tank"));
        }
    }

    @Override
    public void saveAdditional(CompoundTag nbt, HolderLookup.Provider provider) {
        if (sinkTank != null) {
            nbt.put("sink_tank", sinkTank.writeToNBT(provider, new CompoundTag()));
        }
        super.saveAdditional(nbt, provider);
    }

    @Override
    public AbstractContainerMenu createMenu(int containerId, Inventory playerInventory, Player player) {
        return KitchenStorageMenu.create(this, playerInventory, containerId);
    }

    @Override
    public Component getDisplayName() {
        return Component.translatable("block_entity.tfcagricultureplus.kitchen_storage." + kind.storageId());
    }

    @Override
    public int getSlotStackLimit(int slot) {
        return switch (kind) {
            case HALF_CABINET -> 16;
            case SINK_CABINET, FRUIT_BOWL -> 1;
            default -> 64;
        };
    }

    @Override
    public boolean isItemValid(int slot, ItemStack stack) {
        if (slot < 0 || slot >= SLOTS || stack.isEmpty()) return false;
        return switch (kind) {
            case COUNTER_CABINET, HALF_CABINET -> true;
            case SINK_CABINET -> stack.getCapability(Capabilities.FluidHandler.ITEM) != null;
            case SPICE_RACK -> stack.is(SPICES);
            case FOOD_DISPLAY, FRUIT_BOWL -> FoodCapability.has(stack);
        };
    }

    public void dropContents() {
        if (level == null || level.isClientSide()) return;
        for (int slot = 0; slot < SLOTS; slot++) {
            final ItemStack stack = inventory.extractItem(slot, inventory.getStackInSlot(slot).getCount(), false);
            if (!stack.isEmpty()) {
                Containers.dropItemStack(level, worldPosition.getX() + 0.5,
                    worldPosition.getY() + 0.5, worldPosition.getZ() + 0.5, stack);
            }
        }
        if (sinkTank != null) {
            sinkTank.setFluid(FluidStack.EMPTY);
        }
        setChanged();
    }

    @Override public net.neoforged.neoforge.items.IItemHandler bItemHandler() { return inventory; }

    /** UI-light deposit: merge into an existing valid slot or the first empty valid slot. */
    public boolean quickInsert(ItemStack stack) {
        if (stack.isEmpty()) return false;
        for (int slot = 0; slot < SLOTS; slot++) {
            final ItemStack current = inventory.getStackInSlot(slot);
            if (!current.isEmpty() && ItemStack.isSameItemSameComponents(current, stack)
                && isItemValid(slot, stack)) {
                final int limit = getSlotStackLimit(slot);
                final int room = limit - current.getCount();
                if (room > 0) {
                    final int moved = Math.min(room, stack.getCount());
                    current.grow(moved);
                    inventory.setStackInSlot(slot, current);
                    stack.shrink(moved);
                    setChanged();
                    return moved > 0;
                }
            }
        }
        for (int slot = 0; slot < SLOTS; slot++) {
            if (inventory.getStackInSlot(slot).isEmpty() && isItemValid(slot, stack)) {
                final int moved = Math.min(getSlotStackLimit(slot), stack.getCount());
                inventory.setStackInSlot(slot, stack.copyWithCount(moved));
                stack.shrink(moved);
                setChanged();
                return moved > 0;
            }
        }
        return false;
    }

    /** UI-light extraction: pull one item from the last occupied slot. */
    public ItemStack quickExtract() {
        for (int slot = SLOTS - 1; slot >= 0; slot--) {
            final ItemStack current = inventory.getStackInSlot(slot);
            if (!current.isEmpty()) {
                final ItemStack out = current.copyWithCount(1);
                current.shrink(1);
                inventory.setStackInSlot(slot, current);
                setChanged();
                return out;
            }
        }
        return ItemStack.EMPTY;
    }
}
