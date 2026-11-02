package io.github.likexiang21.tfcplus.agriculture.common.crop;

/** Tree-form spices that get a real B tree block (TFC oak trunk + B spice leaves). */
public enum SpiceTreeSpecies {
    PIMENTO("pimento"),
    CINNAMON("cinnamon"),
    CLOVE("clove"),
    NUTMEG("nutmeg"),
    STAR_ANISE("star_anise");

    private final String id;

    SpiceTreeSpecies(String id) {
        this.id = id;
    }

    public String id() {
        return id;
    }

    public String leafPath() {
        return "spice_leaves/" + id;
    }

    public String saplingPath() {
        return "spice_sapling/" + id;
    }

    public String productItemId() {
        return "tfcagricultureplus:spice/" + id;
    }
}
