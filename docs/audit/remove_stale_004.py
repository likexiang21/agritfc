from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
lines = p.read_text(encoding="utf-8").splitlines()
# Remove the stale block immediately after the new OPEN-004 status.
for i, line in enumerate(lines):
    if line.startswith("- 已补 174 个工作方块配方 + 174 个 loot table"):
        del lines[i:i + 5]
        break
p.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("removed stale block")
