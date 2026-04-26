from enum import Enum
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
            #This should return a LeafNode with no tag, just a raw text value.
        case TextType.BOLD:
            #This should return a LeafNode with a "b" tag and the text
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            #"i" tag, text
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            #"code" tag, text
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            #"a" tag, text, href prop
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            #"img" tag, empty str, "src" and "alt" props
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError("TextType not found")

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        all_eq = (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
        return True if all_eq == True else False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

