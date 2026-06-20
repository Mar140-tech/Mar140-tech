## 2025-05-15 - Accessible Tabs Pattern
**Learning:** Converting `div`-based tabs to semantic `button` elements with WAI-ARIA roles (`tablist`, `tab`, `tabpanel`) significantly improves screen reader navigation and keyboard accessibility. Automatic activation (switching content on focus) is a smooth micro-UX pattern for this app's dashboard.
**Action:** Always use the `button` element for interactive tabs and implement `ArrowRight`, `ArrowLeft`, `Home`, and `End` keyboard handlers to follow the WAI-ARIA Tab pattern.

## 2025-05-15 - Decorative Emoji Handling
**Learning:** Screen readers often announce emojis in headers and buttons, which can be repetitive or confusing.
**Action:** Wrap decorative emojis in `<span aria-hidden="true">` to prevent them from being announced while keeping them visually present for sighted users.
