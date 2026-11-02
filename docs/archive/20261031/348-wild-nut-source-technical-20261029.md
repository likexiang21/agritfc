# 348 野草开心果/腰果来源 P0-AD 技术分析

> 日期：2026-10-29
> 目标：在开心果/腰果专属树完成前，给这两种 B 坚果一个临时可获得来源，避免 B 43 坚果只停留在创造页。
> 约束：不推送；不伪造；明确标注为临时。

## 1. 背景

B 8 种坚果中：

- acorn/chestnut/pine_nut/hickory_nut/beechnut：已有 TFC/AFC 树叶映射；
- macadamia：A 已有树叶临时来源；
- **pistachio / cashew：没有任何树/叶映射，当前不可获得**。

## 2. 实现

`WildNutDropHandler`：

- 短草/高草破坏；
- 2% 概率；
- 随机掉 `pistachio` 或 `cashew`；
- 同时掉对应 `nut_shell/<nut>`；
- 不取消原草掉落。

## 3. 定位

这是**临时可获得性来源**，不是树，也不是正式生态。等 pistachio/cashew 专属树完成后，应删除或大幅降低该来源。

## 4. 测试

```text
gradle compileJava
BUILD SUCCESSFUL
```

已有：

```text
PASS: 320 crop P0 checks
```

## 5. 风险

- 未实机；
- 2% 概率未平衡；
- 与树种/生物群系无关；
- 不是正式生产链；
- 不能宣称坚果树完成。
