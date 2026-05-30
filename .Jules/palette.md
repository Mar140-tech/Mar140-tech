# Palette's UX Journal - WiFi Scanner Pro

## 2023-10-27 - Accessible Tab Navigation Pattern
**Learning:** In many full-stack mockups, navigation tabs are often implemented as simple `div` elements with click listeners. This breaks keyboard accessibility as they aren't focusable and don't announce their role to screen readers. Using a `role="tablist"` with `button` elements as `role="tab"` is the standard for accessible interactive tabs.
**Action:** Always refactor `div`-based tabs to semantic `button` elements with ARIA attributes and implement arrow key navigation to meet WCAG standards.
