# 619 二次崩溃修复工作报告（烤箱配方迁移）

> 日期：2026-10-30
> 状态：**数据已修复；未实机**

## 1. 完成

- 定位 15 条 `firmalife:oven` 配方；
- 全部转换为 `tfc:heating`；
- 删除 `recipe/oven/`；
- B 数据中 `firmalife:oven` 引用为 0；
- `gradle build` 成功；
- 新 jar 已迁移到 `mods/`。

## 2. 校验

```text
heating recipes = 16
firmalife:oven refs = 0
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,921,489 bytes
SHA-256 CA37E09A14ADDD9D3198FB23183D62C631934292E0254DB0E9D07175A19F8FF6
```

## 3. 未做

- 未实机；
- 需用户启动确认 JEI 烤箱分类已隐藏、无崩溃。
