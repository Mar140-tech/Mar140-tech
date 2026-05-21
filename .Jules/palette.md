## 2025-05-14 - [Accessible Tabs]
**Learning:** Implementing tabs with semantic `button` elements and ARIA roles (`tablist`, `tab`, `tabpanel`) significantly improves keyboard navigability and screen reader support compared to using generic `div` elements. Managing `aria-selected` state via JavaScript is crucial for real-time feedback.
**Action:** Always prefer `button` elements for interactive tab controls and ensure `aria-selected`, `aria-controls`, and `aria-labelledby` are correctly linked.
