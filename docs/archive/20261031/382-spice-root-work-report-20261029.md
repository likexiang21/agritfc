# 382 豆蔻根茎 P0-AU 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：cardamom 根茎物品/种植/收获；完整 root 机制未完成。

## 1. 完成内容

- `SpiceRootItem`；
- `AgricultureSpices.ROOTS`（当前仅 cardamom）；
- 收获额外掉 1 根茎；
- 根茎可右键种回 cardamom；
- item model + en/zh；
- 创造页。

## 2. 验证

```text
PASS: 382 crop P0 checks
PASS: spice root resources
gradle compileJava
BUILD SUCCESSFUL
processResources BUILD SUCCESSFUL
```

## 3. 边界

- **未实机**；
- 只有 cardamom；
- 根茎无分级；
- 放置不额外检查 farmland；
- 数量未平衡；
- 不能宣称 root 香料全部完成。

## 4. 下一批

1. 实机 cardamom；
2. 根茎分级；
3. 更多 root 香料；
4. 全量实机测试。
