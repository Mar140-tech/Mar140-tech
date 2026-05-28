## 2025-05-14 - [Accessible Tab Navigation Pattern]
**Learning:** In a full-stack environment where the frontend is a single HTML file without a build step, accessibility improvements can be implemented using semantic HTML and ARIA roles. Replacing non-semantic `div` tabs with `button` elements and adding keyboard event listeners significantly improves navigation for screen readers and keyboard users.
**Action:** Always use semantic `button` elements for tabs, implement `role="tablist"`/`role="tab"`/`role="tabpanel"`, and support Arrow keys, Home, and End for keyboard navigation.
