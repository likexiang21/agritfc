from pathlib import Path

base = Path(r"D:\111\最强服务器\.minecraft\versions\Essential TerraFirmaCraft (TFC)\saves\tfctest\datapacks\runtime-tree-clear\data\runtime_tree_clear\function")
base.mkdir(parents=True, exist_ok=True)
lines = ["say RUNTIME_CLEAR_CLEAR"]
for y in range(1, 9):
    for x in range(-1, 8):
        for z in range(-3, 4):
            lines.append(f"execute as @a at @s run setblock ~{x} ~{y} ~{z} minecraft:air")
base.joinpath("clear.mcfunction").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
print("clear commands", len(lines) - 1)
