# 581 OPEN-012 静态覆盖收口评估

> 日期：2026-10-30
> 状态：**静态覆盖达到可实现范围；未实机**
> 约束：不实机、不推送。

## 1. 当前 JEI 覆盖

B 自有 recipe category：

| category | 数量 |
|---|---:|
| `mortar` | B 自定义 |
| `cutting_board` | B 自定义 |
| `in_world` | 409 条（205 axe + 204 saw） |

复用上游 category：

- Firmalife `drying`：34 个 B 晾架 catalyst；
- Firmalife `mixing_bowl`：B 食谱使用原类型；
- TFC `knapping`：B 陶盘 recipe 使用 `tfc:knapping`；
- TFC 其它加工：按 TFC 原类型自动出现。

## 2. 催化剂

- mortar：15 种岩石石臼；
- cutting board：wooden/stone/log 三族；
- in_world：`#c:tools/axe` + `#c:tools/saw` 全部物品；
- drying：34 个 B 晾架；
- 烹饪锅：动态组合，无固定 recipe category。

## 3. 信息页

- 10 个设备；
- 19 个金属罐；
- 18 个陶盘/木盘；
- 21 个繁殖材料；
- 3 个新增 info 语言键。

## 4. 为什么没有“B 独立 category”更多

再新增会重复：

- drying 已由 Firmalife 显示；
- mixing bowl 已由 Firmalife 显示；
- knapping 已由 TFC 显示；
- pan 是动态组合，不是固定 recipe；
- nursery 没有 recipe 类型，只有信息页。

因此关闭 OPEN-012 的“独立分类”要求，保留 `partially` 的实机验证项。

## 5. 未完成

- 未实机确认 JEI 页面/侧栏；
- 烹饪锅仍无固定配方展示；
- 未新增 B 独立的“繁殖材料”category（配方本身是原版 crafting）。
