import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise Exception("invalid markdown syntax")
        split_text = node.text.split(delimiter)
        
        for i in range(0, len(split_text)):
            if i % 2 == 0:
                new_node = TextNode(split_text[i], TextType.TEXT)
            else:
                new_node = TextNode(split_text[i], text_type)
            new_nodes.append(new_node)
        
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):    
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

