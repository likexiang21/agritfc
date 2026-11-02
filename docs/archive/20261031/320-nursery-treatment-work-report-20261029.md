# 320 育苗盘处理加速 P0-P 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：种子处理阶段缩短育苗盘生长时间；未实机。

## 1. 完成内容

- `SeedTreatments.nurseryTicks(stage)`：
  - 1200 / 1000 / 800 / 600；
- `NurseryTrayBlockEntity`：
  - `insert` 读取 SEED_TREATMENT；
  - 保存 `requiredTicks`；
  - `ready()` 使用 requiredTicks；
  - 存档保存/读取 `required_ticks`；
  - tick 使用 requiredTicks。

## 2. 验证

```text
PASS: 278 crop P0 checks
```

新增 4 个育苗时间检查。

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

## 3. 边界

- **未实机验证**；
- 组件在种子入槽时保留未实测；
- 数值未平衡；
- 不支持无性苗；
- 没有 GUI。

## 4. 下一批

1. 实机验证种子处理→育苗→移栽；
2. 无性苗；
3. TFC 29 剩余覆盖；
4. 全量实机测试。
