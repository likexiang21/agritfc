# 643 自定义树叶 codec 修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- `SpiceTreeLeavesBlock` 重写 `codec()`；
- `NutLeavesBlock` 重写 `codec()`；
- 两次编译修正了返回类型与可见性（`public MapCodec<? extends LeavesBlock>`）；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,924,120 bytes
SHA-256 A9B1D14063DB73868E02B0B5406593BFC4A14A266C7437C1E8430EDD11D83AF8
```

## 3. 未做

- 未实机；
- 未逐项验证全部自定义 Block 子类 codec。
