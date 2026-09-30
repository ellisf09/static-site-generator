import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter

class TestSplitNodes(unittest.TestCase):
    def test_split_code(self):
        node = TextNode("This is `code` here", TextType.TEXT)
        new = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new), 3)
        self.assertEqual(new[0].text, "This is ")
        self.assertEqual(new[0].text_type, TextType.TEXT)
        self.assertEqual(new[1].text, "code")
        self.assertEqual(new[1].text_type, TextType.CODE)
        self.assertEqual(new[2].text, " here")
        self.assertEqual(new[2].text_type, TextType.TEXT)

    def test_split_bold(self):
        node = TextNode("Hello **world**!", TextType.TEXT)
        new = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new), 3)
        self.assertEqual(new[1].text_type, TextType.BOLD)
        self.assertEqual(new[1].text, "world")

    def test_split_italic(self):
        node = TextNode("This _is_ good", TextType.TEXT)
        new = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new[1].text_type, TextType.ITALIC)
        self.assertEqual(new[1].text, "is")

    def test_no_split_non_text(self):
        node = TextNode("bold", TextType.BOLD)
        new = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new), 1)
        self.assertEqual(new[0], node)

    def test_unmatched_delimiter_raises(self):
        node = TextNode("This is `broken", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_multiple_splits(self):
        node = TextNode("a `b` c `d` e", TextType.TEXT)
        new = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new), 5)
        self.assertEqual(new[1].text, "b")
        self.assertEqual(new[3].text, "d")

if __name__ == "__main__":
    unittest.main()
