package io.github.likexiang21.tfcplus.agriculture.common.crop;

import java.util.List;

/** Vegetative propagation stock items and their source crop/product. */
public final class PropagationStock {

    public record Entry(String species, String cropBlockId, String productItemId, String texture) {}

    private static final List<Entry> ALL = List.of(
        // CORM
        c("shallot", "tfcfarmingplus:crop/shallot", "tfcfarmingplus:food/shallot"),
        c("garlic", "tfc:crop/garlic", "tfc:food/garlic"),
        c("taro", "tfcfarmingplus:crop/taro", "tfcfarmingplus:food/taro"),
        c("water_chestnut", "tfcfarmingplus:crop/water_chestnut", "tfcfarmingplus:food/water_chestnut"),
        c("water_caltrop", "tfcfarmingplus:crop/water_caltrop", "tfcfarmingplus:food/water_caltrop"),
        c("arrowhead", "tfcfarmingplus:crop/arrowhead", "tfcfarmingplus:food/arrowhead"),
        c("gorgon_nut", "tfcfarmingplus:crop/gorgon_nut", "tfcfarmingplus:food/gorgon_nut"),
        // TUBER
        c("sunchoke", "tfcfarmingplus:crop/sunchoke", "tfcfarmingplus:food/sunchoke"),
        c("yacon", "tfcfarmingplus:crop/yacon", "tfcfarmingplus:food/yacon"),
        c("potato", "tfc:crop/potato", "tfc:food/potato"),
        c("yam", "tfcfarmingplus:crop/yam", "tfcfarmingplus:food/yam"),
        // RHIZOME
        c("ginger", "tfcfarmingplus:crop/ginger", "tfcfarmingplus:food/ginger"),
        c("turmeric", "tfcfarmingplus:crop/turmeric", "tfcfarmingplus:food/turmeric"),
        c("lotus", "tfcfarmingplus:crop/lotus", "tfcfarmingplus:food/lotus"),
        // CROWN
        c("artichoke", "tfcfarmingplus:crop/artichoke", "tfcfarmingplus:food/artichoke"),
        c("cardoon", "tfcfarmingplus:crop/cardoon", "tfcfarmingplus:food/cardoon"),
        c("rhubarb", "tfcfarmingplus:crop/rhubarb", "tfcfarmingplus:food/rhubarb"),
        c("asparagus", "tfcfarmingplus:crop/asparagus", "tfcfarmingplus:food/asparagus"),
        // DIVISION
        c("chive", "tfcfarmingplus:crop/chive", "tfcfarmingplus:food/chive"),
        c("cassava", "tfc:crop/cassava", "tfc:food/cassava"),
        // RUNNER
        c("strawberry", "tfcagricultureplus:crop/strawberry", "tfc:food/strawberry")
    );

    private static Entry c(String species, String crop, String product) {
        final String texture = product.startsWith("tfc:")
            ? "tfc:item/food/" + product.substring("tfc:food/".length())
            : "tfcfarmingplus:item/food/" + product.substring("tfcfarmingplus:food/".length());
        return new Entry(species, crop, product, texture);
    }

    public static List<Entry> all() {
        return ALL;
    }

    private PropagationStock() {}
}
