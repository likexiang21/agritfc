# 312 种子处理 P0-L 工作报告

> 日期：2026-10-28
> 状态：**初步完成，未推送、未提交远程**
> 范围：种子处理 DataComponent + 湿草右键操作；生长/育苗效果未接。

## 1. 完成内容

- `SeedTreatments`：阶段推进；
- `SEED_TREATMENT` String DataComponent；
- `SeedTreatmentHandler`：
  - 主手种子；
  - 副手 `wet_grass`；
  - 右键推进 soaked → germinated → dressed；
  - 消耗 1 湿草（创造不消耗）；
- 主入口注册事件。

## 2. 验证

```text
PASS: 271 crop P0 checks
```

新增 6 项：

- 三个阶段推进；
- TFC 种子识别；
- A 种子识别；
- 食物不误判。

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

## 3. 边界

- **未实机验证**；
- 处理阶段尚未影响生长速度/育苗/移栽；
- 没有 UI/提示；
- 没有完整九工序；
- 没有处理种子物品（按计划使用组件）。
