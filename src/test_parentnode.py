import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
                parent_node.to_html(),
                "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_great_grandchildren(self):
        great_grandchild_node = LeafNode("b", "child")
        grandchild_node = ParentNode("span", [great_grandchild_node])
        child_node = ParentNode("div", [grandchild_node])
        parent_node = ParentNode("body", [child_node])
        self.assertEqual(
                parent_node.to_html(),
                "<body><div><span><b>child</b></span></div></body>",
        )
    
    def test_no_tag(self):
        child_node = LeafNode("b", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_no_children(self):
        parent_node = ParentNode("body", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    # Method provided by boots
    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(parent_node.to_html(), '<div class="container"><span>child</span></div>')
