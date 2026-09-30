import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    def test_full_example(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` and an "
            "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a "
            "[link](https://boot.dev)"
        )
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(nodes, expected)

    def test_no_markdown(self):
        nodes = text_to_textnodes("hello world")
        self.assertEqual(nodes, [TextNode("hello world", TextType.TEXT)])

    def test_only_bold(self):
        nodes = text_to_textnodes("hi **there** friend")
        self.assertEqual(
            nodes,
            [
                TextNode("hi ", TextType.TEXT),
                TextNode("there", TextType.BOLD),
                TextNode(" friend", TextType.TEXT),
            ],
        )

    def test_only_italic(self):
        nodes = text_to_textnodes("a _b_ c")
        self.assertEqual(
            nodes,
            [
                TextNode("a ", TextType.TEXT),
                TextNode("b", TextType.ITALIC),
                TextNode(" c", TextType.TEXT),
            ],
        )

    def test_only_code(self):
        nodes = text_to_textnodes("run `this` now")
        self.assertEqual(
            nodes,
            [
                TextNode("run ", TextType.TEXT),
                TextNode("this", TextType.CODE),
                TextNode(" now", TextType.TEXT),
            ],
        )

if __name__ == "__main__":
    unittest.main()
