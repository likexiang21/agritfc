# 667 锅腐烂黄油拒绝修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- `CookingPanBlockEntity.addSolidOil` 增加 `FoodCapability.isRotten` 检查；
- 腐烂黄油不再能作为固态油；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,926,100 bytes
SHA-256 E5CE3F97B9B7D3FA8BEBDC01B90A030AF49AE8FFAA580C81BB41A36F54F71AFE
```

## 3. 未做

- 未实机；
- 未验证其它固态油来源。
