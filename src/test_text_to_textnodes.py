import unittest
from inline_markdown import *

class TestTextToTextNodes(unittest.TestCase):

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertListEqual(
            [
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
            ],
            text_to_textnodes(text)
        )

    def test_text_textnodes2(self):
        text = "This is _italic_ first, then **bold** and then `code block` to see if order matters"
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" first, then ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and then ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" to see if order matters", TextType.TEXT)
            ],
            text_to_textnodes(text)
        )

    def test_invalid_syntax(self):
        text = "This is **text** with an _italic_ word and a `code block missing the second delimiter"
        with self.assertRaises(Exception):
            text_to_textnodes(text)

    def test_plaintext(self):
        text = "This is plaintext"
        self.assertListEqual(
            [
                TextNode("This is plaintext", TextType.TEXT)
            ],
            text_to_textnodes(text)
        )
    
    def test_no_text(self):
        self.assertListEqual([], text_to_textnodes(""))
