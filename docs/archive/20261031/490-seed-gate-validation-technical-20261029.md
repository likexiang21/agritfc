# 490 TFC 直接播种/A-B 育苗门实机复测 P0-CW 技术分析

> 日期：2026-10-29
> 目标：复测 P0-CV 修复后的播种门行为。
> 约束：不推送；不伪造；调试命令为临时测试入口。

## 1. 测试

干净存档：

- TFC farmland + `tfc:seeds/wheat`；
- minecraft farmland + A `tfcfarmingplus:seeds/napa_cabbage`；
- minecraft farmland + B `tfcagricultureplus:seeds/strawberry`；
- 玩家 survival；
- 临时 `tfcplusdebug_use_with` 使用对应种子；
- 检查上方方块。

## 2. 实机结果

```text
GATE_TFC_WHEAT_OK
GATE_A_NAPA_AIR
GATE_B_STRAWBERRY_AIR
```

- TFC wheat 直接播种成功；
- A napa 种子被取消，未放置作物；
- B strawberry 种子被取消，未放置作物。

## 3. 结论

P0-CV 修复生效：

- TFC 走原直接播种；
- A/B 走育苗盘→移栽。

## 4. 未验证

- TFC/A/B 全部种子逐一；
- TFC 29 收获覆盖与直接播种组合；
- 旧存档。
