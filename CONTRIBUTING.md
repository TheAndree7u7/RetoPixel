# Contributing to RetoPixel

Thank you for taking the time to contribute! 🎮

---

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Project Structure](#project-structure)
4. [Branching Model](#branching-model)
5. [Making Changes](#making-changes)
6. [Running Tests](#running-tests)
7. [Submitting a Pull Request](#submitting-a-pull-request)
8. [Style Guide](#style-guide)

---

## Code of Conduct

Be respectful, inclusive, and constructive. We follow the
[Contributor Covenant](https://www.contributor-covenant.org/) principles.

---

## Getting Started

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/<your-username>/RetoPixel.git
   cd RetoPixel
   ```
3. **Create a branch** for your changes (see [Branching Model](#branching-model)).
4. Make your changes and run the tests (see [Running Tests](#running-tests)).
5. Open a Pull Request.

> **Prerequisites**: Python 3.9 or newer (only needed for tests).  
> The site itself requires no build step — open `index.html` directly in a browser.

---

## Project Structure

```
RetoPixel/
├── index.html          # Main entry point (static HTML)
├── style.css           # All styles (custom properties + components)
├── tests/
│   ├── __init__.py
│   └── test_static_site.py   # Python unittest smoke tests
├── .github/
│   ├── workflows/
│   │   ├── ci.yml              # CI: lint + test on push / PR
│   │   └── deploy-pages.yml    # Deploy to GitHub Pages on push to main
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   ├── pull_request_template.md
│   └── dependabot.yml
├── CHANGELOG.md
├── CONTRIBUTING.md     # (this file)
├── LICENSE
└── README.md
```

---

## Branching Model

| Branch pattern | Purpose |
|---|---|
| `main` | Production / GitHub Pages source |
| `feat/<name>` | New features |
| `fix/<name>` | Bug fixes |
| `docs/<name>` | Documentation-only changes |
| `chore/<name>` | Tooling, CI, dependencies |

---

## Making Changes

### HTML (`index.html`)

- Keep markup semantic and accessible.
- Every interactive element must have an accessible label.
- Run an HTML validator before committing (e.g. [validator.w3.org](https://validator.w3.org/)).

### CSS (`style.css`)

- **Always use CSS custom properties** (defined in `:root`) for colours, radii, and transitions.
  Do not add raw hex values — add a new token instead.
- Follow the section order in the file:
  1. Design tokens
  2. Reset
  3. Base
  4. Layout
  5. Components
  6. Animations
- Prefer `min()`, `clamp()`, and relative units (`rem`, `em`, `%`) over fixed `px`.

---

## Running Tests

From the repository root:

```bash
python -m unittest discover -s tests -v
```

The tests are fast pure-Python checks (no browser required). They validate:

- Required files exist.
- HTML language attribute is English.
- Core branding and form elements are present.
- Key CSS classes and design tokens are defined.
- Open Graph meta tags exist.
- ARIA attributes are present.

When adding a new HTML element or CSS class that should always exist, add a corresponding
test case in `tests/test_static_site.py`.

---

## Submitting a Pull Request

1. Ensure all tests pass locally.
2. Fill in the pull-request template completely.
3. Link any related issue with `Fixes #<issue-number>` in the PR description.
4. Keep PRs focused — one logical change per PR makes review faster.
5. CI will run automatically; address any failures before requesting review.

---

## Style Guide

| Item | Convention |
|---|---|
| Indentation | 2 spaces (HTML & CSS) |
| Quotes | Double quotes in HTML attributes |
| CSS property order | Follow existing file order (alphabetical within blocks) |
| Commit messages | `<type>: <short description>` (e.g. `feat: add remember-me checkbox`) |
| Commit types | `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore` |

---

Happy coding! 🕹️
