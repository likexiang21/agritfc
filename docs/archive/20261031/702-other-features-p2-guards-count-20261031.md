# 702 其他功能 P2 清理：创造模式守卫与自检计数

> 日期：2026-10-31
> 状态：**代码已修复；静态构建通过；未实机**

## 1. Firmalife 废枝叶创造模式守卫

`FirmalifePlantWasteHandler` 与其他收获/废枝处理器不一致，创造模式破坏也会掉 B 废枝叶。

修复：在 `onBlockBreak` 开头加：

```java
if (CreativeGuards.isCreative(event)) {
    return;
}
```

与 `BushWasteHandler` / `CropWasteHandler` / `StrawberryWasteHandler` 一致。

## 2. 客户端渲染自检计数

`TFCAgriculturePlusClient` 的 `total` 只取 `AgricultureBlocks.all().size()`，但 cutout 还包含
`AgricultureSpices.CROPS` 和盘子，日志会出现负数“无需登记”。

修复：

```java
final int total = AgricultureBlocks.all().size()
    + AgricultureSpices.CROPS.size() + 1;
```

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
json 6535 / models 3709 / blockstates 539 / item_models 957
lang 1107 / 1107
final_static_audit problems 0
```

当前 jar：

```text
2,954,689 bytes
SHA-256 9CAA9D331665B567C14FF283C7C45022FCF0F9F9A22CB81671B246B2629A106A
```

## 4. 仍未完成

- 未实机；
- 菌包丢进度、流体掉落、BER、GUI 仍属 P2；
- P1-5/P1-6 视觉资源仍未完成。
