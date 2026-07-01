# Palette's Journal

## 2026-06-18 - [Accessible Tab Refactor]
**Learning:** Refactoring non-semantic 'div' tabs to 'button' elements requires resetting browser-default properties like 'border' and 'color' to preserve the UI's visual integrity. Implementing the WAI-ARIA Tabs pattern with automatic activation (focus-based switching) significantly enhances the experience for keyboard and screen reader users.
**Action:** Use a complete CSS reset (border: none, color: inherit, etc.) when converting divs to buttons and strictly follow the roving tabindex pattern for keyboard-accessible components.

## 2026-06-20 - [Signal Strength Visualization]
**Learning:** When adding qualitative labels (e.g., 'Excellent', 'Good') to technical data like WiFi signal strength, it's critical to keep the original quantitative value (dBm) visible for sighted users. Technical users often rely on exact values that labels may oversimplify. Using ARIA 'role="img"' on the visual bar container provides a clean, single announcement for screen readers.
**Action:** Always pair visual/qualitative indicators with their source quantitative data for expert users, and use robust ARIA labels to summarize complex visual patterns.
