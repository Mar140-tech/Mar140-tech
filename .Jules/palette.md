# Palette's Journal

## 2026-06-18 - [Accessible Tab Refactor]
**Learning:** Refactoring non-semantic 'div' tabs to 'button' elements requires resetting browser-default properties like 'border' and 'color' to preserve the UI's visual integrity. Implementing the WAI-ARIA Tabs pattern with automatic activation (focus-based switching) significantly enhances the experience for keyboard and screen reader users.
**Action:** Use a complete CSS reset (border: none, color: inherit, etc.) when converting divs to buttons and strictly follow the roving tabindex pattern for keyboard-accessible components.

## 2026-06-25 - [Accessible Visual Indicators]
**Learning:** When visualizing complex data like signal strength bars, using a container with `role="img"` and a descriptive `aria-label` provides a clean, single announcement for screen readers. Internal text elements that are redundant to the `aria-label` should be hidden with `aria-hidden="true"` to prevent cluttered or repetitive speech output.
**Action:** Always pair visual-only indicators with a high-level `aria-label` on the wrapper and hide the implementation details (bars, redundant labels) from the accessibility tree.
