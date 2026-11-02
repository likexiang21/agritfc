# 524 P1-3 Patchouli 作物章节技术分析

> 日期：2026-10-29
> 状态：**内容静态补全；未实机**
> 约束：不实机、不处理视觉、不推送。

## 1. 问题

用户报告帕秋莉手册不可读。

静态确认：

- B 原有手册只有 3 个旧主题：
  - 厨房；
  - 养蚕；
  - 木工；
- **没有作物系统章节**；
- 旧内容多为长段纯文本，没有分步骤结构。

## 2. 本次新增

新增分类：

```text
assets/tfc/patchouli_books/field_guide/
  en_us/categories/agriculture_plus_crops.json
  zh_cn/categories/agriculture_plus_crops.json
```

新增 7 个主题 × 中英双语 = **14 个 entry 文件**：

1. `crops/overview` —— 成熟收获、未成熟保护、双格清理、创造模式；
2. `crops/nursery` —— TFC 直播、A/B 育苗门、育苗盘、移栽、种子处理；
3. `crops/grain` —— 谷物捆、脱粒、湿草、干燥、堆肥；
4. `crops/spices` —— 15 作物香料 + 5 树香料、繁殖、研磨；
5. `crops/nuts` —— 3 种 B 坚果、nut_state 四季、成熟掉落；
6. `crops/mushrooms` —— 15 种野生、11 可栽培、4 naturalOnly、菌包温度/次数/阶段；
7. `crops/bushes` —— TFC 10 灌木、破坏拦截、废枝。

## 3. 可读性处理

- 每页只讲一个主题；
- 用 `$(li)` 列表和短段落；
- 不写原始物品 ID；
- 明确区分：
  - TFC 种子直接播种；
  - A/B 种子育苗；
  - 102 作物/香料废枝叶与 10 灌木废枝；
  - 11 可栽培 + 4 naturalOnly。
- 中英文内容同步。

## 4. 校验

```text
Patchouli entries: 20（旧 6 + 新 14）
Patchouli categories: 8（旧 6 + 新 2）
bad icons: 0
json 6442 / bad 0
final_static_audit problems 0
```

## 5. 未完成

- 未实机打开 Patchouli 检查排版/分页；
- 没有 recipe pages / 图片；仍是文字页；
- 旧厨房/养蚕/木工页面没有重写；
- 未处理视觉。
