package io.github.likexiang21.tfcplus.agriculture.common.crop;

/**
 * Standalone prototype for the P0 crop-yield invariants.
 *
 * <p>Compile/run without Minecraft:
 * <pre>
 * javac -encoding UTF-8 -d &lt;tmp&gt; CropYieldLedger.java GrainCrop.java CropYieldProto.java
 * java -cp &lt;tmp&gt; io.github.likexiang21.tfcplus.agriculture.common.crop.CropYieldProto
 * </pre>
 * Exits non-zero on any failed assertion.
 */
public final class CropYieldProto {

    private static int checks = 0;

    public static void main(String[] args) {
        check(new CropYieldLedger("millet", 8, 1, 3, 2).isValid(), "valid millet ledger");
        check(!new CropYieldLedger("bad-seed", 8, 0, 3, 2).isValid(), "reject seedBack=0");
        check(!new CropYieldLedger("bad-mass", 4, 1, 5, 2).isValid(), "reject processed>raw");
        check(!new CropYieldLedger("bad-by", 8, 1, 3, 0).isValid(), "reject byproduct=0");

        check(GrainCrop.values().length == 16, "16 grain crops");
        for (GrainCrop crop : GrainCrop.values()) {
            check(crop.bundlePath().equals("grain_bundle/" + crop.id()), "bundle path " + crop.id());
            check(crop.bundleId().startsWith("tfcagricultureplus:grain_bundle/"), "bundle id " + crop.id());
            check(!crop.grainItemId().isBlank(), "grain item " + crop.id());
            check(!crop.seedItemId().isBlank(), "seed item " + crop.id());
            check(crop.cropBlockId().endsWith("/" + crop.id()), "crop block " + crop.id());
            check(!crop.isMature(crop.maxAge() - 1), "immature " + crop.id());
            check(crop.isMature(crop.maxAge()), "mature " + crop.id());
        }
        check(java.util.Arrays.stream(GrainCrop.values()).filter(c -> c.source() == GrainCrop.Source.A).count() == 10,
            "10 A grains");
        check(java.util.Arrays.stream(GrainCrop.values()).filter(GrainCrop::isTfc).count() == 6,
            "6 TFC grains");
        check(GrainCrop.fromCropBlockId("tfcfarmingplus:crop/millet") == GrainCrop.MILLET,
            "reverse A millet");
        check(GrainCrop.fromCropBlockId("tfc:crop/wheat") == GrainCrop.WHEAT,
            "reverse TFC wheat");
        check(GrainCrop.fromCropBlockId("tfcfarmingplus:wild_crop/millet") == null,
            "reject wild crop");
        check(GrainCrop.fromCropBlockId("tfc:crop/beet") == null,
            "reject non-grain crop");

        check(CropWasteCrops.ALL.size() == 82, "82 crop-waste crops");
        check(CropWasteCrops.has("spinach"), "spinach has waste");
        check(!CropWasteCrops.has("wheat"), "wheat has no crop waste");
        check("spinach".equals(CropWasteCrops.cropFromBlockId("tfcfarmingplus:crop/spinach")),
            "waste reverse A spinach");
        check("cabbage".equals(CropWasteCrops.cropFromBlockId("tfc:crop/cabbage")),
            "waste reverse TFC cabbage");
        check(CropWasteCrops.cropFromBlockId("tfc:crop/wheat") == null,
            "wheat not in waste table");

        check(MushroomSpecies.values().length == 15, "15 mushroom species");
        check(MushroomSpecies.naturalOnlySpecies().size() == 4, "4 natural-only mushrooms");
        check(MushroomSpecies.cultivableSpecies().size() == 11, "11 cultivable mushrooms");
        check(MushroomSpecies.PORCINI.naturalOnly(), "porcini natural-only");
        check(MushroomSpecies.OYSTER.blockPath().equals("wild_mushroom/oyster"), "oyster wild block path");
        check(MushroomSpecies.fromBlockId("tfcagricultureplus:wild_mushroom/oyster") == MushroomSpecies.OYSTER,
            "mushroom reverse oyster");
        check(MushroomSpecies.fromBlockId("tfcagricultureplus:wild_mushroom/porcini") == MushroomSpecies.PORCINI,
            "mushroom reverse porcini");
        check(MushroomSpecies.fromBlockId("tfcagricultureplus:wild_mushroom/not_a_mushroom") == null,
            "mushroom reject unknown");

        check(NutBearingTree.values().length == 5, "5 nut-bearing tree groups");
        check(NutBearingTree.fromLeafBlockId("tfc:wood/leaves/oak") == NutBearingTree.OAK, "oak nut mapping");
        check(NutBearingTree.fromLeafBlockId("afc:wood/leaves/beech") == NutBearingTree.BEECH, "beech nut mapping");
        check(NutBearingTree.fromLeafBlockId("tfc:wood/leaves/beech") == null, "beech is not TFC leaf");
        check(NutBearingTree.OAK.shellItemId().equals("tfcagricultureplus:nut_shell/acorn"),
            "oak shell item id");

        check(SpiceSpecies.values().length == 20, "20 spice species");
        for (SpiceSpecies spice : SpiceSpecies.values()) {
            check(!spice.form().isBlank(), "spice form " + spice.id());
            check(spice.cropPath().equals("spice_crop/" + spice.id()), "spice crop path " + spice.id());
            check(spice.seedPath().equals("spice_seed/" + spice.id()), "spice seed path " + spice.id());
            check(spice.productPath().equals("spice/" + spice.id()), "spice product path " + spice.id());
            check(spice.wastePath().equals("spice_waste/" + spice.id()), "spice waste path " + spice.id());
            check(spice.groundPath().equals("ground_spice/" + spice.id()), "spice ground path " + spice.id());
            check(spice.seedYield() == ("corm".equals(spice.form()) ? 2 : 1), "spice seed yield " + spice.id());
            check(spice.productYield() == (("tree".equals(spice.form()) || "root".equals(spice.form())) ? 2 : 1),
                "spice product yield " + spice.id());
            if ("corm".equals(spice.form())) {
                check(spice.cormPath().equals("spice_corm/" + spice.id()), "spice corm path " + spice.id());
            }
            if ("root".equals(spice.form())) {
                check(spice.rootPath().equals("spice_root/" + spice.id()), "spice root path " + spice.id());
            }
        }
        check(BushSpecies.values().length == 10, "10 TFC bushes");
        check(BushSpecies.fromTfcBushBlockId("tfc:plant/blackberry_bush") == BushSpecies.BLACKBERRY,
            "blackberry bush mapping");
        check(BushSpecies.fromTfcBushBlockId("tfc:plant/strawberry_bush") == null,
            "strawberry not TFC bush");

        check(NutTreeSpecies.values().length == 3, "3 B nut trees");
        for (NutTreeSpecies tree : NutTreeSpecies.values()) {
            check(tree.leafPath().equals("nut_leaves/" + tree.id()), "nut leaves path " + tree.id());
            check(tree.saplingPath().equals("nut_sapling/" + tree.id()), "nut sapling path " + tree.id());
        }
        check(SpiceTreeSpecies.values().length == 5, "5 spice tree species");
        for (SpiceTreeSpecies tree : SpiceTreeSpecies.values()) {
            check(tree.leafPath().equals("spice_leaves/" + tree.id()), "spice leaves path " + tree.id());
            check(tree.saplingPath().equals("spice_sapling/" + tree.id()), "spice sapling path " + tree.id());
        }

        check(SeedTreatments.next("").equals(SeedTreatments.SOAKED), "seed treatment soaked");
        check(SeedTreatments.next(SeedTreatments.SOAKED).equals(SeedTreatments.GERMINATED), "seed treatment germinated");
        check(SeedTreatments.next(SeedTreatments.GERMINATED).equals(SeedTreatments.DRESSED), "seed treatment dressed");
        check(SeedTreatments.isSeedItemId("tfc:seeds/wheat"), "TFC seed detection");
        check(SeedTreatments.isSeedItemId("tfcfarmingplus:seeds/millet"), "A seed detection");
        check(!SeedTreatments.isSeedItemId("tfc:food/wheat"), "food is not a seed");
        check(SeedTreatments.boostForStage(SeedTreatments.SOAKED) == 1, "soaked boost");
        check(SeedTreatments.boostForStage(SeedTreatments.GERMINATED) == 2, "germinated boost");
        check(SeedTreatments.boostForStage(SeedTreatments.DRESSED) == 3, "dressed boost");
        check(SeedTreatments.nurseryTicks("") == 1200, "nursery untreated ticks");
        check(SeedTreatments.nurseryTicks(SeedTreatments.SOAKED) == 1000, "nursery soaked ticks");
        check(SeedTreatments.nurseryTicks(SeedTreatments.GERMINATED) == 800, "nursery germinated ticks");
        check(SeedTreatments.nurseryTicks(SeedTreatments.DRESSED) == 600, "nursery dressed ticks");

        check(TfcCropSpecies.values().length == 29, "29 TFC crop species");
        check(TfcCropSpecies.fromBlockId("tfc:crop/tomato") == TfcCropSpecies.TOMATO, "TFC tomato mapping");
        check(TfcCropSpecies.fromBlockId("tfc:crop/wheat").alreadyHandledByGrainBundle(),
            "TFC wheat grain handled by bundle");
        check(!TfcCropSpecies.fromBlockId("tfc:crop/tomato").alreadyHandledByGrainBundle(),
            "TFC tomato not grain bundle");

        check(MushroomSpecies.cultivableSpecies().size() == 11, "11 cultivable mushrooms");
        check(MushroomSpecies.naturalOnlySpecies().size() == 4, "4 natural-only mushrooms");
        for (MushroomSpecies mushroom : MushroomSpecies.cultivableSpecies()) {
            check(mushroom.cultivationTicks() > 0, "mushroom bag ticks " + mushroom.id());
            check(mushroom.bagMinYield() > 0, "mushroom bag min " + mushroom.id());
            check(mushroom.bagMaxYield() >= mushroom.bagMinYield(), "mushroom bag max " + mushroom.id());
            check(mushroom.bagTemperatureOk(mushroom.preferredTemperature()),
                "mushroom bag preferred temperature " + mushroom.id());
        }
        for (MushroomSpecies mushroom : MushroomSpecies.naturalOnlySpecies()) {
            check(mushroom.cultivationTicks() == 0, "natural-only mushroom ticks " + mushroom.id());
        }

        System.out.println("PASS: " + checks + " crop P0 checks");
    }

    private static void check(boolean condition, String label) {
        checks++;
        if (!condition) {
            System.err.println("FAIL: " + label);
            System.exit(1);
        }
    }

    private CropYieldProto() {}
}
