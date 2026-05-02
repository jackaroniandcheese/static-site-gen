from block_markdown import markdown_to_blocks
import unittest

class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_excessive_newlines(self):
        md = """
This is **bolded**

This is _italic_







There are a bunch of excessive newlines but they shouldn't be in the blocks list
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded**",
                "This is _italic_",
                "There are a bunch of excessive newlines but they shouldn't be in the blocks list"
            ]
        )

    def test_whitespace(self):
        md = """
    whitespace both sides             

none left but some at the right

     none right but some at the left
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "whitespace both sides",
                "none left but some at the right",
                "none right but some at the left"
            ]
        )
