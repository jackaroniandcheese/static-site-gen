import unittest
from inline_markdown import split_nodes_image
from textnode import TextNode, TextType
class TestSplitNodesImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_no_metadata(self):
        node = TextNode(
            "This is text with no images or links to an image",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with no images or links to an image", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_only_metadata(self):
        node = TextNode("![image1](imgur.com/1)![image2](imgur.com/2)![image3](imgur.com/3)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image1", TextType.IMAGE, "imgur.com/1"),
                TextNode("image2", TextType.IMAGE, "imgur.com/2"),
                TextNode("image3", TextType.IMAGE, "imgur.com/3"),
            ],
            new_nodes,
        )

    def test_non_text(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is a bold node", TextType.BOLD)
            ],
            new_nodes,
        )

