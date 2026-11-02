package io.github.likexiang21.tfcplus.agriculture.common.crop;

/** The 20 B spice species from docs/291 §9.1. The form is data used for future specialization. */
public enum SpiceSpecies {
    BASIL("basil", "herb"),
    BAY_LAUREL("bay_laurel", "shrub"),
    CARDAMOM("cardamom", "root"),
    CILANTRO("cilantro", "herb"),
    CUMIN("cumin", "herb"),
    OREGANO("oregano", "herb"),
    PIMENTO("pimento", "tree"),
    VANILLA("vanilla", "vine"),
    BLACK_PEPPER("black_pepper", "vine"),
    CINNAMON("cinnamon", "tree"),
    CLOVE("clove", "tree"),
    NUTMEG("nutmeg", "tree"),
    SAFFRON("saffron", "corm"),
    STAR_ANISE("star_anise", "tree"),
    ROSEMARY("rosemary", "shrub"),
    THYME("thyme", "herb"),
    SAGE("sage", "herb"),
    DILL("dill", "herb"),
    FENNEL("fennel", "herb"),
    MUSTARD("mustard", "herb");

    private final String id;
    private final String form;

    SpiceSpecies(String id, String form) {
        this.id = id;
        this.form = form;
    }

    public String id() {
        return id;
    }

    public String form() {
        return form;
    }

    public String cropPath() {
        return "spice_crop/" + id;
    }

    public String seedPath() {
        return "spice_seed/" + id;
    }

    public String productPath() {
        return "spice/" + id;
    }

    public String wastePath() {
        return "spice_waste/" + id;
    }

    public String groundPath() {
        return "ground_spice/" + id;
    }

    public String cormPath() {
        return "spice_corm/" + id;
    }

    public String rootPath() {
        return "spice_root/" + id;
    }

    /** Corm spices propagate vegetatively and guarantee an extra seed item at harvest. */
    public int seedYield() {
        return "corm".equals(form) ? 2 : 1;
    }

    /** Tree/root forms yield one extra product at harvest; herb/vine/corm stay at one. */
    public int productYield() {
        return switch (form) {
            case "tree", "root" -> 2;
            default -> 1;
        };
    }
}
