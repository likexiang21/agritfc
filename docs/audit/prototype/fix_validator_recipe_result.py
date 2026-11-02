from pathlib import Path

p = Path("mod_rebuild/docs/audit/prototype/validate_crop_p0a.py")
t = p.read_text(encoding="utf-8")
old = '    result_id = data["result"]["stack"]["id"]'
new = '    result = data["result"]\n    result_id = result.get("id") or result["stack"]["id"]'
if old in t:
    t = t.replace(old, new, 1)
    p.write_text(t, encoding="utf-8")
    print("validator updated")
else:
    print("anchor missing")
