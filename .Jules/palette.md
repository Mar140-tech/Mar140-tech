## 2026-05-29 - [Accessible Tab Navigation]
**Learning:** Refactoring navigation tabs from non-semantic divs to buttons with ARIA roles (tablist, tab, tabpanel) significantly improves accessibility, but requires manual style resets (border, background) and explicit focus-visible states to maintain visual design.
**Action:** Always use semantic buttons for tabs and manage aria-selected/tabindex/hidden states via JS to ensure screen reader and keyboard compatibility.
