"""
Smoke tests for the RetoPixel static site.

These tests validate that the core files exist and that the HTML/CSS content
meets the project's structural and accessibility requirements.  They run in CI
on every push / pull request and require no browser or external dependencies.

Run from the repository root:

    python -m unittest discover -s tests -v
"""

from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
INDEX_HTML = REPO_ROOT / "index.html"
STYLE_CSS = REPO_ROOT / "style.css"


class FileExistenceTests(unittest.TestCase):
    """Verify that required files are present in the repository."""

    def test_index_file_exists(self):
        self.assertTrue(INDEX_HTML.exists(), "index.html should exist in repository root.")

    def test_style_file_exists(self):
        self.assertTrue(STYLE_CSS.exists(), "style.css should exist in repository root.")


class HTMLStructureTests(unittest.TestCase):
    """Validate HTML content, meta tags, and accessibility attributes."""

    @classmethod
    def setUpClass(cls):
        cls.html = INDEX_HTML.read_text(encoding="utf-8")

    # ── Language & encoding ──────────────────────────────────────────────────

    def test_html_lang_is_english(self):
        self.assertIn('<html lang="en">', self.html)

    def test_charset_utf8(self):
        self.assertIn('charset="UTF-8"', self.html)

    def test_viewport_meta_present(self):
        self.assertIn('name="viewport"', self.html)

    # ── Branding ─────────────────────────────────────────────────────────────

    def test_title_contains_retopixel(self):
        self.assertIn("RetoPixel", self.html)

    def test_subtitle_present(self):
        self.assertIn("Pixel Login Challenge", self.html)

    # ── Form & input elements ─────────────────────────────────────────────────

    def test_username_input_exists(self):
        self.assertIn('id="username"', self.html)

    def test_password_input_exists(self):
        self.assertIn('id="password"', self.html)

    def test_submit_button_exists(self):
        self.assertIn('type="submit"', self.html)

    def test_labels_are_associated(self):
        self.assertIn('for="username"', self.html)
        self.assertIn('for="password"', self.html)

    # ── Accessibility ─────────────────────────────────────────────────────────

    def test_aria_labelledby_on_section(self):
        self.assertIn('aria-labelledby="retopixel-title"', self.html)

    def test_aria_required_on_inputs(self):
        self.assertGreaterEqual(
            self.html.count('aria-required="true"'),
            2,
            "Both username and password inputs should have aria-required='true'.",
        )

    def test_skip_navigation_link_present(self):
        self.assertIn('href="#login-form"', self.html)

    def test_noscript_element_present(self):
        self.assertIn("<noscript>", self.html)

    # ── Open Graph meta tags ──────────────────────────────────────────────────

    def test_og_title_present(self):
        self.assertIn('property="og:title"', self.html)

    def test_og_description_present(self):
        self.assertIn('property="og:description"', self.html)

    def test_og_type_present(self):
        self.assertIn('property="og:type"', self.html)

    # ── Favicon ───────────────────────────────────────────────────────────────

    def test_favicon_link_present(self):
        self.assertIn('rel="icon"', self.html)

    # ── Stylesheet link ───────────────────────────────────────────────────────

    def test_stylesheet_linked(self):
        self.assertIn('href="style.css"', self.html)


class CSSStructureTests(unittest.TestCase):
    """Validate CSS custom properties, component classes, and keyframes."""

    @classmethod
    def setUpClass(cls):
        cls.css = STYLE_CSS.read_text(encoding="utf-8")

    # ── Component classes ─────────────────────────────────────────────────────

    def test_login_box_class_present(self):
        self.assertIn(".login-box", self.css)

    def test_submit_button_class_present(self):
        self.assertIn(".submit-button", self.css)

    def test_user_box_class_present(self):
        self.assertIn(".user-box", self.css)

    # ── Design tokens ─────────────────────────────────────────────────────────

    def test_css_custom_properties_defined(self):
        self.assertIn(":root", self.css, "CSS custom properties should be defined in :root.")

    def test_accent_token_defined(self):
        self.assertIn("--color-accent", self.css)

    def test_background_token_defined(self):
        self.assertIn("--color-bg", self.css)

    # ── Animations ────────────────────────────────────────────────────────────

    def test_keyframes_defined(self):
        self.assertIn("@keyframes", self.css)

    def test_reduced_motion_query_present(self):
        self.assertIn("prefers-reduced-motion", self.css)

    # ── Accessibility helpers ─────────────────────────────────────────────────

    def test_sr_only_class_present(self):
        self.assertIn(".sr-only", self.css)

    # ── No raw hex colours outside :root ─────────────────────────────────────

    def test_no_raw_hex_outside_root(self):
        """Colours outside :root should use var(--...) not raw hex values."""
        # Remove the :root block and comments, then check for bare hex literals
        without_root = re.sub(r":root\s*\{[^}]*\}", "", self.css, flags=re.DOTALL)
        without_comments = re.sub(r"/\*.*?\*/", "", without_root, flags=re.DOTALL)
        # Allow hex inside url() / data URIs and inside rgba/rgb function calls
        without_data_uris = re.sub(r"url\([^)]*\)", "", without_comments)
        without_rgba = re.sub(r"rgba?\([^)]*\)", "", without_data_uris)
        bare_hex = re.findall(r"(?<!['\"])#[0-9a-fA-F]{3,8}\b", without_rgba)
        self.assertEqual(
            bare_hex,
            [],
            f"Raw hex colour(s) found outside :root — use CSS custom properties instead: {bare_hex}",
        )


if __name__ == "__main__":
    unittest.main()
