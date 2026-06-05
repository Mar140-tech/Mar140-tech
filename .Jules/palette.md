## 2025-05-15 - [Accessible Tab Pattern]
**Learning:** Converting `div`-based tabs to semantic `button` elements with the full WAI-ARIA Tab Panel pattern significantly improves accessibility for screen reader and keyboard users without compromising the visual design, provided default button styles are reset.
**Action:** Always use semantic `button` elements for tabs and implement roving tabindex with ARIA roles (`tablist`, `tab`, `tabpanel`) and states (`aria-selected`).
