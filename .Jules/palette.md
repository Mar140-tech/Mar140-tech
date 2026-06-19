# Palette's Journal

This journal contains critical UX and accessibility learnings discovered during the development of the WiFi Scanner Pro project.

## 2026-06-19 - Accessible WAI-ARIA Tabs
**Learning:** Converting `div` based tabs to semantic `button` elements with proper ARIA roles and roving `tabindex` significantly improves keyboard navigability and screen reader support without compromising the existing visual design.
**Action:** Always use semantic elements for interactive components and implement WAI-ARIA patterns (like `role="tablist"`) to ensure accessibility is baked in.
