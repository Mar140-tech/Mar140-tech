## 2026-05-11 - [Accessible Tabs]
**Learning:** Using divs for tabs makes them inaccessible to keyboard and screen reader users. Changing them to buttons and adding WAI-ARIA roles (tablist, tab, tabpanel) significantly improves the UX for all users.
**Action:** Always prefer semantic button elements for interactive tab headers and ensure aria-selected/aria-controls attributes are managed via JavaScript.
