## 2026-06-14 - [Accessible Tab Navigation Pattern]
**Learning:** Converting non-semantic div-based tabs to button elements with WAI-ARIA roles (tablist, tab, tabpanel) significantly improves keyboard discoverability and screen reader support without breaking existing CSS layouts if base button styles are properly reset.
**Action:** Always use semantic button elements for tabs and implement 'automatic activation' (focus + switch) via Arrow keys, Home, and End for a native-feeling navigation experience.
