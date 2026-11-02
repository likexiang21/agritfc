# 376 澳洲坚果专属树 P0-AR 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：macadamia B 树苗/树叶/worldgen；实机未完成。

## 1. 完成内容

- `NutTreeSpecies.MACADAMIA`；
- 树叶/树苗/模型/loot/配方；
- 32 变体树叶；
- worldgen feature ×3；
- biome modifier；
- 8 种坚果全部有来源/叶状态路径。

## 2. 验证

```text
PASS: 370 crop P0 checks
PASS: pistachio/cashew/macadamia tree resources
PASS: pistachio/cashew/macadamia tree worldgen resources
gradle compileJava
BUILD SUCCESSFUL
processResources BUILD SUCCESSFUL
```

## 3. 边界

- **未实机**；
- 树干仍为 TFC oak log；
- 不是 TFC 果树/嫁接体系；
- A macadamia 树叶来源仍并存；
- worldgen 群系复用蘑菇标签；
- 不能宣称坚果生态最终验收。

## 4. 下一批

1. 实机坚果树立；
2. 群系/密度平衡；
3. 专属木材；
4. 全量实机测试。
