# Palette's Journal - WiFi Scanner Pro

## 2025-05-14 - [Accessible Tab Implementation Patterns]
**Learning:** When refactoring non-semantic elements (like `div`) to semantic ones (like `button`) for tabs, specific attention must be paid to CSS property overrides. Using `border: none` in a general selector to reset button styles will override previously defined `border-bottom` styles on active states if the reset comes after or has equal specificity. Also, keyboard navigation for tabs (Arrow keys) must include `e.preventDefault()` to avoid unwanted page scrolling while navigating the tablist.
**Action:** Always place button resets before state-specific border definitions, or use specific resets like `border-top: none; border-left: none; border-right: none;` if a bottom border is required. Always prevent default behavior for navigation keys in focus-managed components.
