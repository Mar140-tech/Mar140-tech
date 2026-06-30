# Palette's Journal

## 2026-06-18 - [Accessible Tab Refactor]
**Learning:** Refactoring non-semantic 'div' tabs to 'button' elements requires resetting browser-default properties like 'border' and 'color' to preserve the UI's visual integrity. Implementing the WAI-ARIA Tabs pattern with automatic activation (focus-based switching) significantly enhances the experience for keyboard and screen reader users.
**Action:** Use a complete CSS reset (border: none, color: inherit, etc.) when converting divs to buttons and strictly follow the roving tabindex pattern for keyboard-accessible components.

## 2026-06-30 - [Accessible Data Visualization]
**Learning:** When replacing text with visual indicators like signal bars, applying 'role="img"' and a descriptive 'aria-label' (e.g., "Signal strength: Excellent") to the container ensures the status is clearly communicated to screen reader users, even when the underlying data is presented visually.
**Action:** Always provide a text-based interpretation of visual data via ARIA labels and hide decorative sub-elements with 'aria-hidden="true"'.
