import pathlib, json, re
base = pathlib.Path(r"mod_rebuild/tfcagricultureplus/src/main/resources/data/tfcagricultureplus")
for key in ("adult_silkworm", "silkworm_egg", "silkworm", "cocoon", "silk_thread", "silk_cloth", "spice_corm", "spice_root", "propagation_stock"):
    print("====", key)
    for p in base.rglob("*.json"):
        s=p.read_text(encoding="utf-8", errors="ignore")
        if key in s:
            # print only output lines
            for line in s.splitlines():
                if key in line and ('id' in line or 'item' in line or 'name' in line):
                    print(p.relative_to(base), line.strip())
