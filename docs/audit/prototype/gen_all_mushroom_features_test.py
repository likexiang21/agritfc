from pathlib import Path

base = Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\saves\tfctest2\datapacks\runtime-all-mushroom-features\data\runtime_all_mushroom_features\function")
base.mkdir(parents=True, exist_ok=True)
src = Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus/worldgen/placed_feature")
features = sorted(p.stem for p in src.glob("wild_mushroom_*.json"))
place = ["say RUNTIME_ALL_MUSHROOM_PLACE"]
check = ["say RUNTIME_ALL_MUSHROOM_CHECK"]
for i, feature in enumerate(features):
    suffix = feature[len("wild_mushroom_"):]
    x = i * 2
    place.append(f"execute as @a at @s run setblock ~{x} ~-1 ~ minecraft:grass_block")
    place.append(f"execute as @a at @s run place feature tfcagricultureplus:{feature} ~{x} ~ ~")
    place.append(f"execute as @a at @s if block ~{x} ~ ~ tfcagricultureplus:wild_mushroom/{suffix} run say MUSHROOM_OK_{suffix.upper()}")
    check.append(f"execute as @a at @s if block ~{x} ~ ~ tfcagricultureplus:wild_mushroom/{suffix} run say MUSHROOM_STILL_{suffix.upper()}")
place.append("schedule function runtime_all_mushroom_features:check 20t")
check.append("schedule function runtime_all_mushroom_features:cleanup 3s")

base.joinpath("load.mcfunction").write_text(
    "say RUNTIME_ALL_MUSHROOM_LOAD\nschedule function runtime_all_mushroom_features:place 10s\n",
    encoding="utf-8", newline="\n")
base.joinpath("place.mcfunction").write_text("\n".join(place) + "\n", encoding="utf-8", newline="\n")
base.joinpath("check.mcfunction").write_text("\n".join(check) + "\n", encoding="utf-8", newline="\n")
base.joinpath("cleanup.mcfunction").write_text("say RUNTIME_ALL_MUSHROOM_DONE\n", encoding="utf-8", newline="\n")
print("features", len(features))
