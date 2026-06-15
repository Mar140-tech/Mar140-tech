## 2025-05-14 - Accessible Tab Pattern with Automatic Activation
**Learning:** Implementing the WAI-ARIA tab pattern with 'automatic activation' (where focus change immediately switches content) provides a fluid experience for keyboard users in lightweight dashboards. It requires synchronized management of `aria-selected`, `tabindex`, and CSS focus-visible states.
**Action:** Use semantic `button` elements for tabs, set `role="tablist"` on the container, and ensure `e.preventDefault()` is used on Arrow keys to prevent side-effects like page scrolling.
