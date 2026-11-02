# 588 交互去 UI 化：移除弹出式提示文本工作报告

> 日期：2026-10-30
> 状态：**静态实现；未实机**

## 1. 完成

- 移除 13 处 `displayClientMessage`；
- 涉及刀架、菌包、种植门、案板、晾架、石臼、平底锅；
- 保留方块/物品状态与声音反馈；
- 保留厨房容器 UI 与养蚕架 TFC UI；
- `gradle build` 成功。

## 2. 校验

```text
displayClientMessage files 0
json 6484 / bad 0
final_static_audit problems 0
```

## 3. 未做

- 未实机；
- 未移除语言文件死键；
- 未给所有静默失败补音效。
