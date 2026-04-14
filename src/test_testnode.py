import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_ne_text(self):
        node = TextNode("This is text", TextType.TEXT)
        node2 = TextNode("This is some more text", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_ne_text_type(self):
        node = TextNode("Stylized text!", TextType.BOLD)
        node2 = TextNode("Stylized text!", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("Hello", TextType.TEXT)
        self.assertEqual("TextNode(Hello, text, None)", repr(node))

    def test_url_needed(self):
        node = TextNode("This is a link", TextType.LINK, "google.com")
        self.assertIsNotNone(node.url)

    def test_url_not_needed(self):
        node = TextNode("This is not a link", TextType.TEXT)
        self.assertIsNone(node.url)
