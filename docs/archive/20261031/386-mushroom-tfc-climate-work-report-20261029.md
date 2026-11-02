# 386 蘑菇菌包 TFC 气候温度 P0-AW 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：菌包温度改用 TFC Climate；实机未完成。

## 1. 完成内容

- `MushroomBagBlockEntity` 改用：
  - `Climate.getAverageTemperature`；
  - `Climate.fromVanilla` 映射 preferred/tolerance；
- 温度不适宜仍暂停 progress。

## 2. 验证

```text
PASS: 393 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
```

## 3. 边界

- **未实机**；
- 映射/尺度未核对；
- 容差未平衡；
- 极端气候可能永不推进；
- 没有提示；
- 不能宣称蘑菇环境完成。

## 4. 下一批

1. 实机 TFC 温度；
2. 容差校准；
3. 玩家提示；
4. 全量实机测试。
