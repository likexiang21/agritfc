# 357 藏红花球茎 P0-AH 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：藏红花球茎物品/种植/收获；完整球茎分级未完成。

## 1. 完成内容

- `CormItem`；
- `AgricultureSpices.CORMS`（当前仅 saffron）；
- 收获额外掉 1 球茎；
- 球茎可右键种回 saffron 作物；
- item model + en/zh；
- 创造页。

## 2. 验证

```text
PASS: 343 crop P0 checks
PASS: spice corm resources
gradle compileJava
BUILD SUCCESSFUL
```

## 3. 边界

- **未实机**；
- 只有藏红花；
- 没有球茎分级/大小；
- 放置不额外检查 farmland；
- 球茎与 2 种子同时掉落的平衡未验证；
- 不能宣称全部 corm 香料完成。

## 4. 下一批

1. 实机藏红花；
2. 球茎分级；
3. 更多 corm 香料；
4. 全量实机测试。
