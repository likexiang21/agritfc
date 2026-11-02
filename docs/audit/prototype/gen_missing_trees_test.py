from pathlib import Path

base = Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\saves\tfctest2\datapacks\runtime-missing-trees\data\runtime_missing_trees\function")
base.mkdir(parents=True, exist_ok=True)

species = [
    ("macadamia", "tfcagricultureplus:nut_sapling/macadamia", "tfcagricultureplus:nut_leaves/macadamia", 0),
    ("pimento", "tfcagricultureplus:spice_sapling/pimento", "tfcagricultureplus:spice_leaves/pimento", 8),
    ("clove", "tfcagricultureplus:spice_sapling/clove", "tfcagricultureplus:spice_leaves/clove", 16),
    ("nutmeg", "tfcagricultureplus:spice_sapling/nutmeg", "tfcagricultureplus:spice_leaves/nutmeg", 24),
    ("star_anise", "tfcagricultureplus:spice_sapling/star_anise", "tfcagricultureplus:spice_leaves/star_anise", 32),
]

place = ["say RUNTIME_MISSING_PLACE"]
check = ["say RUNTIME_MISSING_CHECK"]
for sid, sapling, leaf, x in species:
    place.append(f"execute as @a at @s run setblock ~{x} ~-1 ~ minecraft:dirt")
    place.append(f'execute as @a at @s run setblock ~{x} ~ ~ {sapling}')
    place.append(f'execute as @a at @s if block ~{x} ~ ~ {sapling} run say MISSING_PLACED_{sid.upper()}')
    check.append(f'execute as @a at @s if block ~{x} ~ ~ tfc:wood/log/oak run say MISSING_TRUNK_{sid.upper()}')
    check.append(f'execute as @a at @s if block ~{x} ~3 ~ {leaf} run say MISSING_LEAF3_{sid.upper()}')
    check.append(f'execute as @a at @s if block ~{x} ~4 ~ {leaf} run say MISSING_LEAF4_{sid.upper()}')

place.append("schedule function runtime_missing_trees:check 300t")
check.append("gamerule randomTickSpeed 3")
check.append("schedule function runtime_missing_trees:cleanup 3s")

base.joinpath("load.mcfunction").write_text(
    "say RUNTIME_MISSING_LOAD\ngamerule randomTickSpeed 1000\nschedule function runtime_missing_trees:place 10s\n",
    encoding="utf-8", newline="\n")
base.joinpath("place.mcfunction").write_text("\n".join(place) + "\n", encoding="utf-8", newline="\n")
base.joinpath("check.mcfunction").write_text("\n".join(check) + "\n", encoding="utf-8", newline="\n")
base.joinpath("cleanup.mcfunction").write_text("say RUNTIME_MISSING_DONE\n", encoding="utf-8", newline="\n")
print("generated", len(species))
