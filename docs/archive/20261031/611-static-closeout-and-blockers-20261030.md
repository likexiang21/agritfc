# 611 静态工作收口与剩余阻塞评估

> 日期：2026-10-30
> 状态：**静态部分收口；剩余需要用户授权/设计**
> 约束：不实机、不推送、不伪造完成。

## 1. 静态审计结果

```text
json files 6484 / bad 0
lang en_us 1087 / zh_cn 1087 / missing 0 / extra 0
models 3690 / blockstates 539 / item_models 943
final_static_audit problems 0
```

当前 jar：

```text
2,919,188 bytes
SHA-256 3F5EDE5B3FFE427F4A5CA9279034273191C474AF7478F46BC5C44E23852D60B2
```

## 2. 已完成静态项

### P0

- 陶盘 knapping 唯一 pattern；
- 删除重复木碗/陶碗；
- 174 工作方块配方 + 173 有效 loot；
- 逐物种名称 + 木材/家具名称。

### P1

- 金属罐 19 个 fluid model + filled 名称 + JEI 信息页；
- 厨房 6 类过滤/堆叠/sink 水罐/玩家装水/潜行快速存取；
- 6 个家具模型差异化；
- Patchouli 10 entry/4 category + 14 spotlight + 厨房 6 crafting + 养蚕 1 crafting + 木工 5 spotlight；
- JEI 3 category + 409 in-world catalyst + 34 drying + 信息页。

### P2

- 82 物种繁殖分类 + 21 无性材料 + 耕地/水源放置；
- 种子处理湿草/堆肥/木灰/石灰；
- 木工 40 配方对照 + TFC 20 木材视觉对齐；
- 枯死灌木已按用户指令恢复 TFC 原版；
- 82 crop_waste + 10 bush_waste 图标映射。

### UI 轻量化

- 13 处 `displayClientMessage` 全部移除；
- 42×2 个 message 语言键删除；
- 锅死方法删除。

## 3. 剩余阻塞

### A. 必须实机

- OPEN-010：金属罐装入/倒出/图标变化；
- OPEN-012：JEI 页面/侧栏/recipe 数量；
- OPEN-003：快速存取/水槽交互；
- OPEN-004：204 配方/loot 实际掉落；
- OPEN-011：TFC 20 木材渲染/朝向；
- OPEN-008：手册排版/翻页。

用户此前明确：**暂不实机**。

### B. 需要新美术

- 香料 `spice/*`、`ground_spice/*` item 图标仍共用 `tfc:item/straw`；
- 坚果 `pistachio`/`nut_shell`/`ground_nut` 仍共用 `tfc:item/straw`；
- Patchouli 章节没有图片页。

用户此前明确：**不做大规模贴图重绘**。
小规模新图标/图片需要用户确认是否允许。

### C. 需要玩法设计

- 母株性状（产量/抗性/生长势 DataComponent）；
- 完整农艺：间苗、培土、搭架、打顶、除草、施肥的具体规则；
- 当前只有种子处理 3 阶段。

## 4. 结论

静态可做的部分已经做完；继续自动改代码只能产生无法验收的猜测实现。

需要用户选择：

1. **允许实机验证**：解除 OPEN-010/012/003/004/011/008 的阻塞；
2. **允许小规模新美术**：香料/坚果图标、手册图片页；或接受占位；
3. **给出母株性状/农艺规则**：或明确暂时不做。

在这些条件明确前，目标应保持阻塞，避免再次用“更漂亮的状态数字”冒充完成。
