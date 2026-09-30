import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_basic(self):
        node = HTMLNode(
            tag="a",
            props={"href": "https://google.com", "target": "_blank"}
        )
        expected = ' href="https://google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p", props={})
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode(tag="p", value="Hello", props={"class": "text"})
        rep = repr(node)
        self.assertIn("tag='p'", rep)
        self.assertIn("value='Hello'", rep)
        self.assertIn("props={'class': 'text'}", rep)

if __name__ == "__main__":
    unittest.main()
