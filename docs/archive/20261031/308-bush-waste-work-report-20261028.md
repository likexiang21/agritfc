# 308 TFC 灌木废枝 P0-J 工作报告

> 日期：2026-10-28
> 状态：**初步完成，未推送、未提交远程**
> 范围：10 种 TFC 灌木的废枝副产；完整采收/再生替换未完成。

## 1. 完成内容

- 新增 `BushSpecies` 10 条；
- 新增 `AgricultureShrubs` 独立物品注册；
- 新增 `BushWasteHandler`；
- 10 个 `bush_waste/<species>` 物品；
- 10 个 item model + en/zh 语言；
- 10 条加入 `tfc:compost_greens/high`；
- 创造页加入。

## 2. 行为

玩家破坏以下精确方块时：

```text
tfc:plant/<species>_bush
```

追加 1 个 `bush_waste/<species>`。

- 不取消原破坏；
- TFC 原浆果/生命周期掉落保留；
- 未处理 A 的灌木，未处理草莓。

## 3. 验证

```text
PASS: 245 crop P0 checks
PASS: 99 item models, 2 lang files, 17 recipes, 102 crop_waste,
      10 bush_waste, 15 wild mushrooms, 4-stage bag, 79 nut leaf states,
      20 spice crops, tags valid
```

编译：

```text
gradle compileJava
BUILD SUCCESSFUL
```

`processResources`：

```text
BUILD SUCCESSFUL
```

## 4. 边界

- **未实机验证**；
- 只补副产，不是完整替换 TFC 灌木采收/再生；
- 没有 B 灌木方块/育苗/扦插；
- 10 条 bush_waste 独立统计，不并入 102 crop_waste；
- 贴图临时 TFC。

## 5. 下一步

1. 完整 TFC 灌木采收/再生替换；
2. TFC 29 剩余种植/收获；
3. 香料形态；
4. 坚果 overlay；
5. 全部代码完成后再统一实机测试。
