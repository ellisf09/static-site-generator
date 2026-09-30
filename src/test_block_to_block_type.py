import unittest
from block_to_block_type import block_to_block_type
from blocktype import BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(
            block_to_block_type("# Heading"),
            BlockType.HEADING
        )
        self.assertEqual(
            block_to_block_type("###### Small"),
            BlockType.HEADING
        )

    def test_not_heading_without_space(self):
        self.assertEqual(
            block_to_block_type("###NoSpace"),
            BlockType.PARAGRAPH
        )

    def test_code_block(self):
        block = "```\nprint('hi')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote_block(self):
        block = "> line1\n> line2"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- item1\n- item2"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_wrong_numbers(self):
        block = "1. first\n3. second"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraph(self):
        block = "This is a normal paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
