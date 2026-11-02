package io.github.likexiang21.tfcplus.agriculture.common.crop;

import java.util.List;
import java.util.Set;

/**
 * The 82 A/TFC crops whose real harvest/trim step produces a leaf/stem/vine/pod/peel residue.
 *
 * <p>This is intentionally not "one waste item per registered crop": grain, oilseed, fiber,
 * nut and mushroom crops are absent because their byproducts are straw/cake/shives/shell/spent
 * substrate, not green crop waste. The list mirrors docs/291 §4.1.2 and also accepts the
 * corresponding wild-crop block IDs so TFC/A wild plants are not exempt from the waste chain.
 */
public final class CropWasteCrops {

    public static final List<String> ALL = List.of(
        "spinach", "lettuce", "celery", "kale", "napa_cabbage", "cabbage", "mustard_greens", "broccoli", "cauliflower",
        "brussels_sprouts", "swiss_chard", "celtuce", "garland_chrysanthemum", "perilla", "arugula", "turnip", "parsnip",
        "sunchoke", "shallot", "celeriac", "salsify", "ginger", "turmeric", "yacon", "chicory_root",
        "chickpea", "faba_bean", "lupin", "adzuki", "bambara_nut", "fenugreek", "chili", "eggplant",
        "okra", "asparagus", "chive", "rhubarb", "artichoke", "taro", "water_chestnut", "water_caltrop",
        "lotus", "water_dropwort", "water_spinach", "arrowhead", "gorgon_nut", "winter_melon", "hops", "loofah",
        "bitter_melon", "snake_gourd", "yam", "malabar_spinach", "chayote", "bottle_gourd", "cantaloupe", "water_shield",
        "cardoon", "purslane", "pea", "cowpea", "common_bean", "winged_bean", "pigeon_pea", "strawberry",
        "beet", "carrot", "cassava", "garlic", "green_bean", "lentil", "melon", "onion",
        "peanut", "potato", "pumpkin", "radish", "red_bell_pepper", "soybean", "squash", "tomato",
        "yellow_bell_pepper"
    );

    private static final Set<String> SET = Set.copyOf(ALL);

    public static boolean has(String crop) {
        return SET.contains(crop);
    }

    /**
     * Returns the crop path for an exact A/TFC crop block ID, or null.
     * Wild crops and non-crop blocks are rejected by the namespace/path prefix.
     */
    public static String cropFromBlockId(String blockId) {
        if (blockId == null) {
            return null;
        }
        final String prefix;
        if (blockId.startsWith("tfcfarmingplus:crop/")) {
            prefix = "tfcfarmingplus:crop/";
        } else if (blockId.startsWith("tfc:crop/")) {
            prefix = "tfc:crop/";
        } else if (blockId.startsWith("tfcfarmingplus:wild_crop/")) {
            prefix = "tfcfarmingplus:wild_crop/";
        } else if (blockId.startsWith("tfc:wild_crop/")) {
            prefix = "tfc:wild_crop/";
        } else {
            return null;
        }
        final String crop = blockId.substring(prefix.length());
        return has(crop) ? crop : null;
    }

    private CropWasteCrops() {}
}
