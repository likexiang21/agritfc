from pathlib import Path

base = Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\saves\tfctest2\datapacks\runtime-all-trees\data\runtime_all_trees\function")
base.mkdir(parents=True, exist_ok=True)

# (id, sapling, leaf, x)
species = [
    ("pistachio", "tfcagricultureplus:nut_sapling/pistachio", "tfcagricultureplus:nut_leaves/pistachio", 2),
    ("cashew", "tfcagricultureplus:nut_sapling/cashew", "tfcagricultureplus:nut_leaves/cashew", 4),
    ("macadamia", "tfcagricultureplus:nut_sapling/macadamia", "tfcagricultureplus:nut_leaves/macadamia", 6),
    ("pimento", "tfcagricultureplus:spice_sapling/pimento", "tfcagricultureplus:spice_leaves/pimento", 8),
    ("cinnamon", "tfcagricultureplus:spice_sapling/cinnamon", "tfcagricultureplus:spice_leaves/cinnamon", 10),
    ("clove", "tfcagricultureplus:spice_sapling/clove", "tfcagricultureplus:spice_leaves/clove", 12),
    ("nutmeg", "tfcagricultureplus:spice_sapling/nutmeg", "tfcagricultureplus:spice_leaves/nutmeg", 14),
    ("star_anise", "tfcagricultureplus:spice_sapling/star_anise", "tfcagricultureplus:spice_leaves/star_anise", 16),
]

place = ["say RUNTIME_ALL_TREES_PLACE"]
check = ["say RUNTIME_ALL_TREES_CHECK"]
for sid, sapling, leaf, x in species:
    place.append(f"execute as @a at @s run setblock ~{x} ~-1 ~ minecraft:dirt")
    place.append(f'execute as @a at @s run setblock ~{x} ~ ~ {sapling}')
    place.append(f'execute as @a at @s if block ~{x} ~ ~ {sapling} run say PLACED_{sid.upper()}')
    check.append(f'execute as @a at @s if block ~{x} ~ ~ tfc:wood/log/oak run say TRUNK_{sid.upper()}')
    check.append(f'execute as @a at @s if block ~{x} ~3 ~ {leaf} run say LEAF3_{sid.upper()}')
    check.append(f'execute as @a at @s if block ~{x} ~4 ~ {leaf} run say LEAF4_{sid.upper()}')

place.append("schedule function runtime_all_trees:check 300t")
check.append("gamerule randomTickSpeed 3")
check.append("schedule function runtime_all_trees:cleanup 3s")

base.joinpath("load.mcfunction").write_text(
    "say RUNTIME_ALL_TREES_LOAD\ngamerule randomTickSpeed 1000\nschedule function runtime_all_trees:place 10s\n",
    encoding="utf-8", newline="\n")
base.joinpath("place.mcfunction").write_text("\n".join(place) + "\n", encoding="utf-8", newline="\n")
base.joinpath("check.mcfunction").write_text("\n".join(check) + "\n", encoding="utf-8", newline="\n")
base.joinpath("cleanup.mcfunction").write_text("say RUNTIME_ALL_TREES_DONE\n", encoding="utf-8", newline="\n")
print("generated", len(species), "species")
