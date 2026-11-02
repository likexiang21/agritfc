# 648 代码筛查：木料堆 insert 的 all 参数未生效

> 日期：2026-10-30
> 状态：**代码已修复；静态构建通过；未实机**

## 1. 发现

`LumberPileBlockEntity.insert(ItemStack held, boolean all)` 的 `all` 参数没有参与逻辑：

```java
final int available = 64 - current.getCount();
final int amount = Math.min(1, available);
```

无论调用方传 `false` 还是 `true`，都只插入 1 个木料。该方法目前主要调用点传 `false`，但 API 契约错误，未来 shift 批量插入会静默失效。

## 2. 修复

```java
final int amount = Math.min(held.getCount(), all ? available : 1);
```

- `all=false`：保持每次 1 个；
- `all=true`：插入 `min(手持数量, 剩余容量)`；
- 不超过手持数量。

## 3. 校验

```text
gradle build BUILD SUCCESSFUL
```

当前 jar：

```text
2,926,150 bytes
SHA-256 CCB0A91E5B836529F3A7BBD451D0E6E1CFC4669992273ABA4EEDAE07ACEAFDD6
```

## 4. 未完成

- 未把 shift 交互接到 `all=true`（行为变更需单独确认）。
