from pathlib import Path

p = Path("mod_rebuild/tfcagricultureplus/src/main/java/io/github/likexiang21/tfcplus/agriculture/TFCAgriculturePlus.java")
t = p.read_text(encoding="utf-8")
needle = '''            for (final ItemEntity item : player.level().getEntitiesOfClass(ItemEntity.class,
                player.getBoundingBox().inflate(6.0))) {
                TFCAgriculturePlus.LOGGER.info("[TFC Agriculture Plus] dropped {} x{}",
                    item.getItem().getItem(), item.getItem().getCount());
            }
'''
replacement = needle + '''            for (final var stack : player.getInventory().items) {
                if (!stack.isEmpty()) {
                    TFCAgriculturePlus.LOGGER.info("[TFC Agriculture Plus] inventory {} x{}",
                        stack.getItem(), stack.getCount());
                }
            }
'''
if "inventory {} x{}" not in t:
    t = t.replace(needle, replacement, 1)
p.write_text(t, encoding="utf-8")
print("inventory log added")
