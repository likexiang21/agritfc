# 687 香料废枝叶堆肥接入工作报告

> 日期：2026-10-31
> 状态：**数据已修复；未实机**

## 1. 完成

- 20 个 `spice_waste/*` 全部接入 TFC 堆肥标签；
- herb 9 种 → high；
- 其余 11 种 → medium；
- 保留 TFC 原始 values；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,937,590 bytes
SHA-256 77D4BDA06C3C54BB4ED33EC6BDBE9F12D8A2CEB183D25C64A6D94B956422E623
```

## 3. 未做

- 未实机；
- 香料其它加工出口未补齐。
