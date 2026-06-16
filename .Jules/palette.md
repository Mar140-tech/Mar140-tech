## 2025-05-15 - Accessible Tab Navigation
**Learning:** Implementing semantic tabs with `role="tablist"` and `button` elements using a roving `tabindex` significantly improves keyboard discoverability. Automatic activation (switching content on focus) provides a more fluid micro-interaction for keyboard users in small-scale utility apps.
**Action:** Always prefer `button` over `div` for interactive tabs and implement `ArrowRight`/`ArrowLeft` navigation with `event.preventDefault()` to ensure a standard-compliant accessible experience.
