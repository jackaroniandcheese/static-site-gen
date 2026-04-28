import unittest
from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
   # unittest.util._MAX_LENGTH = 999999999    

    def test_text(self):
        node = TextNode("This is simply raw text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.TEXT)
        self.assertEqual(
                f"{new_nodes}",
                "[TextNode(This is simply raw text, text, None)]"
                )

    def test_bold(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
                f"{new_nodes}",
                "[TextNode(This is text with a , text, None), TextNode(bolded phrase, bold, None), TextNode( in the middle, text, None)]"
                )

    def test_italic(self):
        node = TextNode("This is text with an _italicized phrase_ in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
                f"{new_nodes}",
                "[TextNode(This is text with an , text, None), TextNode(italicized phrase, italic, None), TextNode( in the middle, text, None)]"
                )

    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
                f"{new_nodes}",
                "[TextNode(This is text with a , text, None), TextNode(code block, code, None), TextNode( word, text, None)]"
                )

    def test_invalid_syntax(self):
        node = TextNode("This is text that is **incorrectly** using **bold lettering", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)
