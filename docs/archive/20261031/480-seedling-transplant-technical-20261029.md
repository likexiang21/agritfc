# 480 育苗移栽实机验证 P0-CR 技术分析

> 日期：2026-10-29
> 目标：完成育苗盘→seedling→移栽到耕地的实机链路。
> 约束：不推送；不伪造；调试命令为临时测试入口。

## 1. 测试

干净存档：

- 育苗盘 stage2 + strawberry seed；
- 玩家 use 育苗盘；
- `tfcplusdebug_plant_seedling ~4 ~-1 ~`，目标是耕地本身；
- 检查 ~4 ~ 上方。

## 2. 实机结果

```text
SEEDLING2_PLANTED
SEEDLING2_FARMLAND
inventory tfcagricultureplus:seedling x1
```

- 耕地上方出现 `tfcagricultureplus:crop/strawberry`；
- 耕地仍在；
- 背包仍剩余 1 个 seedling（因为本轮产出了多个）；
- 无 ERROR。

## 3. 结论

**育苗盘 → seedling → 移栽到耕地**的实机链路打通。

## 4. 未验证

- 移栽后 growth/成熟/收获；
- seedling NBT 保留；
- 不同种子作物；
- 旧存档。
