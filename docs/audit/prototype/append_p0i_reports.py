from pathlib import Path

p = Path("mod_rebuild/docs/305-spice-crop-technical-20261028.md")
t = p.read_text(encoding="utf-8")
t = t.replace("3. spice crop_waste 20 条，补齐 102；\n4. 实机验证；\n5. TFC 29 剩余覆盖。",
"""3. spice crop_waste 20 条，补齐 102；
4. 实机验证；
5. TFC 29 剩余覆盖。

## 6. P0-I：20 条 spice crop_waste（追加）

已实现：

- 20 个 `spice_waste/<spice>` 物品；
- 20 个 item model + en/zh 语言；
- 9 个草本香料废料进 `compost_greens/high`，11 个其余香料进 `medium`；
- `CropWasteHandler` 增加 `tfcagricultureplus:spice_crop/<id>` 分支：
  - 只在该 CropBlock 最大 age 时掉落；
  - 不取消原作物破坏；
  - 原产物/种子仍按 loot table 掉落；
- 总 crop_waste：82（A/TFC）+ 20（B 香料）= **102**。

校验：

```text
PASS: 242 crop P0 checks
PASS: 99 item models, 2 lang files, 17 recipes, 102 crop_waste,
      15 wild mushrooms, 4-stage bag, 79 nut leaf states, 20 spice crops, tags valid
```

边界：香料仍是普通 CropBlock，树/藤/球茎形态未实现；未实机。
""")
p.write_text(t, encoding="utf-8")

p = Path("mod_rebuild/docs/306-spice-crop-work-report-20261028.md")
t = p.read_text(encoding="utf-8")
t = t.replace("3. spice crop_waste 20 条；\n4. 实机验证；\n5. TFC 29 剩余覆盖。",
"""3. spice crop_waste 20 条；
4. 实机验证；
5. TFC 29 剩余覆盖。

## 5. P0-I：20 条香料废枝叶（追加）

- 新增 20 个 `spice_waste/<spice>` 物品；
- 草本类 9 条进 `compost_greens/high`；
- 其他 11 条进 `compost_greens/medium`；
- `CropWasteHandler` 已接 `tfcagricultureplus:spice_crop/<id>`；
- 只在该作物最大 age 掉落，不取消原破坏；
- crop_waste 总量达到 **102**。

验证：

```text
PASS: 242 crop P0 checks
PASS: 99 item models, 2 lang files, 17 recipes, 102 crop_waste,
      15 wild mushrooms, 4-stage bag, 79 nut leaf states, 20 spice crops, tags valid
```

边界：未实机验证；香料形态仍未细分。
""")
p.write_text(t, encoding="utf-8")
print("P0-I appended")
