## 2025-05-15 - [Tab Component Accessibility Refactor]
**Learning:** When refactoring non-semantic elements (like `div`) to semantic ones (like `button`), reset shorthand properties like `border: none` *before* declaring specific properties like `border-bottom`. Shorthand resets can inadvertently override more specific styles if declared later in the CSS block, leading to visual regressions.
**Action:** Always place general CSS resets or shorthand property definitions at the top of a style block to ensure specific overrides remain effective.
