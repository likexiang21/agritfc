# 419 实机生长/BE 验证 P0-BM 工作报告

> 日期：2026-10-29
> 状态：**生长/BE 验证部分通过；未推送、未提交远程**
> 范围：真实客户端 basil 生长、菌包 stage、育苗盘 stage；未做收获。

## 1. 完成内容

- 临时数据包 place/check；
- randomTickSpeed=1000；
- 验证：
  - `OK_BASIL_MATURE`；
  - `OK_MUSHROOM_BAG_STAGE2`；
  - `OK_NURSERY_STAGE2`；
- 修复 NurseryTray 空槽保存崩溃；
- 记录日志；
- 恢复旧 jar/options，删除数据包。

## 2. 验证

```text
OK_BASIL_MATURE
OK_MUSHROOM_BAG_STAGE2
OK_NURSERY_STAGE2
RUNTIME_GROWTH_DONE
```

## 3. 修复

`NurseryTrayBlockEntity.saveAdditional`：

```java
tag.put("seed", seed.isEmpty() ? new CompoundTag() : seed.save(registries));
```

## 4. 边界

- 未验证坚果幼树（check 坐标错误）；
- 未验证收获/移栽/菌包产出；
- randomTickSpeed 非正常；
- 数据合并绕过玩家交互；
- 测试后已恢复环境。

## 5. 下一批

1. 修正树冠 check；
2. 玩家破坏/收获；
3. 育苗盘/菌包交互；
4. 全量验收。
