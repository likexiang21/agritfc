from pathlib import Path

p = Path("mod_rebuild/docs/audit/OPEN-ISSUES.md")
t = p.read_text(encoding="utf-8")

old2 = "## OPEN-002 客户端大量 `Unknown recipe category: tfcagricultureplus:in_world/...`\n\n**状态：recorded / 未处理**"
new2 = """## OPEN-002 客户端大量 `Unknown recipe category: tfcagricultureplus:in_world/...`

**状态：fixed-static / runtime-unverified（2026-10-29）**

- 根因：`ClientRecipeBook` 跳过 `isSpecial()=true` 的配方；`MortarRecipe`/`FoodMixingBowlRecipe` 未覆盖；
- 已为两者补 `isSpecial() = true`；
- 4 个自定义 Recipe 全部通过 `check_recipe_is_special.py`；
- 18:28 日志来自旧 jar；当前源码已覆盖；
- 未实机确认日志消失；
- 证据：docs/536、537。"""
if old2 not in t:
    raise SystemExit("OPEN-002 anchor missing")
t = t.replace(old2, new2, 1)

old13 = "## OPEN-013 7 个研钵 knapping 配方共用同一 `tfc:rock` pattern\n\n**状态：recorded / 未处理**"
new13 = """## OPEN-013 7 个研钵 knapping 配方共用同一 `tfc:rock` pattern

**状态：resolved-static（2026-10-29）**

- 7 个 pestle 的 pattern 相同，但 `ingredient` 全部不同；
- TFC `KnappingRecipe.matches` 同时检查 `ingredient`；
- `check_pestle_disambiguation.py`：7/7 unique；
- 不存在实际配方冲突；未实机验证；
- 证据：docs/536、537。"""
if old13 not in t:
    raise SystemExit("OPEN-013 anchor missing")
t = t.replace(old13, new13, 1)
p.write_text(t, encoding="utf-8")
print("OPEN-002/013 updated")
