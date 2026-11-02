from pathlib import Path
repls = [
 ("- Firmalife 其余 12 个 plant 方块（fig/cocoa/grapes/pineapple/nightshade）仍无 B 侧钩子；", "- Firmalife 其余 12+2 个植物方块已由 694/695 接入 B 废枝叶；"),
 ("- Firmalife 其余 12 个 plant 方块仍无 B 侧钩子；", "- Firmalife 其余 12+2 个植物方块已由 694/695 接入 B 废枝叶；"),
 ("- Firmalife 剩余 12 个 `firmalife:plant/*`（fig/cocoa/grape/pineapple/nightshade）和 2 个葡萄种植方块仍无 B 侧钩子；", "- Firmalife 剩余 12+2 个植物方块已由 694/695 接入 B 废枝叶；"),
]
for name in ("690-strict-eval-p0-p1-fixes-20261031.md","691-strict-eval-p0-p1-fixes-work-report-20261031.md","692-strict-eval-p0-2-tfc-farmland-20261031.md"):
 p=Path("mod_rebuild/docs")/name; t=p.read_text(encoding="utf-8")
 for a,b in repls: t=t.replace(a,b)
 p.write_text(t,encoding="utf-8"); print(name)
