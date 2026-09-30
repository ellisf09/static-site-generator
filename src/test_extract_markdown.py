import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")],
            matches
        )

    def test_extract_multiple_images(self):
        matches = extract_markdown_images(
            "![a](url1) and ![b](url2)"
        )
        self.assertListEqual(
            [("a", "url1"), ("b", "url2")],
            matches
        )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "Here is a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [("link", "https://boot.dev")],
            matches
        )

    def test_extract_multiple_links(self):
        matches = extract_markdown_links(
            "[one](1.com) and [two](2.com)"
        )
        self.assertListEqual(
            [("one", "1.com"), ("two", "2.com")],
            matches
        )

    def test_no_images(self):
        matches = extract_markdown_images("No images here")
        self.assertListEqual([], matches)

    def test_no_links(self):
        matches = extract_markdown_links("No links here")
        self.assertListEqual([], matches)

if __name__ == "__main__":
    unittest.main()
