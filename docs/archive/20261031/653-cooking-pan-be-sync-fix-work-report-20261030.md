# 653 锅方块实体同步修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- `CookingPanBlockEntity.sync()` 改为 `markForSync()`；
- 客户端可通过 BlockEntity 更新包收到 `entries`/`oil`；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,925,928 bytes
SHA-256 85071E106AA81B19988A28C2487434BE5FE16CB37FCD8A8E02166FE48F024946
```

## 3. 未做

- 未实机；
- 未验证食材/油全路径同步。
