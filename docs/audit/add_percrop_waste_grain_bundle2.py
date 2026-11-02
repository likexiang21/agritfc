from pathlib import Path

p = Path("mod_rebuild/docs/audit/generate_291_v2.py")
lines = p.read_text(encoding="utf-8").splitlines()

start = next(i for i, l in enumerate(lines) if "#### 4.1.2" in l)
end = next(i for i, l in enumerate(lines) if l.strip().startswith('lines.append("\\n## 5.') or '## 5. 培育链' in l)
new = [
    'lines.append("#### 4.1.2 废枝叶：逐作物专属，不设通用 `green_waste`\\n")',
    'lines.append("“废枝叶”只是统称，**每个作物一个专属物品 `crop_waste/<crop>`**（可带来源/等级组件），不能用一个通用 `green_waste` 覆盖全部。下面逐作物给出类型、堆肥档与其它出口。\\n")',
    'lines.append("| 作物 | 来源/组 | 废枝叶物品 | 类型 | 堆肥档 | 其它出口 |\\n")',
    'lines.append("|---|---|---|---|---|---|\\n")',
    'for crop, sg in order:',
    '    group = sg.split("·", 1)[1] if "·" in sg else sg',
    '    wtype, tag, alt = waste_override.get(crop, waste_group.get(group, ("茎叶残渣", "tfc:compost_greens/medium", "堆肥/饲料")))',
    '    lines.append(f"| `{crop}` | {sg} | `tfcagricultureplus:crop_waste/{crop}` | {wtype} | `{tag}` | {alt} |\\n")',
    'lines.append("#### 4.1.3 谷物捆：湿草的加工来源\\n")',
    'lines.append("不是所有谷物都直接掉散粒：**长秆谷物先收谷物捆，再脱粒**，脱粒副产才是湿草。\\n")',
    'lines.append("| 作物 | 来源 | 谷物捆物品 | 收获 | 脱粒 | 湿草/干燥 | 备注 |\\n")',
    'lines.append("|---|---|---|---|---|---|---|\\n")',
    'for crop in bundle_crops:',
    '    src = "A" if crop in a_group_of else "TFC"',
    '    lines.append(f"| `{crop}` | {src} | `tfcagricultureplus:grain_bundle/{crop}` | 成熟收获 → 1–2 捆 + 种子 | 脱粒 → 谷粒 + 1–2 `wet_grass` | `wet_grass` 1:1 晒干 → `tfc:straw` | 主产品仍是谷粒；不减少原有谷粒 |\\n")',
    'lines.append("非谷物捆（直接脱粒/散粒）：" + " · ".join("`" + c + "`" for c in non_bundle_grains) + "；TFC 的 `sugarcane` 不属于谷物捆。\\n")',
    'lines.append("**TFC 兼容**：TFC 29 的 raw 掉落建议不直接改；TFC 谷物是否改走 `grain_bundle` 需单批确认。A 的谷物捆可先落地。\\n")',
    'lines.append("#### 4.1.4 废枝叶/菌渣/坚果壳的边界\\n")',
    'lines.append("- 坚果壳：不是“绿色废枝叶”，单独走 `nut_shell/<nut>` → `tfc:compost_browns/high` / 燃料；\\n")',
    'lines.append("- 蘑菇废菌包：`spent_substrate` → `tfc:compost_browns/medium` / 堆肥，不算绿色枝叶；\\n")',
    'lines.append("- 香料废枝叶：`crop_waste/<spice>` → 按 `compost_greens/high|medium`；\\n")',
    'lines.append("- 所有 `crop_waste` / 壳 / 菌渣必须有堆肥/饲料/燃料/纸至少一个出口，不得造死物品。\\n")',
    '',
]
lines[start:end] = new
p.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("section replaced", start, end)
