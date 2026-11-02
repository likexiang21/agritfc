from pathlib import Path
import re

p = Path("mod_rebuild/docs/291-crop-system-complete-modification-20261028.md")
t = p.read_text(encoding="utf-8")

# --- Replace 4.1.2 table with only actual waste crops. ---
start = t.find("#### 4.1.2")
end = t.find("#### 4.1.3")
if start < 0 or end < 0:
    raise SystemExit("4.1.2/4.1.3 missing")
section = t[start:end]
rows = []
for line in section.splitlines():
    m = re.match(r"\| `([^`]+)` \| ([^|]+) \| `tfcagricultureplus:crop_waste/[^`]+` \|([^|]*)\|([^|]*)\|([^|]*)\|$", line)
    if m:
        rows.append([m.group(1), m.group(2).strip(), m.group(3).strip(), m.group(4).strip(), m.group(5).strip()])
if len(rows) != 116:
    raise SystemExit(f"waste rows parse {len(rows)}")

a_no_groups = {"A·谷物/禾本", "A·油料", "A·纤维"}
tfc_no_groups = {"TFC·谷物/禾本", "TFC·纤维", "TFC·水生/纤维", "TFC·叶菜/饲草"}
a_no_crops = {"agave", "jobs_tears", "wild_rice_stem"}
tfc_no_crops = {"canola"}
def has_waste(crop, sg):
    if sg.startswith("A·"):
        return sg not in a_no_groups and crop not in a_no_crops
    return sg not in tfc_no_groups and crop not in tfc_no_crops

yes = [r for r in rows if has_waste(r[0], r[1])]
no = [r for r in rows if not has_waste(r[0], r[1])]
if len(yes) != 81:
    raise SystemExit(f"expected 81 A/TFC waste rows, got {len(yes)}")

new = []
new.append("#### 4.1.2 废枝叶：不是所有作物都有，按实际加工判定\n")
new.append("“废枝叶”只是统称，**不是每个作物都产**。只有实际加工步骤产生外叶/茎/藤/荚/皮渣的作物才有 `crop_waste/<crop>`；没有该副产的作物不造物品，走各自副产（straw / oil cake / shives / shell / spent substrate）。\n")
new.append("| 作物 | 来源/组 | 废枝叶物品 | 类型 | 堆肥档 | 其它出口 |\n")
new.append("|---|---|---|---|---|---|\n")
for r in yes:
    new.append(f"| `{r[0]}` | {r[1]} | `tfcagricultureplus:crop_waste/{r[0]}` | {r[2]} | `{r[3]}` | {r[4]} |\n")
new.append("\n**不产 crop_waste 的 A/TFC 作物**（共 35 条）：\n")
new.append("- A 谷物 12、A 油料 4、A 纤维 4、`agave`、`jobs_tears`、`wild_rice_stem`；\n")
new.append("- TFC 谷物 7、`jute`、`papyrus`、`alfalfa`、`canola`；\n")
new.append("- 这些作物的副产是：谷物 bundle/wet_grass/straw、油料 stalk/oil cake、纤维 shives、坚果 shell、蘑菇 spent substrate。\n")
new.append("\n**B 新增 43 条的废料**：香料 20 条有 `crop_waste/<spice>`（计入 101）；坚果 8 条只有 `nut_shell`；蘑菇 15 条只有 `spent_substrate`，二者都不算绿色废枝叶。因此 **crop_waste 总数 = 81（A/TFC）+ 20（B 香料）= 101**，不是 159。\n")
new.append("\n**没有实际废枝叶的作物不设物品**；`crop_waste` 不得成为“每作物一个死物品”的指标。\n")
t = t[:start] + "".join(new) + "\n" + t[end:]

# --- Replace 4.1.3 table: A 10 only, TFC 6 optional. ---
start = t.find("#### 4.1.3")
end = t.find("#### 4.1.4")
if start < 0 or end < 0:
    raise SystemExit("4.1.3/4.1.4 missing")
new = '''#### 4.1.3 谷物捆：湿草的加工来源

不是所有谷物都直接掉散粒：**A 的 10 种长秆谷物先收谷物捆，再脱粒**，脱粒副产才是湿草。

| 作物 | 来源 | 谷物捆物品 | 收获 | 脱粒 | 湿草/干燥 | 备注 |
|---|---|---|---|---|---|---|
| `millet` | A | `tfcagricultureplus:grain_bundle/millet` | 成熟收获 → 1–2 捆 + 种子 | 脱粒 → 谷粒 + 1–2 `wet_grass` | `wet_grass` 1:1 晒干 → `tfc:straw` | 主产品仍是谷粒 |
| `foxtail_millet` | A | `tfcagricultureplus:grain_bundle/foxtail_millet` | 同上 | 同上 | 同上 | 主产品仍是谷粒 |
| `fonio` | A | `tfcagricultureplus:grain_bundle/fonio` | 同上 | 同上 | 同上 | 主产品仍是谷粒 |
| `spelt` | A | `tfcagricultureplus:grain_bundle/spelt` | 同上 | 同上 | 同上 | 主产品仍是谷粒 |
| `emmer` | A | `tfcagricultureplus:grain_bundle/emmer` | 同上 | 同上 | 同上 | 主产品仍是谷粒 |
| `einkorn` | A | `tfcagricultureplus:grain_bundle/einkorn` | 同上 | 同上 | 同上 | 主产品仍是谷粒 |
| `pearl_millet` | A | `tfcagricultureplus:grain_bundle/pearl_millet` | 同上 | 同上 | 同上 | 主产品仍是谷粒 |
| `finger_millet` | A | `tfcagricultureplus:grain_bundle/finger_millet` | 同上 | 同上 | 同上 | 主产品仍是谷粒 |
| `sorghum` | A | `tfcagricultureplus:grain_bundle/sorghum` | 同上 | 同上 | 同上 | 主产品仍是谷粒 |
| `jobs_tears` | A | `tfcagricultureplus:grain_bundle/jobs_tears` | 同上 | 同上 | 同上 | 主产品仍是谷粒 |

**TFC 6 种谷物**（barley/oat/rice/rye/wheat/maize）：P1 **保持 TFC 原 raw，不启用 bundle**；湿草仅来自野草收割/未成熟补偿。bundle 版本列为可选数据包，P2 后评估。

非谷物捆：`buckwheat` / `amaranth` / `quinoa`；TFC `sugarcane` 不属于谷物捆。

'''
t = t[:start] + new + t[end:]

# --- Stats and cross references. ---
t = t.replace("| 副产物物品 | 1 + 16 + 159 | `wet_grass`（1）+ `grain_bundle/<crop>`（16）+ `crop_waste/<crop>`（159）；坚果壳/菌渣另算 |",
              "| 副产物物品 | 1 + 10 + 101 | `wet_grass`（1）+ `grain_bundle/<crop>`（10，A 谷物）+ `crop_waste/<crop>`（101，按实际副产）；坚果壳/菌渣另算 |")
t = t.replace("废枝叶产 **逐作物 `crop_waste/<crop>`**；谷物按 4.1.3 先出谷物捆，脱粒产 `wet_grass`",
              "废枝叶只有实际产出的作物才有 **`crop_waste/<crop>`**；A 谷物按 4.1.3 先出谷物捆，脱粒产 `wet_grass`")

# --- Section 13 replace with decisions link + table. ---
start = t.find("## 13.")
end = t.find("## 14.", start)
if start < 0 or end < 0:
    raise SystemExit("section13/14 missing")
new13 = '''## 13. 未决问题与解决方案

完整分析与决定见 [292 未决问题决策](292-crop-open-issues-decisions-20261028.md)。摘要：

| # | 决定 |
|---:|---|
| 1 | A 以实际 87 种为准，旧文档 86 废弃 |
| 2 | 分四层：A 87/B 43 全链；TFC 29 资源+加工；TFC 10 灌木资源+采收/加工 |
| 3 | 育苗/移栽用 B 自有方块 + `in_world`，不改 TFC |
| 4 | 种子处理用 DataComponent，不新增 116 个处理种子物品 |
| 5 | P1 不改 TFC/A raw；TFC raw 永久保持；A raw 调整仅可选数据包 |
| 6 | A 删除 6 个 TFC cabbage 模型，B 接管 29 作物 TFC 资源；补 EUPL 通知 |
| 7 | 双主产共用一个 raw ledger，不重复计 raw |
| 8 | 20 香料分草本/灌木/乔木/攀援藤/球茎五类 |
| 9 | 15 蘑菇分菌包 11 / 菌根树根 3 / 林下菌床 1；菌包 4 stage |
| 10 | 5 坚果挂已有树，3 坚果用新 B 树；不重复 A/AFC 坚果 |
| 11 | A 10 谷物 bundle→wet_grass；TFC 6 谷物默认 raw 不变，bundle 可选 |
| 12 | 废枝叶按实际加工；仅 101 条有 `crop_waste`，其余走 straw/cake/shives/shell/spent substrate |
| 13 | TFC 10 灌木只做资源+采收/加工；草莓已是 A 普通作物 |

## 14. 来源文档
'''
t = t[:start] + new13 + t[end + len("## 14. 来源文档"):]
# If source block insertion leaves heading correctly; check later.

# Avoid double source heading if any.
t = t.replace("## 14. 来源文档\n## 14. 来源文档\n", "## 14. 来源文档\n")

p.write_text(t, encoding="utf-8")
print("291 corrected: waste only actual, bundle A only, decisions added")
