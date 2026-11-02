# 639 TFC 灌木废枝重复修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- `BushWasteHandler` 增加 `SeasonalPlantBlock.LIFECYCLE == FRUITING` 跳过；
- 结果灌木的废枝只由 `BushHarvestHandler` 掉一次；
- 非结果灌木仍由 `BushWasteHandler` 掉；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,923,274 bytes
SHA-256 6B9801C5DCA4FC5512807011DFC31436F2A75375095732DA826CDA886094E073
```

## 3. 未做

- 未实机；
- 未验证其它 SeasonalPlantBlock 掉落。
