# 625 种子处理静态物品初始化修复工作报告（OPEN-016）

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- 删除 `SeedTreatmentHandler` 的 3 个静态 `Item` 字段；
- 改为事件触发时解析 `tfc:compost` / `tfc:powder/wood_ash` / `tfc:powder/lime`；
- 全项目扫描确认无其它 `static final Item/Block` 注册对象；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
static final Item 0
static final Block 0
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,921,535 bytes
SHA-256 14C986E224FD43F2FF862C7D07C40F0A40FAFF744071A9FCED0E657B2598832D
```

## 3. 未做

- 未实机；
- 未启动客户端；
- 未通知玩家测试。
