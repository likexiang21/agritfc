from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-024 自定义树叶未重写 codec（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `SpiceTreeLeavesBlock` / `NutLeavesBlock` 构造函数带 species，但继承 `LeavesBlock.codec()`；
- codec 被使用时可能构造普通 `LeavesBlock`，丢失 species 类型；
- 修复：两个类重写 `public MapCodec<? extends LeavesBlock> codec()`；
- build 成功；
- 证据：docs/642、643。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-024 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [641-interaction-cancel-guards-fix-work-report-20261030.md](641-interaction-cancel-guards-fix-work-report-20261030.md) | 交互入口取消检查修复工作报告 |"
add = "\n| [642-custom-leaves-codec-fix-20261030.md](642-custom-leaves-codec-fix-20261030.md) | 自定义树叶 codec 修复 |\n| [643-custom-leaves-codec-fix-work-report-20261030.md](643-custom-leaves-codec-fix-work-report-20261030.md) | 自定义树叶 codec 修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
