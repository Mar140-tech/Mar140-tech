## 2026-06-07 - [Accessible Tab Navigation]
**Learning:** Using `div` for tabs prevents keyboard access and hides state from screen readers. Implementing the WAI-ARIA Tab Pattern with semantic `button` elements and arrow-key navigation provides a robust and expected UX for power users and assistive technology.
**Action:** Always use `<button>` for tabs and implement `role="tablist"`, `role="tab"`, and `role="tabpanel"` with proper keyboard event listeners for horizontal navigation.
