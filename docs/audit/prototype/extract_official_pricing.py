import urllib.request
import re
from pathlib import Path

url = "https://api-docs.deepseek.com/zh-cn/assets/js/1ce5519a.2f5af637.js"
s = urllib.request.urlopen(url, timeout=20).read().decode("utf-8", "ignore")
s = re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), s)
needles = ["低谷时段价格为", "高峰时段", "周末", "中国法定节假日", "9:00", "14:00", "18:00"]
out = []
for needle in needles:
    idx = s.find(needle)
    out.append(f"=== {needle} @ {idx} ===")
    if idx >= 0:
        out.append(s[max(0, idx - 300):idx + 700].replace("\\n", " "))
Path("mod_rebuild/docs/audit/official-pricing-snippet.txt").write_text("\n".join(out), encoding="utf-8")
print("written")
