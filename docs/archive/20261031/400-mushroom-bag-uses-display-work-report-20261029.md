# 400 菌包使用次数显示 P0-BD 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：菌包 growing 提示附加 uses/max；未实机。

## 1. 完成内容

- growing 消息追加 `(uses/MAX_USES)`；
- 便于实机观察复用次数。

## 2. 验证

```text
PASS: 393 crop P0 checks
PASS: B data item refs 0
gradle compileJava
BUILD SUCCESSFUL
```

## 3. 边界

- **未实机**；
- 只空手右键；
- 无 tooltip；
- 次数文本未本地化；
- 不能宣称菌包 UI 完成。

## 4. 下一批

1. 实机显示；
2. tooltip；
3. GUI；
4. 全量实机测试。
