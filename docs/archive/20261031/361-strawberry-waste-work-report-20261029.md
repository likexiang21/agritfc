# 361 草莓废枝叶来源 P0-AJ 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：TFC strawberry_bush 的 crop_waste/strawberry 来源；草莓正式作物化未完成。

## 1. 完成内容

- `StrawberryWasteHandler`；
- 精确匹配 TFC strawberry_bush；
- FRUITING 才掉；
- 追加 crop_waste/strawberry；
- 不取消原掉落；
- 主入口注册。

## 2. 验证

```text
gradle compileJava
BUILD SUCCESSFUL
PASS: 343 crop P0 checks
```

## 3. 边界

- **未实机**；
- 只补废枝叶；
- 草莓仍未成为真正 A 普通作物；
- 不影响 TFC 10 bush 统计；
- 不能宣称 A 87 完成。

## 4. 下一批

1. 草莓正式作物化；
2. 实机；
3. 全量验收。
