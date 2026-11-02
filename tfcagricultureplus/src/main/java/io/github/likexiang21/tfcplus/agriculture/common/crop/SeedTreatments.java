package io.github.likexiang21.tfcplus.agriculture.common.crop;

/** Seed treatment stages stored on the existing seed stack as a DataComponent. */
public final class SeedTreatments {
    public static final String SOAKED = "soaked";
    public static final String GERMINATED = "germinated";
    public static final String DRESSED = "dressed";

    public static String next(String current) {
        if (current == null || current.isBlank()) return SOAKED;
        return switch (current) {
            case SOAKED -> GERMINATED;
            case GERMINATED -> DRESSED;
            default -> DRESSED;
        };
    }

    public static int boostForStage(String stage) {
        if (stage == null) return 0;
        return switch (stage) {
            case SOAKED -> 1;
            case GERMINATED -> 2;
            case DRESSED -> 3;
            default -> 0;
        };
    }

    /** Nursery growth time is shortened by 200 ticks per treatment step, floor 600 ticks. */
    public static int nurseryTicks(String stage) {
        return Math.max(600, 1200 - 200 * boostForStage(stage));
    }

    public static boolean isSeedItemId(String itemId) {
        if (itemId == null) return false;
        final int colon = itemId.indexOf(':');
        if (colon < 0) return false;
        final String path = itemId.substring(colon + 1);
        return path.startsWith("seeds/") || path.startsWith("seed/") || path.startsWith("spice_seed/");
    }

    private SeedTreatments() {}
}
