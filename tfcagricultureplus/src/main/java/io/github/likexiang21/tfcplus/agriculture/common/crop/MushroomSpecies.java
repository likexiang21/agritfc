package io.github.likexiang21.tfcplus.agriculture.common.crop;

import java.util.List;
import java.util.Map;

/**
 * The 15 mushroom species from docs/291 §9.3.
 *
 * <p>All 15 get wild world generation and natural respawn. The four species marked
 * {@code naturalOnly} must never get a cultivation-bag recipe; the other 11 are the future
 * bag/log candidates. This enum is pure data so the prototype and resource generator can use it
 * without Minecraft classes.
 */
public enum MushroomSpecies {
    OYSTER("oyster", "平菇", false),
    SHIITAKE("shiitake", "香菇", false),
    BUTTON("button", "双孢菇", false),
    ENOKI("enoki", "金针菇", false),
    WOOD_EAR("wood_ear", "木耳", false),
    REISHI("reishi", "灵芝", false),
    LIONS_MANE("lions_mane", "猴头菇", false),
    MAITAKE("maitake", "舞茸", false),
    KING_OYSTER("king_oyster", "杏鲍菇", false),
    SHIMEJI("shimeji", "蟹味菇", false),
    TURKEY_TAIL("turkey_tail", "云芝", false),
    PORCINI("porcini", "牛肝菌", true),
    MOREL("morel", "羊肚菌", true),
    CHANTERELLE("chanterelle", "鸡油菌", true),
    BLACK_TRUFFLE("black_truffle", "黑松露", true);

    private final String id;
    private final String cnName;
    private final boolean naturalOnly;

    private static final Map<String, Integer> CULTIVATION_TICKS = Map.ofEntries(
        Map.entry("oyster", 1200),
        Map.entry("shiitake", 1600),
        Map.entry("button", 1800),
        Map.entry("enoki", 1400),
        Map.entry("wood_ear", 1300),
        Map.entry("reishi", 2400),
        Map.entry("lions_mane", 2000),
        Map.entry("maitake", 2200),
        Map.entry("king_oyster", 1800),
        Map.entry("shimeji", 1500),
        Map.entry("turkey_tail", 2000)
    );

    MushroomSpecies(String id, String cnName, boolean naturalOnly) {
        this.id = id;
        this.cnName = cnName;
        this.naturalOnly = naturalOnly;
    }

    public String id() {
        return id;
    }

    public String cnName() {
        return cnName;
    }

    public boolean naturalOnly() {
        return naturalOnly;
    }

    /** Colonisation time inside the cultivation bag; 0 for natural-only species. */
    public int cultivationTicks() {
        return naturalOnly ? 0 : CULTIVATION_TICKS.getOrDefault(id, 1200);
    }

    /** Bag harvest minimum; natural-only species never reach this path. */
    public int bagMinYield() {
        return switch (id) {
            case "oyster", "button", "enoki", "shimeji" -> 3;
            case "reishi", "lions_mane", "turkey_tail" -> 1;
            default -> 2;
        };
    }

    public int bagMaxYield() {
        return switch (id) {
            case "reishi", "lions_mane", "turkey_tail" -> 2;
            case "shiitake", "wood_ear", "maitake", "king_oyster" -> 3;
            default -> 4;
        };
    }

    /** Preferred bag temperature on the vanilla biome scale; natural-only species use 0. */
    public float preferredTemperature() {
        return switch (id) {
            case "enoki" -> 0.3F;
            case "button", "lions_mane", "maitake", "shimeji" -> 0.4F;
            case "oyster", "shiitake", "king_oyster" -> 0.5F;
            case "wood_ear", "reishi", "turkey_tail" -> 0.6F;
            default -> 0.0F;
        };
    }

    public boolean bagTemperatureOk(float temperature) {
        return !naturalOnly && Math.abs(temperature - preferredTemperature()) <= 0.25F;
    }

    public String blockPath() {
        return "wild_mushroom/" + id;
    }

    public String blockId() {
        return "tfcagricultureplus:" + blockPath();
    }

    public static List<MushroomSpecies> naturalOnlySpecies() {
        return java.util.Arrays.stream(values()).filter(MushroomSpecies::naturalOnly).toList();
    }

    public static List<MushroomSpecies> cultivableSpecies() {
        return java.util.Arrays.stream(values()).filter(s -> !s.naturalOnly()).toList();
    }

    /** Resolve a wild block item/block ID such as {@code ...:wild_mushroom/oyster}. */
    public static MushroomSpecies fromBlockId(String blockId) {
        if (blockId == null) {
            return null;
        }
        final String prefix = "tfcagricultureplus:wild_mushroom/";
        if (!blockId.startsWith(prefix)) {
            return null;
        }
        final String id = blockId.substring(prefix.length());
        for (MushroomSpecies species : values()) {
            if (species.id.equals(id)) {
                return species;
            }
        }
        return null;
    }
}
