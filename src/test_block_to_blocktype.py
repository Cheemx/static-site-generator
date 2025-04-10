import unittest

from blocknode import block_to_block_type, BlockType


class BlockTOBlockType(unittest.TestCase):
    def test_block_to_blocktype_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_to_blocktype_code(self):
        block = "```code block```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    
    def test_block_to_blocktype_quote(self):
        block = "> a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_block_to_blocktype_unordered_list(self):
        block = "- item"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
    
    def test_block_to_blocktype_ordered_list(self):
        block = "1. item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_block_to_blocktype_ordered_paragraph(self):
        block = "just a paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)