# RetoPixel

RetoPixel is a lightweight, pixel-inspired login interface built with pure HTML and CSS.
The repository is now fully documented in English and prepared for automated testing and
GitHub Pages deployment.

## Project Goal

The goal of RetoPixel is to provide a clean and reusable front-end challenge project with:

- A visual style aligned with a pixel/cyber aesthetic.
- Simple and semantic markup.
- No JavaScript dependency.
- Easy deployment through GitHub Pages.

## Tech Stack

- HTML5
- CSS3
- Python `unittest` (for repository smoke tests)
- GitHub Actions (CI + Pages deployment)

## Local Usage

1. Clone the repository.
2. Open `index.html` in your browser.

## Run Tests

From the repository root:

```bash
python -m unittest discover -s tests -v
```

These tests validate core static-site expectations (language, metadata, form structure,
and stylesheet presence).

## GitHub Pages Deployment

This repository includes a workflow at:

- `.github/workflows/deploy-pages.yml`

Deployment behavior:

- Runs on pushes to `main` and on manual dispatch.
- Publishes the root static site as a GitHub Pages artifact.

### One-time repository setup

In GitHub repository settings:

1. Go to **Settings > Pages**.
2. Set **Source** to **GitHub Actions**.
3. Ensure your default branch is `main` (or update the workflow branch trigger).

After that, every push to `main` will deploy the latest version automatically.
