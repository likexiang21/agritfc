# 425 树苗支撑与生长定位 P0-BP 工作报告

> 日期：2026-10-29
> 状态：**支撑判定已修改；树生长未复测**
> 范围：Nut/Spice 树苗 mayPlaceOn 显式接受 dirt/grass。

## 1. 完成内容

- 定位树苗消失；
- 修改 `NutTreeSaplingBlock.mayPlaceOn`；
- 修改 `SpiceTreeSaplingBlock.mayPlaceOn`；
- 加入 `Blocks.DIRT` / `Blocks.GRASS_BLOCK`；
- `gradle build` 成功；
- 恢复测试环境。

## 2. 未完成

- **没有复测树苗是否保留**；
- **没有复测树干/树冠**；
- 没有确认随机刻是否推进 stage；
- 不能宣称树生长完成。

## 3. 证据

- 日志：`mod_rebuild/docs/audit/runtime-tree-player-20261029.log`
- 测试后已恢复旧 jar/options、删除数据包。

## 4. 下一批

1. 复测树苗 stage0/1/2；
2. 复测树干/树冠；
3. 若仍失败，检查 randomTick 与 growTree。
