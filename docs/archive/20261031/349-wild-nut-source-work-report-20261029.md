# 349 野草开心果/腰果来源 P0-AD 工作报告

> 日期：2026-10-29
> 状态：**临时来源完成，未推送、未提交远程**
> 范围：pistachio/cashew 草的 2% 来源；专属树未完成。

## 1. 完成内容

- `WildNutDropHandler`；
- 短草/高草 2%；
- 随机 pistachio/cashew；
- 同时掉对应坚果壳；
- 不取消原草掉落；
- 主入口注册。

## 2. 验证

```text
gradle compileJava
BUILD SUCCESSFUL
PASS: 320 crop P0 checks
```

## 3. 边界

- **未实机**；
- 是临时来源，不是树；
- 概率未平衡；
- 无群系差异；
- pistachio/cashew 树仍未实现；
- 不能宣称坚果生产链完成。

## 4. 下一批

1. 专属树；
2. 实机核对；
3. 正式生态替换临时来源；
4. 全量实机测试。
