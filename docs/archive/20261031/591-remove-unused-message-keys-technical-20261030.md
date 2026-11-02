# 591 移除未使用的弹出式提示语言键技术分析

> 日期：2026-10-30
> 状态：**静态清理；未实机**
> 用户要求：减少弹出式提示文本。

## 1. 背景

587/588 已移除 13 处 `displayClientMessage` 调用，但语言文件仍保留 42 个
`message.tfcagricultureplus.*` 键，属于死文本。

## 2. 清理

从 `en_us.json` / `zh_cn.json` 删除所有以：

```text
message.tfcagricultureplus.
```

开头的键，共 42 个/语言。

保留：

- `block_entity.tfcagricultureplus.kitchen_storage.*`（容器标题）；
- `jei.tfcagricultureplus.*`；
- 物种名、物品名等。

## 3. 结果

```text
en_us 1129 → 1087
zh_cn 1129 → 1087
missing/extra 0
```

## 4. 校验

```text
json 6484 / bad 0
final_static_audit problems 0
gradle build BUILD SUCCESSFUL
```

## 5. 未完成

- `CookingPanBlockEntity.status()` 仍保留为死方法（无调用方），未删除；
- 未实机。
