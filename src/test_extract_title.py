import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_extract_title_with_spaces(self):
        self.assertEqual(extract_title("#   World   "), "World")

    def test_no_title(self):
        with self.assertRaises(Exception):
            extract_title("No headings here")

if __name__ == "__main__":
    unittest.main()
