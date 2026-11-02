# 603 OPEN-005 扩展：灌木废枝图标差异化技术分析

> 日期：2026-10-30
> 状态：**静态视觉映射；未实机**
> 约束：视觉可用，但不重绘贴图。

## 1. 问题

10 个 `bush_waste/<species>` 仍共用：

```text
tfc:item/straw
```

与作物废枝叶问题相同。

## 2. 修复

复用 TFC 已有浆果灌木贴图：

| 物种 | 贴图 |
|---|---|
| blackberry | `tfc:block/berry_bush/blackberry_bush` |
| blueberry | `.../blueberry_bush` |
| bunchberry | `.../bunchberry_bush` |
| cloudberry | `.../cloudberry_bush` |
| cranberry | `.../cranberry_bush` |
| elderberry | `.../elderberry_bush` |
| gooseberry | `.../gooseberry_bush` |
| raspberry | `.../raspberry_bush` |
| snowberry | `.../snowberry_bush` |
| wintergreen | `.../wintergreen_berry_bush` |

10 个 item model 改为 `minecraft:item/generated` + 对应 layer0。

没有新增/重绘 PNG。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
json 6484 / bad 0
final_static_audit problems 0
```

## 4. 未完成

- 未实机查看图标；
- 香料/坚果 item 图标仍是 `tfc:item/straw` 占位，未处理；
- 未处理视觉细节。
