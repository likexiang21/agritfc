package io.github.likexiang21.tfcplus.agriculture.common.crop;

/**
 * One crop's yield accounting row.
 *
 * <p>This is deliberately a plain Java record with no Minecraft imports so it can be
 * compiled and exercised by the standalone P0 prototype before the mod registry is touched.
 *
 * <p>Invariants from docs/291/292:
 * <ul>
 *   <li>{@code seedBack >= 1}: a harvest must return at least one seed/seed piece;</li>
 *   <li>{@code processed >= 1}: every crop must have a usable primary output;</li>
 *   <li>{@code byproduct >= 1}: every crop must have a byproduct outlet;</li>
 *   <li>{@code processed <= raw}: processing must not create mass.</li>
 * </ul>
 */
public record CropYieldLedger(String crop, int raw, int seedBack, int processed, int byproduct) {

    public CropYieldLedger {
        if (crop == null || crop.isBlank()) {
            throw new IllegalArgumentException("crop id must not be blank");
        }
        if (raw <= 0) {
            throw new IllegalArgumentException("raw must be > 0: " + crop);
        }
        if (seedBack < 0 || processed < 0 || byproduct < 0) {
            throw new IllegalArgumentException("negative yield component: " + crop);
        }
    }

    public boolean isValid() {
        return seedBack >= 1
            && processed >= 1
            && byproduct >= 1
            && processed <= raw;
    }

    /** Processed primary output; the value used by food/processing recipes. */
    public int netProcessed() {
        return processed;
    }

    /** Processed primary output plus byproduct; useful for whole-harvest accounting. */
    public int totalUseful() {
        return processed + byproduct;
    }

    /** Short human-readable reason; empty when valid. */
    public String invalidReason() {
        if (seedBack < 1) return "seedBack < 1";
        if (processed < 1) return "processed < 1";
        if (byproduct < 1) return "byproduct < 1";
        if (processed > raw) return "processed > raw";
        return "";
    }
}
