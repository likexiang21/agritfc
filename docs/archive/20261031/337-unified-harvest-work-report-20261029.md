# 337 统一收获替换 P0-X 工作报告

> 日期：2026-10-29
> 状态：**初步完成，未推送、未提交远程**
> 范围：A/TFC/B 非谷物成熟作物的 B 控制收获替换；未实机。

## 1. 完成内容

- `CropBItemResolver`：
  - 三类方块 → 种子/废枝叶；
  - 谷物识别；
- `UnifiedCropHarvestHandler`：
  - 取消成熟非谷物破坏；
  - 原 loot 原产物；
  - 补种子；
  - 补废枝叶；
  - 移除方块；
- 旧 `CropWasteHandler`/TFC/A 种子返还加入 `event.isCanceled()` 跳过，避免重复；
- 主入口事件顺序调整。

## 2. 验证

```text
gradle compileJava
BUILD SUCCESSFUL
```

已有：

```text
PASS: 283 crop P0 checks
```

## 3. 边界

- **未实机**；
- 原 loot 的时运/工具/玩家条件未逐一验证；
- 双格 top/bottom 未完整验证；
- 可能影响其他 mod 的 BlockEvent 监听；
- 没有完整收获回归；
- 不能宣称 A/TFC/B 收获全部验收。

## 4. 下一批

1. 实机核对 A/TFC/B 作物收获；
2. 双格/特殊作物；
3. 香料形态/坚果树；
4. 全量实机测试。
