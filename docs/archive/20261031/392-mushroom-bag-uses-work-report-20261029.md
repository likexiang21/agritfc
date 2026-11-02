# 392 菌包使用次数上限 P0-AZ 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：菌包 3 次使用上限；未实机。

## 1. 完成内容

- `uses` 字段；
- `MAX_USES=3`；
- `markSpent` 自增；
- `maxed()`；
- stage 3 接种前检查；
- spent 消息；
- NBT 保存/读取。

## 2. 验证

```text
PASS: 393 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
processResources BUILD SUCCESSFUL
```

## 3. 边界

- **未实机**；
- 上限未平衡；
- 没有剩余次数提示；
- 耗尽后只能破坏/丢弃；
- 不能宣称菌包平衡完成。

## 4. 下一批

1. 实机次数；
2. tooltip 剩余次数；
3. 耗尽回收；
4. 全量实机测试。
