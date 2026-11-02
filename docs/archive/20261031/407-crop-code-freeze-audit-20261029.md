# 407 作物系统代码冻结审计（2026-10-29）

> 目的：在 48 轮后给出代码级证据与剩余风险；**不伪造完成，不标记目标完成**。
> 结论：**代码级功能覆盖已基本闭合；实机验证仍未执行**。

## 1. 本轮最终构建

```text
gradle build
BUILD SUCCESSFUL

PASS: 99 item models, 2 lang files, 17 recipes, 102 crop_waste,
      10 bush_waste, 15 wild mushrooms, 4-stage bag, 79 nut leaf states,
      15 spice crops, 5 spice trees, 20 ground spices, 8 ground nuts,
      8 nut shells, tags valid

PASS: nursery tray + seedling resources
PASS: spice trellis resources
PASS: spice corm resources
PASS: strawberry crop resources
PASS: A 86 crops + B strawberry = 87; TFC 29 crops/seed models
PASS: pistachio/cashew tree resources
PASS: pistachio/cashew tree worldgen resources
PASS: spice tree resources
PASS: spice tree worldgen resources
PASS: spice root resources
PASS: tree biome tags

BAD_REFS 0
PASS: 393 crop P0 checks
```

## 2. 代码级覆盖

### A 87 / TFC 29

- 统一收获替换；
- 种子返还；
- 谷物 bundle；
- crop_waste；
- 直接播种拦截；
- 育苗盘/幼苗/移栽；
- 双格清理；
- 创造模式保护。

### TFC 10 灌木

- 废枝；
- 破坏采收；
- 空手右键采收；
- 创造模式保护。

### B 43

| 类别 | 状态 |
|---|---|
| 20 香料 | 15 crop + 5 tree；产品/废枝叶/粉/种子/树苗 |
| 8 坚果 | 叶状态/树/壳/粉/燃料；3 个 B 树 + 5 既有树 |
| 15 蘑菇 | worldgen/15 物种/菌包/温度/时间/产量/次数 |

### 其他

- wet_grass + 16 grain bundles；
- 102 crop_waste；
- 蘑菇 worldgen/菌包；
- 坚果叶状态；
- 树木 worldgen/群系标签；
- 数据引用的 BAD_REFS 0。

## 3. 仍未完成

1. **实机验证**：当前环境缺少 `.tooling`，无法启动验证客户端；
2. **旧资源清理**：5 个 tree form 的旧 `spice_crop`/`spice_seed` 资源仍在 resources，但已不再注册；
3. **逐作物 loot/产量核对**：没有 159 条实机或动态数据包回归；
4. **视觉/文本**：多数临时 TFC 贴图，未重绘；
5. **平衡**：温度、产量、时间、概率均未实机平衡；
6. **159 条最终验收**：未做。

## 4. 结论

代码级实现已经远超最早的骨架，但：

- **没有实机证据**；
- **没有完成最终验收**；
- 因此**不标记目标完成**；
- 不推送。

下一步必须：

1. 补齐验证环境（`.tooling`）。
2. 统一实机测试：注册/资源加载、种植、育苗、收获、菌包、树、创造模式。
3. 根据实机结果修 bug 与平衡。
4. 清理未使用旧资源。
