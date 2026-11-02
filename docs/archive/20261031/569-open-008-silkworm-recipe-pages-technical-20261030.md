# 569 OPEN-008 扩展：养蚕手册 recipe/spotlight 页技术分析

> 日期：2026-10-30
> 状态：**静态内容补全；未实机**
> 约束：不实机、不推送。

## 1. 背景

养蚕手册 `agriculture_plus_silkworm/intro` 只有 3 页文字，没有养蚕架配方和蚕卵/蚕茧/蚕丝物品入口。

## 2. 新增页

### crafting ×1

```text
recipe: tfcagricultureplus:workstations/silkworm_rack
```

原版 `crafting_shaped`，Patchouli 可直接显示。

### spotlight ×3

- `silkworm_egg`：0 °C 以上 2–4 天孵化；
- `cocoon`：10 成长点结茧，3–5 天成虫；
- `silk_thread`：熟蚕+纺锤 → 1 丝线，24 丝线织 1 丝绸。

中英双语。

## 3. 校验

```text
recipe ID 存在
json 6483 / bad 0
final_static_audit problems 0
gradle build BUILD SUCCESSFUL
```

## 4. 未完成

- 未实机检查页渲染；
- 未给木工主题加 recipe 页；
- 未处理视觉。
