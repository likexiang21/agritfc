# 470 测试命令清理与最终构建 P0-CM 技术分析

> 日期：2026-10-29
> 目标：移除实机测试用临时命令，产出可发布构建。
> 约束：不推送；不伪造。

## 1. 移除内容

从 `TFCAgriculturePlus` 移除：

```text
/tfcplusdebug_harvest
/tfcplusdebug_drops
/tfcplusdebug_use
```

及对应 `RegisterCommandsEvent` 监听、调试 import。

## 2. 保留内容

- 树生成日志；
- 注册计数日志；
- 全部正式注册/事件/资源。

## 3. 验证

```text
gradle build BUILD SUCCESSFUL
validate_crop_p0a.py PASS（全部项）
jar: TFCAgriculturePlus-NeoForge-1.21.1-0.1.0.jar
size: 2,745,908
```

## 4. 结论

测试入口已从正式 jar 移除，构建与资源校验通过。

## 5. 未验证

- 移除命令后的客户端加载（仅构建/资源校验）；
- 其余玩法链。
