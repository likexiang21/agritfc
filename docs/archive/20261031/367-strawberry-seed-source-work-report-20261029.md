# 367 草莓种子来源 P0-AM 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：TFC strawberry_bush 20% 掉 B 草莓种子；未实机。

## 1. 完成内容

- `StrawberrySeedDropHandler`；
- 20% 掉 B strawberry seed；
- 不取消原 TFC 掉落；
- 与草莓废枝叶 handler 并存。

## 2. 验证

```text
gradle compileJava
BUILD SUCCESSFUL
PASS: 363 crop P0 checks
```

## 3. 边界

- **未实机**；
- 20% 未平衡；
- TFC 草莓丛与 B 草莓作物并存；
- 没有正式野生生成；
- 不能宣称草莓链最终完成。

## 4. 下一批

1. 实机草莓链；
2. 平衡；
3. 野生生成/关系裁决；
4. 全量实机测试。
