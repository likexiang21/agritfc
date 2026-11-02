# 459 玩家破坏收获链实机验证 P0-CG 工作报告

> 日期：2026-10-29
> 状态：**成熟 basil/strawberry 玩家破坏收获成功；未推送、未提交远程**
> 范围：临时 debug 命令 + 干净存档实机。

## 1. 完成内容

- 添加临时 `tfcplusdebug_harvest` 命令；
- 真实玩家破坏成熟作物；
- 检查方块/掉落物；
- 记录日志；
- 恢复环境。

## 2. 结果

```text
HARVEST_BASIL_GONE
HARVEST_STRAWBERRY_GONE
HARVEST_ITEM_NEAR
```

## 3. 结论

BlockEvent.BreakEvent 玩家破坏路径与 B 收获处理已执行；作物被移除并出现掉落物。

## 4. 未完成

- 掉落物 ID/数量；
- 种子/废枝叶 top-up 全量；
- 未成熟保护；
- creative 分支；
- 全部物种。

## 5. 风险

- 调试命令必须发布前移除/加开关；
- 不能宣称收获链全部完成。
