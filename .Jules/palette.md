# Palette's Journal

## 2026-06-18 - [Accessible Tab Refactor]
**Learning:** Refactoring non-semantic 'div' tabs to 'button' elements requires resetting browser-default properties like 'border' and 'color' to preserve the UI's visual integrity. Implementing the WAI-ARIA Tabs pattern with automatic activation (focus-based switching) significantly enhances the experience for keyboard and screen reader users.
**Action:** Use a complete CSS reset (border: none, color: inherit, etc.) when converting divs to buttons and strictly follow the roving tabindex pattern for keyboard-accessible components.

## 2026-06-23 - [Form and Icon Accessibility]
**Learning:** Decorative emojis in headers and buttons can be noisy for screen reader users if not hidden. Additionally, unlinked form labels reduce the clickable area and accessibility of inputs.
**Action:** Always wrap decorative icons/emojis in `aria-hidden="true"` and ensure every form input has a corresponding `<label for="...">` to improve both accessibility and click targets.
