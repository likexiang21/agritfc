# 365 草莓普通作物 P0-AL 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：B strawberry 普通作物；野生生成/实机未完成。

## 1. 完成内容

- `crop/strawberry` CropBlock；
- `seeds/strawberry` BlockItem；
- 8 龄 blockstate；
- product + seed loot；
- 统一收获自动追加 crop_waste/strawberry；
- 种子处理/育苗/移栽系统自动识别；
- 创造页；
- 临时模型/贴图/语言。

## 2. 验证

```text
PASS: strawberry crop resources
PASS: 363 crop P0 checks
gradle compileJava
BUILD SUCCESSFUL
processResources BUILD SUCCESSFUL
```

## 3. 边界

- **未实机**；
- B 命名空间替代，不是 A 原方块；
- TFC strawberry_bush 仍保留；
- 没有野生生成；
- 贴图临时；
- 不能宣称 A 87 完整验收。

## 4. 下一批

1. 实机种植/收获；
2. 野生生成；
3. 与 TFC strawberry_bush 关系裁决；
4. 全量实机测试。
