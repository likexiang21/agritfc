package io.github.likexiang21.tfcplus.agriculture.common.crop;

/** The 10 TFC berry bushes that remain after strawberry was migrated to an A crop. */
public enum BushSpecies {
    BLACKBERRY("blackberry"),
    BLUEBERRY("blueberry"),
    BUNCHBERRY("bunchberry"),
    CLOUDBERRY("cloudberry"),
    CRANBERRY("cranberry"),
    ELDERBERRY("elderberry"),
    GOOSEBERRY("gooseberry"),
    RASPBERRY("raspberry"),
    SNOWBERRY("snowberry"),
    WINTERGREEN("wintergreen");

    private final String id;

    BushSpecies(String id) {
        this.id = id;
    }

    public String id() {
        return id;
    }

    public String tfcBushBlockId() {
        // TFC's wintergreen block is wintergreen_berry_bush, not wintergreen_bush.
        final String blockId = id.equals("wintergreen") ? "wintergreen_berry" : id;
        return "tfc:plant/" + blockId + "_bush";
    }

    public String wastePath() {
        return "bush_waste/" + id;
    }

    public static BushSpecies fromTfcBushBlockId(String blockId) {
        if (blockId == null) {
            return null;
        }
        // TFC also exposes the *_bush_cane form of the same 10 bushes.
        if (blockId.endsWith("_bush_cane")) {
            blockId = blockId.substring(0, blockId.length() - "_cane".length());
        }
        for (BushSpecies bush : values()) {
            if (bush.tfcBushBlockId().equals(blockId)) {
                return bush;
            }
        }
        return null;
    }
}
