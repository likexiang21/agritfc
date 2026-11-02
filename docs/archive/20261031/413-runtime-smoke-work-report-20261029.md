# 413 实机注册烟测 P0-BJ 工作报告

> 日期：2026-10-29
> 状态：**部分注册确认；未推送、未提交远程**
> 范围：真实客户端 load function 烟测；未做玩法测试。

## 1. 完成内容

- 创建临时数据包；
- load function 放置 B 方块并检查；
- summon B 物品；
- 进入 `tfctest` 世界；
- 收集服务器日志；
- 删除测试数据包；
- 恢复游戏 B jar/options。

## 2. 成功标记

```text
OK_BLOCK_NURSERY
OK_BLOCK_STRAWBERRY
OK_BLOCK_NUT_LEAVES
OK_BLOCK_SPICE_LEAVES
OK_BLOCK_WILD_MUSHROOM
OK_BLOCK_TRELLIS
OK_BLOCK_NUT_SAPLING
OK_BLOCK_MUSHROOM_BAG
OK_BLOCK_SAFFRON
```

## 3. 未确认

```text
spice_crop/basil
spice_crop/cardamom
spice_sapling/cinnamon
```

原因优先怀疑支撑方块/canSurvive 与 load 时区块状态，而不是注册失败；需后续用正确 farmland/dirt 再测。

## 4. 证据

- 日志：`mod_rebuild/docs/audit/runtime-smoke-20261029.log`
- 世界加载：`Total time to load game and open world was 78.05458 seconds`
- 无 Registry loading errors；
- 无 B recipe parse error。

## 5. 边界

- **不是玩法验收**；
- 只验证命令/注册层；
- 未种植/生长/收获；
- 未验证 GUI/树苗生长/菌包；
- 测试数据包已删除；
- 不能宣称目标完成。
