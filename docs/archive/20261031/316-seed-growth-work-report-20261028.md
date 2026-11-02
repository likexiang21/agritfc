# 316 种子处理生长效果 P0-N 工作报告

> 日期：2026-10-28
> 状态：**初步完成，未推送、未提交远程**
> 范围：种植后对处理种子执行一次受限生长推进；未实机。

## 1. 完成内容

- `SeedTreatmentGrowthHandler`；
- 读取 `SEED_TREATMENT` 组件；
- soaked → 1 / germinated → 2 / dressed → 3 次推进；
- 目标位置只在作物是 `BonemealableBlock` 且有效时才推进；
- 主入口注册 game-bus listener。

## 2. 验证

```text
PASS: 274 crop P0 checks
```

新增 3 项 boost 阶段校验。

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

## 3. 边界

- **未实机验证**；
- 依赖目标作物实现 `BonemealableBlock`；
- 服务器 task 与方块放置顺序未验证；
- 不保证 TFC/A 作物实际接受这个推进；
- 没有失败提示；
- 不替代 TFC 种植。

## 4. 下一批次

1. 实机前先确认 TFC/A 作物是否 Bonemealable；
2. 育苗盘/缓苗；
3. TFC 29 剩余覆盖；
4. 全部代码完成后再统一实机测试。
