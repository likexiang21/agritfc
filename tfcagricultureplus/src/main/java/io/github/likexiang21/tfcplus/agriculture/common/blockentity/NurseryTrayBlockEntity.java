package io.github.likexiang21.tfcplus.agriculture.common.blockentity;

import io.github.likexiang21.tfcplus.agriculture.common.block.NurseryTrayBlock;
import io.github.likexiang21.tfcplus.agriculture.common.crop.SeedTreatments;
import io.github.likexiang21.tfcplus.agriculture.common.item.SeedlingItem;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureBlockEntities;
import net.minecraft.core.BlockPos;
import net.minecraft.core.HolderLookup;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraft.world.level.block.state.BlockState;

/** One-seed nursery tray: stores the seed, grows, then produces a CROP_ID seedling item. */
public final class NurseryTrayBlockEntity extends BlockEntity {

    public static final int GROW_TICKS = 1200;
    private ItemStack seed = ItemStack.EMPTY;
    private int progress;
    private int requiredTicks = GROW_TICKS;

    public NurseryTrayBlockEntity(BlockPos pos, BlockState state) {
        super(AgricultureBlockEntities.NURSERY_TRAY.get(), pos, state);
    }

    public boolean canAccept(ItemStack stack) {
        if (!seed.isEmpty() || stack.isEmpty()) {
            return false;
        }
        final String id = BuiltInRegistries.ITEM.getKey(stack.getItem()).toString();
        // TFC is no longer exempted: tfc:seeds/<crop> resolves to the real tfc:crop/<crop>
        // block in SeedlingItem, so the seedling can be transplanted. Unknown external seeds
        // are rejected only when no crop block can be resolved.
        return SeedTreatments.isSeedItemId(id) && SeedlingItem.canResolveSeed(id);
    }

    public void insert(ItemStack stack) {
        seed = stack.copyWithCount(1);
        final String treatment = stack.get(io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureDataComponents.SEED_TREATMENT.get());
        requiredTicks = SeedTreatments.nurseryTicks(treatment);
        progress = 0;
        setChanged();
        sync();
    }

    public boolean ready() {
        return !seed.isEmpty() && progress >= requiredTicks;
    }

    public ItemStack takeSeedling() {
        if (!ready()) {
            return ItemStack.EMPTY;
        }
        final String id = BuiltInRegistries.ITEM.getKey(seed.getItem()).toString();
        final String treatment = seed.get(io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureDataComponents.SEED_TREATMENT.get());
        seed = ItemStack.EMPTY;
        progress = 0;
        setChanged();
        sync();
        final ItemStack seedling = SeedlingItem.forSeed(id);
        if (treatment != null && !treatment.isBlank()) {
            seedling.set(io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureDataComponents.SEED_TREATMENT.get(), treatment);
        }
        return seedling;
    }

    public ItemStack seed() {
        return seed;
    }

    private void sync() {
        if (level != null && !level.isClientSide()) {
            level.sendBlockUpdated(worldPosition, getBlockState(), getBlockState(), 3);
        }
    }

    public void dropSeed() {
        if (level == null || level.isClientSide()) {
            return;
        }
        if (!seed.isEmpty()) {
            net.minecraft.world.Containers.dropItemStack(level, worldPosition.getX() + 0.5,
                worldPosition.getY() + 0.5, worldPosition.getZ() + 0.5, seed.copy());
            seed = ItemStack.EMPTY;
            sync();
        }
    }

    public static void serverTick(Level level, BlockPos pos, BlockState state, NurseryTrayBlockEntity tray) {
        if (level.isClientSide()) {
            return;
        }
        final int stage = state.getValue(NurseryTrayBlock.STAGE);
        if (tray.seed.isEmpty()) {
            if (stage != 0) {
                level.setBlock(pos, state.setValue(NurseryTrayBlock.STAGE, 0), 3);
            }
            return;
        }
        if (tray.progress < tray.requiredTicks) {
            tray.progress++;
            if (tray.progress % 20 == 0) {
                tray.setChanged();
            }
        }
        final int target = tray.ready() ? 2 : 1;
        if (stage != target) {
            level.setBlock(pos, state.setValue(NurseryTrayBlock.STAGE, target), 3);
        }
    }

    @Override
    protected void saveAdditional(CompoundTag tag, HolderLookup.Provider registries) {
        super.saveAdditional(tag, registries);
        tag.put("seed", seed.isEmpty() ? new CompoundTag() : seed.save(registries));
        tag.putInt("progress", progress);
        tag.putInt("required_ticks", requiredTicks);
    }

    @Override
    public CompoundTag getUpdateTag(HolderLookup.Provider registries) {
        return saveWithoutMetadata(registries);
    }

    @Override
    public net.minecraft.network.protocol.game.ClientboundBlockEntityDataPacket getUpdatePacket() {
        return net.minecraft.network.protocol.game.ClientboundBlockEntityDataPacket.create(this);
    }

    @Override
    protected void loadAdditional(CompoundTag tag, HolderLookup.Provider registries) {
        super.loadAdditional(tag, registries);
        seed = ItemStack.parseOptional(registries, tag.getCompound("seed"));
        progress = tag.getInt("progress");
        requiredTicks = tag.contains("required_ticks") ? tag.getInt("required_ticks") : GROW_TICKS;
    }
}
