package io.github.likexiang21.tfcplus.agriculture.client.renderer;

import com.mojang.blaze3d.vertex.PoseStack;
import com.mojang.math.Axis;
import java.util.function.Function;
import net.minecraft.client.Minecraft;
import net.minecraft.client.renderer.MultiBufferSource;
import net.minecraft.client.renderer.blockentity.BlockEntityRenderer;
import net.minecraft.world.item.ItemDisplayContext;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.block.entity.BlockEntity;

/**
 * Small generic renderer for the one-item devices that previously had no BER.
 * The item is drawn as a floating "fixed" item above the block face.
 */
public final class SimpleItemBlockEntityRenderer<T extends BlockEntity> implements BlockEntityRenderer<T> {

    private final Function<T, ItemStack> getter;

    public SimpleItemBlockEntityRenderer(Function<T, ItemStack> getter) {
        this.getter = getter;
    }

    @Override
    public void render(T blockEntity, float partialTick, PoseStack pose,
                       MultiBufferSource buffer, int packedLight, int packedOverlay) {
        final ItemStack stack = getter.apply(blockEntity);
        if (stack.isEmpty()) {
            return;
        }
        pose.pushPose();
        pose.translate(0.5D, 0.75D, 0.5D);
        pose.mulPose(Axis.YP.rotationDegrees(45.0F));
        pose.scale(0.45F, 0.45F, 0.45F);
        Minecraft.getInstance().getItemRenderer().renderStatic(
            stack, ItemDisplayContext.FIXED, packedLight, packedOverlay,
            pose, buffer, blockEntity.getLevel(), 0);
        pose.popPose();
    }
}
