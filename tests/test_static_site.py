from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
INDEX_HTML = REPO_ROOT / "index.html"
STYLE_CSS = REPO_ROOT / "style.css"


class StaticSiteTests(unittest.TestCase):
    def test_index_file_exists(self):
        self.assertTrue(INDEX_HTML.exists(), "index.html should exist in repository root.")

    def test_style_file_exists(self):
        self.assertTrue(STYLE_CSS.exists(), "style.css should exist in repository root.")

    def test_html_is_in_english(self):
        content = INDEX_HTML.read_text(encoding="utf-8")
        self.assertIn('<html lang="en">', content)

    def test_retropixel_branding_exists(self):
        content = INDEX_HTML.read_text(encoding="utf-8")
        self.assertIn("RetoPixel", content)
        self.assertIn("Pixel Login Challenge", content)

    def test_login_fields_exist(self):
        content = INDEX_HTML.read_text(encoding="utf-8")
        self.assertIn('id="username"', content)
        self.assertIn('id="password"', content)
        self.assertIn("type=\"submit\"", content)

    def test_css_contains_key_classes(self):
        css = STYLE_CSS.read_text(encoding="utf-8")
        self.assertIn(".login-box", css)
        self.assertIn(".submit-button", css)


if __name__ == "__main__":
    unittest.main()
