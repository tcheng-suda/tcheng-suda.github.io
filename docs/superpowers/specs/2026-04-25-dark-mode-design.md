# Dark Mode Toggle Design

## Summary

Add a light/dark mode toggle to the academic website. Users can manually switch themes via a button in the navigation bar. The site auto-detects system preference on first visit and persists the user's choice in `localStorage`.

## Approach: CSS Variables + `data-theme` Attribute

All colors are defined as CSS custom properties on `:root` (light) and `[data-theme="dark"]` (dark). A toggle button in the nav bar switches the `data-theme` attribute on `<html>`.

## CSS Variables

### Light (default, `:root`)

```
--bg-primary: #fdfdfd
--text-primary: #111
--header-bg: #1661BC
--header-text: #ffffff
--brand-color: #0077CC
--border-color: #e0e0e0
--code-bg: #eef
--card-bg: rgba(22,97,188,0.06)
--sub-menu-bg: #ffffff
--sub-menu-text: #1e1a15
--grey-color: #828282
--heading-color: #1e1a15
--footer-text: #828282
--link-hover-text: #111
--listing-time-color: #333
--talk-meta-color: #555
--talk-type-bg: #1661BC
--talk-type-text: #fff
--link-grid-border: #ddd
--link-grid-hover-bg: #eef5fc
--photo-caption-gradient: rgba(0,0,0,0.6)
```

### Dark (`[data-theme="dark"]`)

```
--bg-primary: #1a1a2e
--text-primary: #e0e0e0
--header-bg: #0d1b2a
--header-text: #e0e0e0
--brand-color: #5dade2
--border-color: #333
--code-bg: #2d2d44
--card-bg: rgba(93,173,226,0.08)
--sub-menu-bg: #16213e
--sub-menu-text: #e0e0e0
--grey-color: #999
--heading-color: #e0e0e0
--footer-text: #999
--link-hover-text: #e0e0e0
--listing-time-color: #aaa
--talk-meta-color: #aaa
--talk-type-bg: #5dade2
--talk-type-text: #1a1a2e
--link-grid-border: #444
--link-grid-hover-bg: rgba(93,173,226,0.12)
--photo-caption-gradient: rgba(0,0,0,0.7)
```

## Toggle Button

- Location: last item in the `<ul class="menu">` in `_includes/nav.html`
- Icon: Font Awesome `fa-sun` (light) / `fa-moon` (dark) — FA 4.3.0 is already loaded
- Click handler: toggles `data-theme` between `light` and `dark` on `<html>`, updates icon, saves to `localStorage`

## Flash Prevention

An inline `<script>` in `_includes/head.html` runs before rendering:
1. Check `localStorage` for saved theme
2. If none, check `prefers-color-scheme: dark` media query
3. Set `data-theme` on `<html>` accordingly

## Files to Modify

| File | Change |
|------|--------|
| `css/main.scss` | Add CSS variable definitions for `:root` and `[data-theme="dark"]` |
| `_sass/_base.scss` | Replace hardcoded colors with CSS variables |
| `_sass/_header.scss` | Replace hardcoded colors with CSS variables |
| `_sass/_layout.scss` | Replace hardcoded colors with CSS variables |
| `_sass/_mobile-header.scss` | Replace hardcoded colors with CSS variables |
| `_sass/_syntax-highlighting.scss` | Adapt code highlighting for dark mode |
| `_includes/nav.html` | Add toggle button `<li>` at end of menu |
| `_includes/head.html` | Add anti-flash inline `<script>` |
