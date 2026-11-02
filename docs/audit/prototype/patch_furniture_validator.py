from pathlib import Path

p = Path("mod_rebuild/docs/audit/prototype/validate_kitchen_furniture.py")
s = p.read_text(encoding="utf-8")
s = s.replace(
    'loot = data / "loot_table/blocks/kitchen" / family / f"{wood}.json"',
    'loot = data / "loot_table/blocks" / family / f"{wood}.json"'
)
s = s.replace(
    'key = f"block.tfcagricultureplus.{block_id}"',
    'key = f"block.tfcagricultureplus.{family}.{wood}"'
)
p.write_text(s, encoding="utf-8")
print("patched")
