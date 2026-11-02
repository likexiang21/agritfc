package io.github.likexiang21.tfcplus.agriculture.common.crop;

import java.util.ArrayList;
import java.util.List;

/** Static prototype: every crop-waste species must have an explicit propagation method. */
public final class CropPropagationProto {
    public static void main(String[] args) {
        final List<String> missing = new ArrayList<>();
        for (final String crop : CropWasteCrops.ALL) {
            if (!CropPropagation.isExplicitlyClassified(crop)) {
                missing.add(crop);
            }
        }
        System.out.println("species=" + CropWasteCrops.ALL.size()
            + " classified=" + CropPropagation.classifiedSpecies().size()
            + " missing=" + missing.size());
        if (!missing.isEmpty()) {
            System.out.println("MISSING " + missing);
            throw new IllegalStateException("unclassified crop species: " + missing);
        }
        System.out.println("PASS: all crop-waste species have explicit propagation");
    }

    private CropPropagationProto() {}
}
