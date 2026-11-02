import urllib.request
import re

url = "https://api-docs.deepseek.com/zh-cn/assets/js/1ce5519a.2f5af637.js"
s = urllib.request.urlopen(url, timeout=20).read().decode("utf-8", "ignore")
s = re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), s)
for pat in ["00:30", "08:30", "优惠", "错峰", "峰谷", "周末", "节假日", "空闲", "夜间"]:
    print("===", pat, "===")
    found = False
    for m in re.finditer(re.escape(pat), s):
        found = True
        print(s[max(0, m.start() - 160):m.start() + 260].replace("\n", " "))
        if found:
            break
    if not found:
        print("(not found)")
