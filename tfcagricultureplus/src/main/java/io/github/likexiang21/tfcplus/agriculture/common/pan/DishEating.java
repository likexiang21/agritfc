package io.github.likexiang21.tfcplus.agriculture.common.pan;

import io.github.likexiang21.tfcplus.agriculture.common.blockentity.ServingPlateBlockEntity;
import net.dries007.tfc.common.component.food.FoodCapability;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;

/** Shared serving logic for plates. */
public final class DishEating {
    public static boolean eatFromPlateBlock(Player player, ServingPlateBlockEntity plate) {
        if (!(player instanceof ServerPlayer)) return true;
        final ItemStack stack = plate.plateStack();
        final PanDishData dish = PanDishData.read(stack);
        if (dish == null || FoodCapability.isRotten(stack)) return false;
        if (player.getAbilities().instabuild) return true;
        consumeOne(player, stack);
        if (dish.servings() <= 1) {
            plate.clearPlate();
        } else {
            final PanDishData rest = new PanDishData(dish.servings() - 1, dish.score(), dish.food(),
                dish.category(), dish.oil(), dish.ingredients());
            PanDishData.write(stack, rest);
            plate.setPlateStack(stack);
        }
        return true;
    }

    /** Called from Item.finishUsingItem. Returns the resulting stack (with one fewer serving). */
    public static ItemStack finishItemUse(Player player, ItemStack stack) {
        final PanDishData dish = PanDishData.read(stack);
        if (dish == null || FoodCapability.isRotten(stack)) return stack;
        if (player.getAbilities().instabuild) return stack;
        consumeOne(player, stack);
        final PanDishData rest = dish.servings() <= 1 ? null
            : new PanDishData(dish.servings() - 1, dish.score(), dish.food(),
                dish.category(), dish.oil(), dish.ingredients());

        // A stack can hold several filled plates. Split one plate off instead of
        // mutating the whole stack (the old setCount(1) deleted every other plate).
        if (stack.getCount() > 1) {
            final ItemStack single = stack.copyWithCount(1);
            stack.shrink(1);
            if (rest == null) {
                PanDishData.clear(single);
            } else {
                PanDishData.write(single, rest);
            }
            if (!player.getInventory().add(single)) player.drop(single, false);
            return stack;
        }

        if (rest == null) {
            PanDishData.clear(stack);
        } else {
            PanDishData.write(stack, rest);
        }
        stack.setCount(1);
        return stack;
    }

    private static void consumeOne(Player player, ItemStack stack) {
        // Use the normal Minecraft eating path. TFC's food component hooks are
        // responsible for nutrition, comparison with IPlayerInfo.eat is intentionally avoided.
        if (player instanceof ServerPlayer && !player.getAbilities().instabuild) {
            player.eat(player.level(), stack.copyWithCount(1));
        }
    }

    public static Item emptyPlateItem(ItemStack stack) {
        return stack.getItem();
    }

    private DishEating() {}
}
