from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
old = "## OPEN-007 农业育种/培育流程未按技术文档（用户 2026-10-29 第六个问题）\n\n**状态：recorded / 未处理**"
new = """## OPEN-007 农业育种/培育流程未按技术文档（用户 2026-10-29 第六个问题）

**状态：partially-fixed-static（P2-1，2026-10-29）/ 未实机**

- 新增 `CropPropagation`，8 种繁殖方式；
- 82 个 crop-waste 作物全部显式分类；
- 播种门改为：TFC 保持直播；A/B `SEED_DIRECT` 放行；其它方式取消并提示具体方法；
- 育苗盘仍是非直播物种的移栽路径；
- 仍未实现块茎/球茎/根茎/匍匐茎/冠芽/扦插物品链、母株性状、温湿度、农艺管理；
- 未实机。
- 证据：docs/528、529。"""
if old not in t:
    raise SystemExit("anchor missing")
t = t.replace(old, new, 1)
p.write_text(t, encoding="utf-8")
print("OPEN-007 updated")
