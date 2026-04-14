import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
   # node1 = HTMLNode()
   # node2 = HTMLNode("p", "Hello HTML", node1, {
    #                    "href": "https://www.google.com",
     #                   "target": "_blank",     
      #              })
    # node2_html = HTMLNode.props_to_html(node2)
    # print(node2_html)

    def test_props_to_html_one(self):
        node = HTMLNode(props={
                    "href": "https://www.google.com",
                    "target": "_blank",
                    }
                ) 
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_two(self):
        node1 = HTMLNode()
        self.assertEqual(node1.props_to_html(), "")

    def test_repr(self):
        node1 = HTMLNode(
            tag="p",
            value="Hello",
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        self.assertEqual("HTMLNode(p, Hello, None, {'href': 'https://www.google.com', 'target': '_blank'})", repr(node1))

