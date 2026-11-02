from pathlib import Path
import re

root = Path("mod_rebuild/tfcagricultureplus/src/main/java/io/github/likexiang21/tfcplus/agriculture/common/recipe")
problems = []
checked = 0
for p in root.rglob("*.java"):
    t = p.read_text(encoding="utf-8")
    if not re.search(r"\b(implements\s+Recipe<|extends\s+MixingBowlRecipe\b)", t):
        continue
    checked += 1
    if not re.search(r"boolean\s+isSpecial\s*\(\s*\)\s*\{\s*return\s+true\s*;", t):
        problems.append(str(p))

print("custom recipe classes", checked, "missing isSpecial=true", len(problems))
for p in problems:
    print("PROBLEM", p)
