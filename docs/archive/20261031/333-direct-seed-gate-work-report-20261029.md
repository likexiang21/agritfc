# 333 直播替换 P0-V 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：取消 A/TFC/B 种子直接种植，要求育苗盘/幼苗移栽；未实机。

## 1. 完成内容

- `DirectSeedPlantingGate`；
- 覆盖 A/TFC/B 种子；
- 只拦截 farmland 上的直接种植；
- 提示 `message.tfcagricultureplus.planting.use_nursery`；
- 育苗盘取出幼苗复制 SEED_TREATMENT；
- 幼苗移栽后执行 1/2/3 次受限生长推进；
- 主入口注册事件。

## 2. 验证

```text
gradle compileJava
BUILD SUCCESSFUL
```

已有：

```text
PASS: 283 crop P0 checks
```

## 3. 边界

- **未实机验证**；
- 玩家必须先做育苗盘，不能直接种；
- TFC/A 作物是否 `BonemealableBlock` 未确认；
- 自动化/脚本种植可能被影响；
- 没有完整实机回归；
- 不能宣称种植链全部验收。

## 4. 下一批

1. 实机验证拦截/移栽/生长；
2. 确认 TFC/A Bonemealable；
3. 收获替换；
4. 全量实机测试。
