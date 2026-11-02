from pathlib import Path

p = Path("mod_rebuild/tfcagricultureplus/src/main/java/io/github/likexiang21/tfcplus/agriculture/TFCAgriculturePlus.java")
t = p.read_text(encoding="utf-8")
if "net.minecraft.world.entity.item.ItemEntity" not in t:
    t = t.replace(
        "import net.minecraft.world.phys.BlockHitResult;\n" if "import net.minecraft.world.phys.BlockHitResult;" in t else "import net.minecraft.server.level.ServerPlayer;\n",
        ("import net.minecraft.world.entity.item.ItemEntity;\nimport net.minecraft.server.level.ServerPlayer;\n" if "BlockHitResult" not in t else "import net.minecraft.world.phys.BlockHitResult;\nimport net.minecraft.world.entity.item.ItemEntity;\n"),
        1,
    )
needle = '''            })));
    }

'''
addition = '''            })));
        event.getDispatcher().register(Commands.literal("tfcplusdebug_drops").executes(context -> {
            final ServerPlayer player = context.getSource().getPlayerOrException();
            for (final ItemEntity item : player.level().getEntitiesOfClass(ItemEntity.class,
                player.getBoundingBox().inflate(6.0))) {
                TFCAgriculturePlus.LOGGER.info("[TFC Agriculture Plus] dropped {} x{}",
                    item.getItem().getItem(), item.getItem().getCount());
            }
            return 1;
        }));
    }

'''
if "tfcplusdebug_drops" not in t:
    t = t.replace(needle, addition, 1)
p.write_text(t, encoding="utf-8")
print("drops command added")
