# 331 野草香料种子来源 P0-U 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：草方块 5% 随机香料种子来源；正式野生香料 worldgen 未完成。

## 1. 完成内容

- `SpiceSeedDropHandler`；
- 短草/高草破坏 5% 概率；
- 从 20 种 SpiceSpecies 随机一种；
- 掉 1 个对应 `spice_seed/<species>`；
- 不取消原草掉落；
- 主入口注册。

## 2. 验证

```text
gradle compileJava
BUILD SUCCESSFUL
```

已有纯 Java：

```text
PASS: 283 crop P0 checks
```

## 3. 边界

- **未实机验证**；
- 只是临时初始来源；
- 单一种子命中概率低；
- 没有正式野生香料植物/worldgen；
- 没有平衡/保底；
- 不能宣称香料生态完成。

## 4. 下一批

1. 正式野生香料植物；
2. 种子来源保底/平衡；
3. TFC 29 剩余；
4. 全量实机测试。
