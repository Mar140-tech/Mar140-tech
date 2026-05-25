## 2024-05-24 - [Accessible Tab Navigation]
**Learning:** Using semantic `button` elements with ARIA roles (`tablist`, `tab`, `tabpanel`) and managing `aria-selected` and `tabindex` is essential for accessible tabbed interfaces. Standard `div` based tabs are invisible to screen readers and unreachable via keyboard.
**Action:** Always implement `role="tablist"`, `role="tab"`, and `role="tabpanel"` for tabbed interfaces, and ensure arrow key navigation is supported.
