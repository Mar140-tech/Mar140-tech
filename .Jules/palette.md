# Palette's Journal

## 2026-06-18 - [Accessible Tab Refactor]
**Learning:** Refactoring non-semantic 'div' tabs to 'button' elements requires resetting browser-default properties like 'border' and 'color' to preserve the UI's visual integrity. Implementing the WAI-ARIA Tabs pattern with automatic activation (focus-based switching) significantly enhances the experience for keyboard and screen reader users.
**Action:** Use a complete CSS reset (border: none, color: inherit, etc.) when converting divs to buttons and strictly follow the roving tabindex pattern for keyboard-accessible components.

## 2026-06-24 - [Micro-UX Scoping and UI Integrity]
**Learning:** Over-scoping a PR with multiple unrelated micro-UX improvements can lead to "repository pollution" and incomplete implementations (e.g., non-functional visual elements due to missing CSS).
**Action:** Strictly limit PRs to a single, high-impact micro-UX improvement (under 50 lines) and ensure all new UI components are fully styled and functional.
