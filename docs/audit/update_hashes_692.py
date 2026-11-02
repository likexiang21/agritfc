import pathlib

targets = [
    "mod_rebuild/docs/688-tfc-firmalife-no-exemption-20261031.md",
    "mod_rebuild/docs/689-tfc-firmalife-no-exemption-work-report-20261031.md",
    "mod_rebuild/docs/690-strict-eval-p0-p1-fixes-20261031.md",
    "mod_rebuild/docs/691-strict-eval-p0-p1-fixes-work-report-20261031.md",
]
new_size = "2,942,138"
new_hash = "38CD6A2E1366512C28A850E05C84A77341C53234D9D2A0A5AA6C4A619D69DD71"
old = [
    ("2,940,851", "D738B5177FB5E116C283ADA494B97330B1DA46B062B4499C328201A94ADC5AB1"),
    ("2,940,893", "97DD9B567FA13FF5AEFB7A87D102CBD331B5FFF9B2E9BFF57061903C38C08045"),
    ("2,940,378", "43F03191927A3EE9C71BF304E5DB95743D6A861E55CE3AD0D2BC9991F0318E8D"),
]
for name in targets:
    p = pathlib.Path(name)
    t = p.read_text(encoding="utf-8")
    for size, h in old:
        t = t.replace(size, new_size).replace(h, new_hash)
    p.write_text(t, encoding="utf-8")
    print("updated", p.name)
