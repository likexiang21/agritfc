# 335 A 作物种子返还 P0-W 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：A 87 作物的种子返还兜底；完整收获替换未完成。

## 1. 完成内容

- `ACropSeedReturnHandler`；
- 只匹配 `tfcfarmingplus:crop/<crop>`；
- 跳过 A 谷物；
- 真实最大 age 才掉 1 个 `tfcfarmingplus:seeds/<crop>`；
- 不取消原破坏；
- 主入口注册。

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

- **未实机**；
- 可能重复原 A 种子掉落；
- 不处理双格/特殊作物；
- 不是完整收获替换；
- 不能宣称 A 87 完成。

## 4. 下一批

1. 实机核对 A 种子 ID；
2. A 收获替换；
3. B 香料/坚果链；
4. 全量实机测试。
