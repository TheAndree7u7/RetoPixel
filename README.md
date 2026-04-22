# RetoPixel

[![CI](https://github.com/TheAndree7u7/RetoPixel/actions/workflows/ci.yml/badge.svg)](https://github.com/TheAndree7u7/RetoPixel/actions/workflows/ci.yml)
[![Deploy to Pages](https://github.com/TheAndree7u7/RetoPixel/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/TheAndree7u7/RetoPixel/actions/workflows/deploy-pages.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg)](LICENSE)

RetoPixel is a lightweight, pixel/cyber-inspired login interface built with **pure HTML and CSS** — no
JavaScript, no build step, no external dependencies.

---

## ✨ Features

| Feature | Details |
|---|---|
| **Pixel grid background** | CSS multi-layer `linear-gradient` tile pattern |
| **CRT scanline overlay** | `body::after` with `repeating-linear-gradient` |
| **Neon glow title** | `glowPulse` `@keyframes` animation |
| **Entrance animation** | `fadeSlideIn` on the login card |
| **Floating labels** | Pure CSS `:focus` / `:valid` selector trick |
| **CSS design tokens** | Full colour palette + radii defined in `:root` |
| **Accessible** | Skip-nav link, `aria-*` attributes, `focus-visible` styles |
| **Reduced-motion safe** | `prefers-reduced-motion` media query disables all animations |
| **Social preview** | Open Graph + Twitter Card meta tags |
| **Inline SVG favicon** | Zero external network request |

---

## 🗂 Project Structure

```
RetoPixel/
├── index.html              # Main entry point
├── style.css               # All styles (design tokens → components → animations)
├── tests/
│   ├── __init__.py
│   └── test_static_site.py # Python unittest smoke tests (30 cases)
├── .github/
│   ├── workflows/
│   │   ├── ci.yml              # CI: tests on push / PR
│   │   └── deploy-pages.yml    # Deploy to GitHub Pages on push to main
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   ├── pull_request_template.md
│   └── dependabot.yml          # Weekly Actions version updates
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE                 # MIT
└── README.md               # (this file)
```

---

## 🚀 Quick start

1. **Clone** the repository:
   ```bash
   git clone https://github.com/TheAndree7u7/RetoPixel.git
   cd RetoPixel
   ```
2. **Open** `index.html` in any modern browser — that's it.

> No `npm install`, no build command, no server required.

---

## 🧪 Tests

The test suite uses the Python standard library only (Python 3.9+).

```bash
python -m unittest discover -s tests -v
```

Tests cover:

- Required files exist.
- HTML language, charset, and viewport meta.
- Core branding and form elements.
- Accessibility: ARIA attributes, skip-nav link.
- Open Graph / Twitter Card meta tags.
- Inline favicon present.
- CSS: component classes, design tokens, keyframes, `prefers-reduced-motion`.
- Enforcement that **no raw hex values** appear outside `:root`.

---

## 🤖 GitHub Automation

### CI (`ci.yml`)

Runs on every push to `main` / `copilot/**` and on every pull request:

1. Checks out the repository.
2. Sets up Python 3.12.
3. Runs the full test suite.

### Deploy to Pages (`deploy-pages.yml`)

Runs on every push to `main` and can be triggered manually:

1. Checks out the repository.
2. Configures GitHub Pages.
3. Uploads the static site as a Pages artifact.
4. Deploys to GitHub Pages.

### Dependabot (`dependabot.yml`)

Automatically opens PRs every Monday to keep GitHub Actions versions up to date.

### One-time repository setup for GitHub Pages

1. Go to **Settings → Pages**.
2. Set **Source** to **GitHub Actions**.
3. Ensure your default branch is `main`.

After that, every push to `main` deploys the latest version automatically.

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide (setup, branching, style rules, and PR checklist).

---

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a full history of changes.

---

## 📄 License

[MIT](LICENSE) © 2024 TheAndree7u7
