# Palette's Journal

## 2026-06-18 - [Accessible Tab Refactor]
**Learning:** Refactoring non-semantic 'div' tabs to 'button' elements requires resetting browser-default properties like 'border' and 'color' to preserve the UI's visual integrity. Implementing the WAI-ARIA Tabs pattern with automatic activation (focus-based switching) significantly enhances the experience for keyboard and screen reader users.
**Action:** Use a complete CSS reset (border: none, color: inherit, etc.) when converting divs to buttons and strictly follow the roving tabindex pattern for keyboard-accessible components.

## 2026-06-25 - [Secure Notification Pattern]
**Learning:** Using 'innerHTML' to inject notification messages is a major security risk for XSS, especially when the message contains dynamic data. Even if currently static, it sets a dangerous precedent.
**Action:** To prevent XSS when adding icons to notifications, use safe DOM manipulation: use 'createElement' or 'innerHTML' for the static icon part, but strictly use 'textContent' or 'document.createTextNode' for the dynamic message body.
