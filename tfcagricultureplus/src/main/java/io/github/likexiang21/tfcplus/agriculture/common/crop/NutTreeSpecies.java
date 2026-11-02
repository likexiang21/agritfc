package io.github.likexiang21.tfcplus.agriculture.common.crop;

/** Dedicated B nut trees for the two nuts without an existing TFC/AFC tree mapping. */
public enum NutTreeSpecies {
    PISTACHIO("pistachio", "tfcagricultureplus:pistachio", "tfcagricultureplus:nut_shell/pistachio"),
    CASHEW("cashew", "tfcagricultureplus:cashew", "tfcagricultureplus:nut_shell/cashew"),
    MACADAMIA("macadamia", "tfcagricultureplus:macadamia", "tfcagricultureplus:nut_shell/macadamia");

    private final String id;
    private final String nutItemId;
    private final String shellItemId;

    NutTreeSpecies(String id, String nutItemId, String shellItemId) {
        this.id = id;
        this.nutItemId = nutItemId;
        this.shellItemId = shellItemId;
    }

    public String id() {
        return id;
    }

    public String leafPath() {
        return "nut_leaves/" + id;
    }

    public String saplingPath() {
        return "nut_sapling/" + id;
    }

    public String nutItemId() {
        return nutItemId;
    }

    public String shellItemId() {
        return shellItemId;
    }
}
