# 355 蘑菇菌包产出范围 P0-AG 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：11 种可栽培蘑菇菌包 min/max 产出；完整平衡未完成。

## 1. 完成内容

- `bagMinYield`/`bagMaxYield` 11 种；
- 菌包 harvest 改为 min+random(max-min+1)；
- 纯 Java 校验 11 组。

## 2. 验证

```text
PASS: 342 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
```

## 3. 边界

- **未实机**；
- 数值未平衡；
- 没有环境/上限；
- 自然专用 4 种仍不可栽培；
- 不能宣称蘑菇链完成。

## 4. 下一批

1. 实机菌包；
2. 环境/产出平衡；
3. 自然专用替代；
4. 全量实机测试。
