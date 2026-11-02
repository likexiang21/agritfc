# 657 育苗盘客户端掉落种子修复工作报告

> 日期：2026-10-30
> 状态：**代码已修复；未实机**

## 1. 完成

- `NurseryTrayBlockEntity.dropSeed` 增加 `level == null || level.isClientSide()` 早退；
- 客户端不再生成幽灵种子/清空客户端 BE；
- 服务端保留原有掉落；
- `gradle build` 成功；
- jar 已迁移到 `mods/`。

## 2. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,925,941 bytes
SHA-256 4C8E68A60A83DE603B408A17A17CED78049DD9B5D75CE878F8E98FE2D2D4CB7E
```

## 3. 未做

- 未实机；
- 未验证破坏/取出全路径。
