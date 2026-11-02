package io.github.likexiang21.tfcplus.agriculture.common.crop;

/** Stable IDs for the 29 TFC crops and their seed item IDs. */
public enum TfcCropSpecies {
    ALFALFA("alfalfa"), BARLEY("barley"), BEET("beet"), CABBAGE("cabbage"), CANOLA("canola"),
    CARROT("carrot"), CASSAVA("cassava"), GARLIC("garlic"), GREEN_BEAN("green_bean"), JUTE("jute"),
    LENTIL("lentil"), MAIZE("maize"), MELON("melon"), OAT("oat"), ONION("onion"),
    PAPYRUS("papyrus"), PEANUT("peanut"), POTATO("potato"), PUMPKIN("pumpkin"), RADISH("radish"),
    RED_BELL_PEPPER("red_bell_pepper"), RICE("rice"), RYE("rye"), SOYBEAN("soybean"),
    SQUASH("squash"), SUGARCANE("sugarcane"), TOMATO("tomato"), WHEAT("wheat"),
    YELLOW_BELL_PEPPER("yellow_bell_pepper");

    private final String id;

    TfcCropSpecies(String id) {
        this.id = id;
    }

    public String id() {
        return id;
    }

    public String blockId() {
        return "tfc:crop/" + id;
    }

    public String seedItemId() {
        return "tfc:seeds/" + id;
    }

    public boolean alreadyHandledByGrainBundle() {
        return switch (id) {
            case "barley", "oat", "rice", "rye", "wheat", "maize" -> true;
            default -> false;
        };
    }

    public static TfcCropSpecies fromBlockId(String blockId) {
        for (TfcCropSpecies crop : values()) {
            if (crop.blockId().equals(blockId)) {
                return crop;
            }
        }
        return null;
    }
}
