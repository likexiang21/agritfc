# 665 锅铲手槽修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- `CookingPanBlockEntity.stir` 增加 `InteractionHand` 参数；
- 按实际手选择 `MAINHAND` / `OFFHAND` 扣耐久；
- `PanInteractions` 传入实际手；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,926,094 bytes
SHA-256 1AF26FC740A7E17E3F0FD5CD8EC915EC175679118E327219E6BAEDDADFDA0ED7
```

## 3. 未做

- 未实机；
- 未验证双持锅铲边界。
