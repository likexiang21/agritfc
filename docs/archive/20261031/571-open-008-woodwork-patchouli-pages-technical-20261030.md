# 571 OPEN-008 扩展：木工手册 spotlight 页技术分析

> 日期：2026-10-30
> 状态：**静态内容补全；未实机**
> 约束：不实机、不推送。

## 1. 背景

木工主题 `agriculture_plus_woodwork/intro` 只有 3 页文字，没有物品入口。
玩家看不到 debarked log / half / quarter、树皮、韧皮的样子。

## 2. 新增 spotlight ×5

中英双语：

- `debarked_log/oak`：4 单位木料堆输入；
- `debarked_half/oak`：2 单位，带朝向；
- `debarked_quarter/oak`：1 单位；
- `bark/oak`：B 自有树皮副产物；
- `bast/oak`：B 自有韧皮副产物。

## 3. 校验

```text
json 6483 / bad 0
final_static_audit problems 0
gradle build BUILD SUCCESSFUL
```

## 4. 未完成

- 未实机检查页渲染；
- 没有 TFC workbench 配方页（木工是斧/锯/工作台处理，不是单一 crafting）；
- 未处理视觉。
