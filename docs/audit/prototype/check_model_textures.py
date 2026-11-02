from pathlib import Path
import json

assets = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus")
textures = {p.relative_to(assets / "textures").with_suffix("").as_posix() for p in (assets / "textures").rglob("*.png")}
problems = []

def walk(obj, where):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "texture" and isinstance(v, str) and v.startswith("tfcagricultureplus:"):
                rel = v.split(":", 1)[1]
                if rel not in textures:
                    problems.append((where, "missing texture", v))
            walk(v, where)
    elif isinstance(obj, list):
        for v in obj:
            walk(v, where)

for p in (assets / "models").rglob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    walk(d, p.relative_to(assets / "models").as_posix())

print("B texture refs missing", len(problems))
for x in problems[:80]:
    print("PROBLEM", x)
