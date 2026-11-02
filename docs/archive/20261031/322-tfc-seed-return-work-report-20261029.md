# 322 TFC 种子返还 P0-Q 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：29 种 TFC 作物的成熟种子返还兜底；完整收获替换未完成。

## 1. 完成内容

- `TfcCropSpecies`：29 条；
- `TfcSeedReturnHandler`：
  - 只处理 `tfc:crop/<id>`；
  - 6 个谷物跳过（GrainHarvestHandler 负责）；
  - 真实最大 age 才返还 1 个种子；
  - 不取消原破坏；
  - 双格 top 跳过；
- 主入口注册事件。

## 2. 验证

```text
PASS: 282 crop P0 checks
```

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

## 3. 边界

- **未实机验证**；
- 会和 TFC 原种子掉落形成重复可能；
- 不是完整替换 TFC 收获；
- 种子 ID 需实机核对；
- 不处理种植/育苗；
- 不能宣称 TFC 29 完成。

## 4. 下一批

1. TFC 29 完整种植/收获覆盖；
2. 实机核对种子 ID；
3. 全量实机测试。
