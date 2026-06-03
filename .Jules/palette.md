## 2025-05-14 - Accessible Tab Navigation Pattern
**Learning:** For full-stack applications with tabbed interfaces, using semantic `button` elements with ARIA roles (`tablist`, `tab`, `tabpanel`) significantly improves accessibility for screen readers and keyboard-only users. Managing `tabindex` and focus during tab switching is crucial for a smooth UX.
**Action:** Always implement ARIA-compliant tab patterns with keyboard support (Arrow keys, Home, End) in similar interfaces.

## 2025-05-14 - Real-time Feedback via Timestamps
**Learning:** In dashboards that fetch data periodically, providing a "Last Updated" timestamp gives users confidence that the information is current and the backend connection is active.
**Action:** Synchronize a visible timestamp whenever data fetching successfully completes.
