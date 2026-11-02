package io.github.likexiang21.tfcplus.agriculture.common.blockentity;

import io.github.likexiang21.tfcplus.agriculture.common.block.MushroomBagBlock;
import io.github.likexiang21.tfcplus.agriculture.common.crop.MushroomSpecies;
import io.github.likexiang21.tfcplus.agriculture.common.registry.AgricultureBlockEntities;
import net.minecraft.core.BlockPos;
import net.minecraft.core.HolderLookup;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraft.world.level.block.state.BlockState;

/** Species/progress state for {@link MushroomBagBlock}; no menu or item handler. */
public final class MushroomBagBlockEntity extends BlockEntity {

    private String speciesId = "";
    private int progress;
    private int uses;

    public static final int MAX_USES = 3;

    public MushroomBagBlockEntity(BlockPos pos, BlockState state) {
        super(AgricultureBlockEntities.MUSHROOM_BAG.get(), pos, state);
    }

    public MushroomSpecies species() {
        return MushroomSpecies.fromBlockId("tfcagricultureplus:wild_mushroom/" + speciesId);
    }

    public void inoculate(MushroomSpecies species) {
        speciesId = species.id();
        progress = 0;
        setChanged();
    }

    public void markSpent() {
        progress = 0;
        uses++;
        setChanged();
    }

    public boolean maxed() {
        return uses >= MAX_USES;
    }

    public int uses() {
        return uses;
    }

    public static void serverTick(Level level, BlockPos pos, BlockState state, MushroomBagBlockEntity bag) {
        if (level.isClientSide()) {
            return;
        }
        final int stage = state.getValue(MushroomBagBlock.STAGE);
        final MushroomSpecies species = bag.species();
        if (species == null) {
            if (stage != 0) {
                level.setBlock(pos, state.setValue(MushroomBagBlock.STAGE, 0), 3);
            }
            return;
        }
        if (stage == 0) {
            level.setBlock(pos, state.setValue(MushroomBagBlock.STAGE, 1), 3);
            return;
        }
        if (stage == 1) {
            final float temperature = net.dries007.tfc.util.climate.Climate.getAverageTemperature(level, pos);
            final float preferred = net.dries007.tfc.util.climate.Climate.fromVanilla(species.preferredTemperature());
            final float tolerance = net.dries007.tfc.util.climate.Climate.fromVanilla(0.25F);
            if (Math.abs(temperature - preferred) > tolerance) {
                return;
            }
            bag.progress++;
            bag.setChanged();
            if (bag.progress >= species.cultivationTicks()) {
                level.setBlock(pos, state.setValue(MushroomBagBlock.STAGE, 2), 3);
            }
        }
    }

    @Override
    protected void saveAdditional(CompoundTag tag, HolderLookup.Provider registries) {
        super.saveAdditional(tag, registries);
        tag.putString("species", speciesId);
        tag.putInt("progress", progress);
        tag.putInt("uses", uses);
    }

    /** Copy persisted state into a dropped BlockItem's BLOCK_ENTITY_DATA component. */
    public void saveToItem(CompoundTag tag) {
        tag.putString("species", speciesId);
        tag.putInt("progress", progress);
        tag.putInt("uses", uses);
    }

    @Override
    protected void loadAdditional(CompoundTag tag, HolderLookup.Provider registries) {
        super.loadAdditional(tag, registries);
        speciesId = tag.getString("species");
        progress = tag.getInt("progress");
        uses = tag.getInt("uses");
    }
}
