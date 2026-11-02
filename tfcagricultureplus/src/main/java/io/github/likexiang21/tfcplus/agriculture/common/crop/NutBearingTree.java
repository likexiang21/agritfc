package io.github.likexiang21.tfcplus.agriculture.common.crop;

import java.util.List;

/**
 * Existing-tree nut mapping used by the TFC leaves mixin.
 *
 * <p>One nut can be carried by several tree species (for example TFC chestnut plus AFC
 * hardy_chestnut/chinquapin). The leaf IDs are exact block IDs; no nonexistent TFC leaf is
 * silently invented.
 */
public enum NutBearingTree {
    OAK(List.of("tfc:wood/leaves/oak", "afc:wood/leaves/black_oak", "afc:wood/leaves/live_oak"),
        "tfcagricultureplus:acorn"),
    CHESTNUT(List.of("tfc:wood/leaves/chestnut", "afc:wood/leaves/hardy_chestnut", "afc:wood/leaves/chinquapin"),
        "tfcagricultureplus:chestnut"),
    PINE(List.of("tfc:wood/leaves/pine", "afc:wood/leaves/red_pine", "afc:wood/leaves/stone_pine",
        "afc:wood/leaves/huangshan_pine"),
        "tfcagricultureplus:pine_nut"),
    HICKORY(List.of("tfc:wood/leaves/hickory", "afc:wood/leaves/scrub_hickory"),
        "tfcagricultureplus:hickory_nut"),
    BEECH(List.of("afc:wood/leaves/beech", "afc:wood/leaves/black_beech", "afc:wood/leaves/rauli_beech"),
        "tfcagricultureplus:beechnut");

    private final List<String> leafBlockIds;
    private final String nutItemId;

    NutBearingTree(List<String> leafBlockIds, String nutItemId) {
        this.leafBlockIds = leafBlockIds;
        this.nutItemId = nutItemId;
    }

    public List<String> leafBlockIds() {
        return leafBlockIds;
    }

    public String nutItemId() {
        return nutItemId;
    }

    public String shellItemId() {
        return "tfcagricultureplus:nut_shell/" + nutItemId.substring(nutItemId.indexOf(':') + 1);
    }

    public static NutBearingTree fromLeafBlockId(String blockId) {
        for (NutBearingTree tree : values()) {
            if (tree.leafBlockIds.contains(blockId)) {
                return tree;
            }
        }
        return null;
    }
}
