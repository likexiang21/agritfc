# 576 晾架占位模型替换工作报告

> 日期：2026-10-30
> 状态：**静态视觉修复；未实机**

## 1. 完成

- 新增共享晾架模型（四腿 + 顶部框 + 横条）；
- 34 个 per-wood 模型改为 parent 共享模型；
- TFC/AFC 木材纹理分别继承；
- 无新增贴图；
- `gradle build` 成功。

## 2. 校验

```text
json 6484 / bad 0
final_static_audit problems 0
```

## 3. 未做

- 未实机；
- 未做 facing 视觉旋转；
- 未处理 spice_trellis。
