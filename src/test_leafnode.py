import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node1 = LeafNode("p", "Hello, world!")
        self.assertEqual(node1.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node1.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_no_tag(self):
        node1 = LeafNode(None, "I forgot the tag for my leaf node!")
        self.assertEqual(node1.to_html(), "I forgot the tag for my leaf node!")

    def test_leaf_no_val(self):
        node1 = LeafNode("p", None)
        self.assertRaises(ValueError, node1.to_html)

    def test_repr(self):
        node1 = LeafNode("p", "This is a paragraph of text")
        self.assertEqual("LeafNode(p, This is a paragraph of text, None)", repr(node1))
