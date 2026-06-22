# Palette's Journal

## 2026-06-18 - [Accessible Tab Refactor]
**Learning:** Refactoring non-semantic 'div' tabs to 'button' elements requires resetting browser-default properties like 'border' and 'color' to preserve the UI's visual integrity. Implementing the WAI-ARIA Tabs pattern with automatic activation (focus-based switching) significantly enhances the experience for keyboard and screen reader users.
**Action:** Use a complete CSS reset (border: none, color: inherit, etc.) when converting divs to buttons and strictly follow the roving tabindex pattern for keyboard-accessible components.

## 2026-06-20 - [Accessibility and Feedback Polish]
**Learning:** For asynchronous buttons that change state (e.g., adding a spinner and changing text), ensuring the button remains a consistent size prevents layout shifts. Additionally, when implementing a shared notification system, clearing the global timeout before starting a new one is essential to prevent stale timeouts from hiding fresh messages.
**Action:** Use state-managed variables for notification timeouts and always apply `aria-hidden="true"` to decorative icons/emojis in headers and buttons to optimize the screen reader experience.
