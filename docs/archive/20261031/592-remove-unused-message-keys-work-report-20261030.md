# 592 移除未使用的弹出式提示语言键工作报告

> 日期：2026-10-30
> 状态：**静态清理；未实机**

## 1. 完成

- 删除 42×2 个 `message.tfcagricultureplus.*` 键；
- 中英语言仍保持 1087 / 1087；
- `gradle build` 成功。

## 2. 校验

```text
lang 1087 / 1087 / missing 0 / extra 0
json 6484 / bad 0
final_static_audit problems 0
```

## 3. 未做

- 未删除 `CookingPanBlockEntity.status()`；
- 未实机。
