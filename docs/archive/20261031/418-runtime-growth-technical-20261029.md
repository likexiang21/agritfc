# 418 实机生长/BE 验证 P0-BM 技术分析

> 日期：2026-10-29
> 目标：在真实客户端验证 B 作物生长、菌包殖民、育苗盘 state 推进。
> 约束：不推送；不伪造；测试后恢复环境。

## 1. 测试方式

临时数据包 `runtime-crop-growth`：

- load：`gamerule randomTickSpeed 1000`，5 秒后 place；
- place：
  - farmland + `spice_crop/basil`；
  - dirt + `nut_sapling/pistachio`；
  - `mushroom_bag` + `data merge {species:"oyster",progress:1199}`；
  - `nursery_tray` + `data merge {seed:...,progress:1200,required_ticks:1200}`；
- 300 tick 后 check；
- cleanup 恢复 randomTickSpeed 3。

## 2. 运行时发现并修复的 bug

### NurseryTrayBlockEntity 空槽保存崩溃

日志：

```text
java.lang.IllegalStateException: Cannot encode empty ItemStack
  at NurseryTrayBlockEntity.saveAdditional(NurseryTrayBlockEntity.java:99)
```

原因：`seed.save(registries)` 对空 ItemStack 编码。

修复：

```java
tag.put("seed", seed.isEmpty() ? new CompoundTag() : seed.save(registries));
```

修复后该错误消失。

## 3. 通过项

```text
OK_BASIL_MATURE
OK_MUSHROOM_BAG_STAGE2
OK_NURSERY_STAGE2
```

- 香料作物从 age0 长到 age7；
- 菌包从 stage1 推进到 stage2；
- 育苗盘从 stage1 推进到 stage2；
- 无 Registry/Recipe 错误；
- 无 NurseryTray 保存错误。

## 4. 未验证

- 坚果树的 check 坐标在树苗位置，而树冠在顶部，所以没有 `OK_NUT_TREE_LEAVES`；
- 不能据此判失败；
- 未验证收获；
- 未验证幼苗移栽/菌包收获。

## 5. 证据

```text
mod_rebuild/docs/audit/runtime-growth-20261029.log
```

## 6. 风险

- 生长测试用 randomTickSpeed=1000，不是正常速率；
- 数据合并直接设置 BE，不经过玩家交互；
- 树冠检查位置错误；
- 测试后已恢复环境。
