from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")
old = '''### 静态检查

在 B 的 `src/main/resources` 中未找到：

- `assets/tfcagricultureplus/patchouli_books/**`
- `data/tfcagricultureplus/patchouli_books/**`

B 自身没有专属 Patchouli 书页资源；现有手册内容来自外部/前置模组或缺失。

结论：需要确认书 ID，并补 B 自己的可读书页；当前不可读问题成立。
'''
new = '''### 修正后的静态检查

上一版记录“B 没有任何 Patchouli 资源”是**错误**的，现修正：

B 实际有手册资源，但挂在 TFC 的 field guide 下：

```text
assets/tfc/patchouli_books/field_guide/
  en_us/categories/agriculture_plus_kitchen.json
  en_us/categories/agriculture_plus_silkworm.json
  en_us/categories/agriculture_plus_woodwork.json
  en_us/entries/agriculture_plus_kitchen/intro.json
  en_us/entries/agriculture_plus_silkworm/intro.json
  en_us/entries/agriculture_plus_woodwork/intro.json
  ... zh_cn 同名 6 个文件
```

即只有 **3 个旧主题**：厨房、养蚕、木工。

### 真正问题

1. **没有作物系统章节**：
   - 无 crop / 香料 / 坚果 / 蘑菇 / 育苗 / 菌包 / 树叶状态页面；
   - 用户无法从手册理解本次农业重做。
2. 现有 3 个条目是超长纯文本块（`patchouli:text` 连续多页），没有：
   - 配方页；
   - 图/表；
   - 分步骤；
   - 与 JEI/REI 的联动。
3. 部分条目图标/分类可能指向旧内容，容易被用户理解为“手册不可读”。

结论：手册不是“没有资源”，而是**内容覆盖严重不足、可读性差**；用户批评成立。
'''
if old not in t:
    raise SystemExit("anchor missing")
t = t.replace(old, new, 1)
p.write_text(t, encoding="utf-8")
print("OPEN-008 corrected")
