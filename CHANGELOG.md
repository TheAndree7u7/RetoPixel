# Changelog

All notable changes to RetoPixel are documented here.  
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- CSS custom properties (design tokens) for the entire colour palette and spacing scale.
- CRT scanline overlay (`body::after`) for an authentic pixel-display feel.
- Neon glow animation on the `<h1>` title (`glowPulse` keyframe).
- Entrance animation for the login card (`fadeSlideIn` keyframe).
- `prefers-reduced-motion` media query override — all animations disabled for users who prefer it.
- Inline SVG favicon — zero external network request.
- Open Graph and Twitter Card meta tags for social preview.
- `<meta name="theme-color">` for browser UI tinting on mobile.
- Skip-navigation link (`.sr-only`) for keyboard / screen-reader users.
- `<noscript>` notice confirming the page works without JavaScript.
- `aria-required="true"` attributes on form inputs.
- `novalidate` on `<form>` to allow custom validation UX in the future.
- `spellcheck="false"` on the username input.
- Explicit `font-family: inherit` and `font-size: 1rem` on the submit button.
- `focus-visible` outline on the submit button for keyboard accessibility.
- `LICENSE` (MIT).
- `CONTRIBUTING.md` — setup, workflow, and style guide.
- `CHANGELOG.md` (this file).
- GitHub issue templates (bug report + feature request).
- GitHub pull-request template.
- Dependabot configuration for GitHub Actions version updates.
- Expanded test suite: Open Graph tags, favicon, ARIA attributes, noscript block, CSS tokens, animations.

### Changed
- All hard-coded colour and radius values in `style.css` replaced with CSS custom properties.
- `README.md` updated with CI/Pages badges, expanded usage and contribution sections.

---

## [1.0.0] — Initial release

### Added
- Pixel-themed login interface (`index.html` + `style.css`).
- Python `unittest` smoke tests (`tests/test_static_site.py`).
- GitHub Actions CI workflow (`.github/workflows/ci.yml`).
- GitHub Pages deployment workflow (`.github/workflows/deploy-pages.yml`).
