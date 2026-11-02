package io.github.likexiang21.tfcplus.agriculture.common.crop;

import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;

/**
 * Per-species propagation methods from docs/291 section 5 and the A/TFC crop matrix.
 *
 * <p>This class is the single source of truth for whether a seed may be sown directly or must
 * go through the nursery. It intentionally does not invent new propagation items: species that
 * need tubers, corms, rhizomes, crowns, runners or division are marked accordingly here, but the
 * corresponding vegetative item chain is still a separate migration item.
 */
public final class CropPropagation {

    public enum Method {
        SEED_DIRECT,
        NURSERY,
        RUNNER,
        TUBER,
        RHIZOME,
        CORM,
        CROWN,
        DIVISION
    }

    private static final Map<String, Method> METHODS = new LinkedHashMap<>();

    static {
        add(Method.SEED_DIRECT,
            // grains
            "millet", "foxtail_millet", "buckwheat", "fonio", "spelt", "emmer", "einkorn",
            "pearl_millet", "amaranth", "quinoa", "finger_millet", "sorghum", "jobs_tears",
            // legumes / oil / fiber seed crops
            "chickpea", "faba_bean", "lupin", "adzuki", "bambara_nut", "pea", "cowpea",
            "common_bean", "winged_bean", "pigeon_pea", "soybean", "peanut", "green_bean", "lentil",
            // quick leafy crops and root crops sown in place
            "spinach", "lettuce", "celery", "kale", "mustard_greens", "arugula", "purslane",
            "water_spinach", "malabar_spinach", "turnip", "parsnip", "celeriac", "salsify",
            "chicory_root", "radish", "carrot", "beet", "onion", "fenugreek",
            // TFC grains and industrial crops (same table, no tfc: prefix exemption)
            "barley", "oat", "rice", "rye", "wheat", "maize", "alfalfa", "canola", "jute",
            "papyrus", "sugarcane",
            // A fiber/oil/special crops that previously fell through to the nursery default
            "agave", "cotton", "flax", "hemp", "ramie", "safflower", "sesame", "sisal",
            "sunflower", "wild_rice_stem");
        add(Method.NURSERY,
            // heading brassicas, fruiting crops, cucurbits and water greens
            "napa_cabbage", "cabbage", "broccoli", "cauliflower", "brussels_sprouts",
            "swiss_chard", "celtuce", "garland_chrysanthemum", "perilla", "chili", "eggplant",
            "okra", "tomato", "red_bell_pepper", "yellow_bell_pepper", "loofah", "bitter_melon",
            "snake_gourd", "chayote", "bottle_gourd", "cantaloupe", "melon", "winter_melon",
            "squash", "pumpkin", "water_shield", "water_dropwort");
        add(Method.RUNNER, "strawberry");
        add(Method.TUBER, "sunchoke", "yacon", "potato", "yam");
        add(Method.RHIZOME, "ginger", "turmeric", "lotus", "hops");
        add(Method.CORM, "shallot", "garlic", "taro", "water_chestnut", "water_caltrop", "arrowhead", "gorgon_nut");
        add(Method.CROWN, "artichoke", "cardoon", "rhubarb", "asparagus");
        add(Method.DIVISION, "chive", "cassava");
    }

    private static void add(Method method, String... species) {
        for (final String crop : species) {
            METHODS.put(crop, method);
        }
    }

    /** All A/TFC/B seeds use the same table; no namespace exemption remains. */
    public static Method of(String crop) {
        return METHODS.getOrDefault(crop, Method.NURSERY);
    }

    public static boolean allowsDirectSowing(String crop) {
        return of(crop) == Method.SEED_DIRECT;
    }

    public static boolean isExplicitlyClassified(String crop) {
        return crop != null && METHODS.containsKey(crop);
    }

    /** Extracts the crop path from A/TFC/B seed item IDs; null for unknown external seeds. */
    public static String speciesFromSeedId(String itemId) {
        if (itemId == null) return null;
        if (itemId.startsWith("tfcfarmingplus:seeds/")) {
            return itemId.substring("tfcfarmingplus:seeds/".length());
        }
        if (itemId.startsWith("tfcagricultureplus:seeds/")) {
            return itemId.substring("tfcagricultureplus:seeds/".length());
        }
        if (itemId.startsWith("tfc:seeds/")) {
            return itemId.substring("tfc:seeds/".length());
        }
        return null;
    }

    public static Set<String> classifiedSpecies() {
        return METHODS.keySet();
    }

    private CropPropagation() {}
}
