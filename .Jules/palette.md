# Palette's Journal

## 2026-06-18 - [Accessible Tab Refactor]
**Learning:** Refactoring non-semantic 'div' tabs to 'button' elements requires resetting browser-default properties like 'border' and 'color' to preserve the UI's visual integrity. Implementing the WAI-ARIA Tabs pattern with automatic activation (focus-based switching) significantly enhances the experience for keyboard and screen reader users.
**Action:** Use a complete CSS reset (border: none, color: inherit, etc.) when converting divs to buttons and strictly follow the roving tabindex pattern for keyboard-accessible components.

## 2026-06-25 - [Visual Signal Strength Indicators]
**Learning:** Raw technical data like dBm is often difficult for users to interpret quickly. Adding a 4-bar visual indicator alongside the numeric value provides immediate, intuitive feedback. Combining this with an `aria-label` that includes both a descriptive term (e.g., "Excellent") and the raw data ensures the information is accessible to both visual and screen reader users.
**Action:** When displaying complex technical metrics, always provide a simplified visual metaphor and ensure it is backed by descriptive ARIA labels for accessibility.
