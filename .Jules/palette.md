# Palette's UX Journal

## 2025-05-15 - Accessible Tabs with Keyboard Navigation
**Learning:** Converting non-semantic tab containers to ARIA-compliant button-based tablists significantly improves accessibility. Using `:focus-visible` with high-contrast outlines and `aria-selected` for state management ensures a consistent experience for both keyboard and screen reader users. Automatic activation (switching content on focus) provides a smoother interaction flow for small sets of tabs.
**Action:** Always use semantic `<button>` elements for tabs, implement the roving tabindex pattern, and ensure keyboard navigation (Arrows, Home, End) is supported with `event.preventDefault()` to avoid page scrolling.
