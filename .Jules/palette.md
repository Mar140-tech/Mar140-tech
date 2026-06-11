## 2026-06-11 - [Accessible Tabs Implementation]
**Learning:** Implementing WAI-ARIA tabs requires more than just roles; it needs keyboard management (arrow keys), focus management (tabindex cycle), and explicit associations (aria-controls/aria-labelledby). Using semantic <button> elements for tabs simplifies focus management significantly compared to <div>.
**Action:** Always prefer <button> for tabs and ensure 'aria-selected' and 'tabindex' are synchronized with the active state in JavaScript.
