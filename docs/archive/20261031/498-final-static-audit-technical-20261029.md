# 498 最终静态/原型/jar 审计 P0-DA 技术分析

> 日期：2026-10-29
> 目标：在临近轮数上限前做一次最终构建审计。
> 约束：不推送；不伪造。

## 1. 资源校验

`validate_crop_p0a.py`：全部 PASS。

## 2. 纯 Java 原型

`CropYieldProto`：

```text
PASS: 393 crop P0 checks
protoExit=0
```

## 3. jar

```text
TFCAgriculturePlus-NeoForge-1.21.1-0.1.0.jar
2,745,942 bytes
debug_bytes = False
```

## 4. 未完成

- A 87 / TFC 29 / TFC 10 全量实机；
- 自然世界生成；
- 树叶衰减方块状态；
- 全量 159 行验收；
- 视觉/平衡；
- 长时间稳定性。

## 5. 结论

最终构建在静态/原型层面全绿，jar 无 debug 命令；
但实机覆盖仍是样本级，不能 mark complete。
