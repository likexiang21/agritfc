# 531 P2-2 木工内容与 TFC Woodworking 对照工作报告

> 日期：2026-10-29
> 状态：**静态对照 + 一处错误修复；未实机**
> 范围：P2-2。

## 1. 完成

- 对照 TFCW 原版 40 条 wood/stripped_wood 配方；
- B 的 40 条复制配方结构与 key/result 一致，problems 0；
- 发现并删除 `lumber_pile` 的错误自掉落表；
- P0-3 loot 数量修正为 173。

## 2. 校验

```text
gradle clean build BUILD SUCCESSFUL
json 6441 / bad 0
final_static_audit problems 0
woodwork parity 40/40 problems 0
```

## 3. 未做

- 未实机；
- 未逐项对照模型/碰撞/交互/音效；
- 未证明 TFCW 原 in-world 去皮/劈木动作全部等
- 未处理视觉。
