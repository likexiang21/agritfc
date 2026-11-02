from pathlib import Path
import json

assets = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfcagricultureplus")
models = {p.relative_to(assets / "models").with_suffix("").as_posix() for p in (assets / "models").rglob("*.json")}
problems = []
for p in (assets / "models").rglob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    parent = d.get("parent")
    if parent and parent.startswith("tfcagricultureplus:"):
        rel = parent.split(":", 1)[1]
        if rel not in models:
            problems.append((p.relative_to(assets / "models").as_posix(), parent))
print("missing local parents", len(problems))
for x in problems[:50]:
    print(x)
