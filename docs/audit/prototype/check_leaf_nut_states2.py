from pathlib import Path
import json

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets")
for ns in ("tfc", "afc"):
    d = root / ns / "blockstates/wood/leaves"
    if not d.exists():
        continue
    bad = []
    for p in d.glob("*.json"):
        obj = json.loads(p.read_text(encoding="utf-8"))
        states = set()
        def collect(x):
            if isinstance(x, dict):
                when = x.get("when")
                if isinstance(when, dict) and "nut_state" in when:
                    states.add(str(when["nut_state"]))
                for k, v in x.items():
                    if isinstance(k, str) and "nut_state=" in k:
                        states.add(k.split("nut_state=")[1].split(",")[0].split("}")[0])
                    collect(v)
            elif isinstance(x, list):
                for v in x:
                    collect(v)
        collect(obj)
        if states != {"0", "1", "2", "3"}:
            bad.append((p.name, sorted(states)))
    print(ns, "leaf files", len(list(d.glob("*.json"))), "bad", len(bad))
    for x in bad[:20]:
        print("BAD", x)
