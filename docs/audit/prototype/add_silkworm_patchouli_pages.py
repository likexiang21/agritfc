import json
from pathlib import Path

root = Path("mod_rebuild/tfcagricultureplus/src/main/resources/assets/tfc/patchouli_books/field_guide")
for lang, idx in (("en_us", 0), ("zh_cn", 1)):
    p = root / lang / "entries/agriculture_plus_silkworm/intro.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    if not any(page.get("recipe") == "tfcagricultureplus:workstations/silkworm_rack" for page in d["pages"]):
        d["pages"].append({
            "type": "patchouli:crafting",
            "recipe": "tfcagricultureplus:workstations/silkworm_rack",
            "text": ("Rack recipe: 3 lumber over two rod posts and a lumber base." if idx == 0 else "养蚕架配方：3 份木材、两根木棍立柱和底部木材。")
        })
    spot = [
        {"item": "tfcagricultureplus:silkworm_egg", "title": "Silkworm egg" if idx == 0 else "蚕卵",
         "text": ("Hatches after 2–4 suitable days at 0 °C or warmer." if idx == 0 else "在 0 °C 以上适宜温度经过 2–4 天孵化。")},
        {"item": "tfcagricultureplus:cocoon", "title": "Cocoon" if idx == 0 else "蚕茧",
         "text": ("Produced at 10 growth points; becomes an adult after 3–5 suitable days." if idx == 0 else "10 点成长后结茧；再经过 3–5 个适宜日变成成虫。")},
        {"item": "tfcagricultureplus:silk_thread", "title": "Silk thread" if idx == 0 else "蚕丝线",
         "text": ("Cooked silkworm + spindle → one silk thread; 24 threads weave one silk cloth." if idx == 0 else "熟蚕 + 纺锤 → 1 根蚕丝线；24 根织成 1 块丝绸。")},
    ]
    existing = {page.get("item") for page in d["pages"] if page.get("type") == "patchouli:spotlight"}
    for page in spot:
        if page["item"] not in existing:
            d["pages"].append({"type": "patchouli:spotlight", **page})
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("silkworm pages updated")
