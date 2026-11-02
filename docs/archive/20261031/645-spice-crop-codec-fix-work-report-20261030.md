# 645 香料作物 codec 修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- `SpiceCropBlocks.Herb/Shrub/Tree/Vine/Root/Corm` 各自重写 `codec()`；
- codec 保留对应形状/棚架逻辑，不再退化为普通 CropBlock；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,926,090 bytes
SHA-256 6E2AAD104A29DCB70874F800474E75D0DFA3B9D891BCD01B843172AEBD67E606
```

## 3. 未做

- 未实机；
- 未验证其它自定义 CropBlock 子类。
