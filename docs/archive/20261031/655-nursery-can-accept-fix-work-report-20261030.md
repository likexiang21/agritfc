# 655 育苗盘 canAccept 修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- `NurseryTrayBlockEntity.canAccept` 条件从 `seed.isEmpty()` 改为 `!seed.isEmpty()`；
- 空托盘现在可以接受 A/B 种子；
- 已有种子仍拒绝；
- TFC 种子仍拒绝；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,925,925 bytes
SHA-256 464B0A20A16472B75DB608D6A6519A5C79C0E6F6B4604C79B15212D29686BEFC
```

## 3. 未做

- 未实机；
- 未验证生长/取出完整流程。
