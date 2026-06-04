## 2026-06-04 - Semantic and Accessible Tabs
**Learning:** Converting non-semantic tab systems (divs) to semantic buttons with a role="tablist" significantly improves keyboard and screen reader accessibility. Implementing the Roving Tabindex pattern along with Arrow key, Home, and End navigation provides a professional and intuitive user experience.
**Action:** Use <button role="tab"> within a role="tablist" for any tabbed navigation and ensure aria-selected and tabindex are managed dynamically.

## 2026-06-04 - Screen Reader Noise Reduction
**Learning:** Decorative emojis in buttons and headers can cause unnecessary noise for screen reader users.
**Action:** Wrap decorative emojis in <span aria-hidden="true"> to hide them from assistive technologies while keeping them visible for visual users.
