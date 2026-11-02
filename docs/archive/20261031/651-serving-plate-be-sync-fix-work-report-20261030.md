# 651 盘子方块实体客户端同步修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- `ServingPlateBlockEntity` 从 `BlockEntity` 改为 `TFCBlockEntity`；
- `setPlateStack` / `clearPlate` 使用 `markForSync()`；
- 客户端可通过 `getUpdateTag`/`getUpdatePacket` 收到 `plateStack`；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,926,030 bytes
SHA-256 3128FA41B9A30EEECB2B39CE22084F76656DB5CF41AF8540BCC9978CC549EC39
```

## 3. 未做

- 未实机；
- 未验证盘子重载/破坏/换菜全路径。
