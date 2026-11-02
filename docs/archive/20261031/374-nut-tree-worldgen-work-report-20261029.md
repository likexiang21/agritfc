# 374 坚果树立世界生成 P0-AQ 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：pistachio/cashew 树苗 worldgen；实机未完成。

## 1. 完成内容

- 2 个 configured feature；
- 2 个 placed feature；
- 1 个 biome modifier；
- 复用 `wild_mushroom_biomes` 标签；
- `would_survive` 过滤；
- 树苗生成后由随机刻长成 B 树。

## 2. 验证

```text
PASS: pistachio/cashew tree worldgen resources
processResources BUILD SUCCESSFUL
```

## 3. 边界

- **未实机**；
- 群系标签复用可能过宽；
- 土壤过滤未验证；
- 只生成树苗，不生成成树；
- 生长依赖随机刻；
- 不能宣称坚果生态完成。

## 4. 下一批

1. 实机 worldgen；
2. 群系/密度平衡；
3. 成树结构；
4. 全量实机测试。
