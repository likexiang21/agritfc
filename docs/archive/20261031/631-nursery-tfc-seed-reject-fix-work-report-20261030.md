# 631 育苗盘 TFC 种子拒绝修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- `NurseryTrayBlockEntity.canAccept` 拒绝 `tfc:` 种子；
- 保持 A/B 种子育苗路径不变；
- `gradle build` 成功；
- 新 jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,921,883 bytes
SHA-256 AA959B2FD4B64C4C985B57F69569BD3F257776E5FD345D5C2CCF3D17848B7168
```

## 3. 未做

- 未实机；
- 未验证其它 A/B 种子移栽路径。
