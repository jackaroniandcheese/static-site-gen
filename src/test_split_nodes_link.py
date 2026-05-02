import unittest
from inline_markdown import split_nodes_link
from textnode import TextNode, TextType

class TestSplitNodesLink(unittest.TestCase):

    def test_split_links(self):
        node = TextNode(
            "Click here to go to [YouTube](youtube.com) or here to go to [Google](google.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Click here to go to ", TextType.TEXT),
                TextNode("YouTube", TextType.LINK, "youtube.com"),
                TextNode(" or here to go to ", TextType.TEXT),
                TextNode("Google", TextType.LINK, "google.com")
            ],
            new_nodes
        )

    def test_no_metadata(self):
        node = TextNode("This has no links, just raw text", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This has no links, just raw text", TextType.TEXT)
            ],
            new_nodes
        )
    
    def test_only_metadata(self):
        node = TextNode("[link1](google.com)[link2](youtube.com)[link3](reddit.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link1", TextType.LINK, "google.com"),
                TextNode("link2", TextType.LINK, "youtube.com"),
                TextNode("link3", TextType.LINK, "reddit.com")
            ],
            new_nodes
        )

    def test_non_text(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is an italic node", TextType.ITALIC)
            ],
            new_nodes
        )

