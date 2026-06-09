## 2025-05-15 - [Accessible Tabs Pattern]
**Learning:** Converting non-semantic `div` tabs to semantic `button` elements with a `role="tablist"` container significantly improves accessibility while preserving layout when CSS resets are applied. Keyboard navigation (arrows, home, end) and roving `tabindex` are essential for a complete implementation.
**Action:** Use `button` elements for tabs, manage `aria-selected` and `tabindex` in the `switchTab` function, and add a `keydown` listener to the tablist for standard keyboard interactions.
