# Palette's Journal

## 2026-06-18 - [Accessible Tab Refactor]
**Learning:** Refactoring non-semantic 'div' tabs to 'button' elements requires resetting browser-default properties like 'border' and 'color' to preserve the UI's visual integrity. Implementing the WAI-ARIA Tabs pattern with automatic activation (focus-based switching) significantly enhances the experience for keyboard and screen reader users.
**Action:** Use a complete CSS reset (border: none, color: inherit, etc.) when converting divs to buttons and strictly follow the roving tabindex pattern for keyboard-accessible components.

## 2026-06-19 - [Centralized Notification Icons]
**Learning:** Adding status-specific icons (✅, ❌, ℹ️) to a centralized 'showNotification' function can lead to visual duplication if existing call sites already include emojis in their message strings. This creates a cluttered UI and redundant information for screen readers.
**Action:** Audit and sanitize all existing calls to feedback functions when adding centralized decorative elements, and use safe DOM manipulation (like text nodes) for the dynamic message body to prevent XSS.
