# 434 树苗定时生长实机验证 P0-BU 技术分析

> 日期：2026-10-29
> 目标：验证 P0-BT 的 `onPlace`→`scheduleTick`→`tick` 树苗生长是否在真实客户端生效。
> 约束：不推送；不伪造；测试后恢复环境。

## 1. 测试

临时数据包 `runtime-tree-sched`：

- `randomTickSpeed=1000`；
- 玩家旁放：
  - farmland + basil；
  - dirt + nut_sapling/pistachio；
  - dirt + spice_sapling/cinnamon；
- 60t 和 300t 检查。

## 2. 结果

60t：

```text
SCHED_NUT_TRUNK60
SCHED_SPICE_TRUNK60
```

300t：

```text
SCHED_NUT_TRUNK300
SCHED_SPICE_TRUNK300
```

结论：**两棵树苗在 60 tick 内已生成树干原木**，说明 scheduled tick 生长路径生效。

## 3. 未通过项

没有：

```text
SCHED_NUT_CANOPY60/300
SCHED_SPICE_CANOPY60/300
SCHED_BASIL_MATURE60/300
```

- canopy 检查坐标假设可能错误；
- basil 的 check 可能因玩家移动/相对坐标失效；
- 树的完整树冠没有确认。

## 4. 结论

- **树苗生长代码已在实机产生树干**；
- 树冠未确认；
- 作物对照未确认；
- 不能宣称树完整完成。

## 5. 证据

```text
mod_rebuild/docs/audit/runtime-tree-sched-20261029.log
```
