package io.github.likexiang21.tfcplus.agriculture.common.crop;

/**
 * The 16 long-stem grain crops that use the bundle -> thresh -> grain + wet_grass route.
 *
 * <p>A crops are owned by {@code tfcfarmingplus}; TFC crops are owned by TFC. This enum only
 * stores stable IDs and does not import either mod, so it is safe to compile standalone and
 * usable from data-driven recipes later.
 */
public enum GrainCrop {
    // A: 10 long-stem grains. Max ages are taken from the real A blockstates.
    MILLET("millet", Source.A, "tfcfarmingplus:food/millet", "tfcfarmingplus:seeds/millet", 7),
    FOXTAIL_MILLET("foxtail_millet", Source.A, "tfcfarmingplus:food/foxtail_millet", "tfcfarmingplus:seeds/foxtail_millet", 7),
    FONIO("fonio", Source.A, "tfcfarmingplus:food/fonio", "tfcfarmingplus:seeds/fonio", 7),
    SPELT("spelt", Source.A, "tfcfarmingplus:food/spelt", "tfcfarmingplus:seeds/spelt", 7),
    EMMER("emmer", Source.A, "tfcfarmingplus:food/emmer", "tfcfarmingplus:seeds/emmer", 7),
    EINKORN("einkorn", Source.A, "tfcfarmingplus:food/einkorn", "tfcfarmingplus:seeds/einkorn", 7),
    PEARL_MILLET("pearl_millet", Source.A, "tfcfarmingplus:food/pearl_millet", "tfcfarmingplus:seeds/pearl_millet", 7),
    FINGER_MILLET("finger_millet", Source.A, "tfcfarmingplus:food/finger_millet", "tfcfarmingplus:seeds/finger_millet", 7),
    SORGHUM("sorghum", Source.A, "tfcfarmingplus:food/sorghum", "tfcfarmingplus:seeds/sorghum", 5),
    JOBS_TEARS("jobs_tears", Source.A, "tfcfarmingplus:food/jobs_tears", "tfcfarmingplus:seeds/jobs_tears", 7),

    // TFC: 6 long-stem grains. TFC maize is age 0..5; the other five are 0..7.
    BARLEY("barley", Source.TFC, "tfc:food/barley_grain", "tfc:seeds/barley", 7),
    OAT("oat", Source.TFC, "tfc:food/oat_grain", "tfc:seeds/oat", 7),
    RICE("rice", Source.TFC, "tfc:food/rice_grain", "tfc:seeds/rice", 7),
    RYE("rye", Source.TFC, "tfc:food/rye_grain", "tfc:seeds/rye", 7),
    WHEAT("wheat", Source.TFC, "tfc:food/wheat_grain", "tfc:seeds/wheat", 7),
    MAIZE("maize", Source.TFC, "tfc:food/maize_grain", "tfc:seeds/maize", 5);

    public enum Source {
        A,
        TFC
    }

    private final String id;
    private final Source source;
    private final String grainItemId;
    private final String seedItemId;
    private final int maxAge;

    GrainCrop(String id, Source source, String grainItemId, String seedItemId, int maxAge) {
        this.id = id;
        this.source = source;
        this.grainItemId = grainItemId;
        this.seedItemId = seedItemId;
        this.maxAge = maxAge;
    }

    public String id() {
        return id;
    }

    public Source source() {
        return source;
    }

    public String grainItemId() {
        return grainItemId;
    }

    public String seedItemId() {
        return seedItemId;
    }

    public int maxAge() {
        return maxAge;
    }

    public boolean isMature(int age) {
        return age >= maxAge;
    }

    public String bundlePath() {
        return "grain_bundle/" + id;
    }

    public String bundleId() {
        return "tfcagricultureplus:" + bundlePath();
    }

    public String cropBlockId() {
        return (isTfc() ? "tfc:crop/" : "tfcfarmingplus:crop/") + id;
    }

    public boolean isTfc() {
        return source == Source.TFC;
    }

    /** Reverse lookup for the block-break handler; null when the block is not a bundle crop. */
    public static GrainCrop fromCropBlockId(String blockId) {
        for (GrainCrop crop : values()) {
            if (crop.cropBlockId().equals(blockId)) {
                return crop;
            }
        }
        return null;
    }
}
