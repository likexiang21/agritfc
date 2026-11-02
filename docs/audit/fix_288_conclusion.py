from pathlib import Path

p = Path("mod_rebuild/docs/288-crop-production-and-cultivation-chain-20261028.md")
t = p.read_text(encoding="utf-8")
old = """**真正的问题不是 29 个 ID、也不是 A 的 6 个 cabbage 模型，而是：**

> 文档把“作物重做”同时定义成 **29 种 TFC 作物的资源覆盖** 和
> **86 种作物的生产链 + 六环节培育链 + 九道种子加工工序**，
> 但没有把这两套范围合并成可执行批次。
> 资源覆盖无法实现培育链；生产/培育链目前完成度为 0；
> 这就是农作物部分的真正关键问题。"""
new = """**2026-10-28 已定案：**

> 29 种 TFC 作物与 10 种 TFC 灌木不是资源覆盖任务，而是**替换/覆盖 TFC 原有种植、收获、掉落和采收/再生流程**；
> 同时 A 87、TFC 29、B 43 共用生产链/六环节/九工序。
> 不再存在“资源覆盖 vs 生产链”的二选一；资源只是覆盖层的一部分。
> 当前生产/培育链完成度仍为 0，下一步按 291/292 的批次施工。"""
if old not in t:
    raise SystemExit("288 conclusion block missing")
p.write_text(t.replace(old, new), encoding="utf-8")
print("288 conclusion fixed")
