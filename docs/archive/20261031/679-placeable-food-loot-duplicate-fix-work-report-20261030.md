# 679 摆盘食物掉落去重修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- `PlaceableFoodBlock.getDrops` 返回空列表；
- 剩余食物只由 `PlaceableFoodBlockEntity.onRemove → dropContents()` 掉落；
- 不再出现整块 + 切片双掉；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,926,691 bytes
SHA-256 FD0C3C2AC27D78E863BC3B5B5494C93EEFC96E3DC6D8BACB328C7516CF5AB6F9
```

## 3. 未做

- 未实机；
- 未验证爆炸/活塞/精准采集。
