# 685 坚果/坚果粉/蘑菇食物定义修复工作报告

> 日期：2026-10-31
> 状态：**数据已修复；未实机**

## 1. 完成

- 新增 31 个 `data/tfcagricultureplus/tfc/food/*.json`：
  - 8 坚果；
  - 8 坚果粉；
  - 15 野生蘑菇 BlockItem；
- 全部带 `ingredient`、`hunger`、`saturation`、`protein`、`decay_modifier`；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,937,449 bytes
SHA-256 FB7B183E9ABACB2009E59A17A92D20690490DA588D50AC19E1FD37907C6873BA
```

## 3. 未做

- 未实机；
- 未添加蘑菇干燥/烹饪配方；
- 香料产品未全部设为可食用。
