from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
t += """

## OPEN-025 香料作物形状子类未重写 codec（2026-10-30 代码筛查）

**状态：fixed-static / 待实机**

- `SpiceCropBlocks` 的 6 个形状类继承 `CropBlock.codec()`，会退化成普通 CropBlock；
- 修复：6 个类分别重写 `public MapCodec<? extends CropBlock> codec()`；
- build 成功；
- 证据：docs/644、645。
"""
p.write_text(t, encoding="utf-8")
print("OPEN-025 appended")

p = Path("mod_rebuild/docs/README.md")
t = p.read_text(encoding="utf-8")
needle = "| [643-custom-leaves-codec-fix-work-report-20261030.md](643-custom-leaves-codec-fix-work-report-20261030.md) | 自定义树叶 codec 修复工作报告 |"
add = "\n| [644-spice-crop-codec-fix-20261030.md](644-spice-crop-codec-fix-20261030.md) | 香料作物形状子类 codec 修复 |\n| [645-spice-crop-codec-fix-work-report-20261030.md](645-spice-crop-codec-fix-work-report-20261030.md) | 香料作物形状子类 codec 修复工作报告 |"
if needle in t:
    t = t.replace(needle, needle + add)
    p.write_text(t, encoding="utf-8")
    print("docs links updated")
