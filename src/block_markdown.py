from enum import Enum
from htmlnode import HTMLNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):

    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    
    for line in lines:
        if line.startswith(">"):
            continue
        else:
            break
    else:
        return BlockType.QUOTE
    
    for line in lines:
        if line.startswith("- "):
            continue
        else:
            break
    else:
        return BlockType.UNORDERED_LIST
    
    i = 0
    for j in range(1, len(lines) + 1):
        if lines[i].startswith(f"{j}. "):
            i+=1
            continue
        else:
            break
    else:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    for i in range(len(blocks)):
        blocks[i] = blocks[i].strip()
    return [b for b in blocks if b != ""]

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                text = block.replace("\n", " ")
                children.append(ParentNode("p", text_to_children(text)))
            case BlockType.HEADING:
                level = block[:7].count("#")
                text = block.lstrip("#").lstrip(" ")
                children.append(ParentNode(f"h{level}", text_to_children(text)))
            case BlockType.QUOTE:
                lines = block.split("\n")
                cleaned = [line.lstrip(">").strip() for line in lines]
                text = " ".join(cleaned)
                children.append(ParentNode("blockquote", text_to_children(text)))
            case BlockType.UNORDERED_LIST:
                lines = block.split("\n")
                cleaned = [line.lstrip("-").strip() for line in lines]
                list_items = [ParentNode("li", text_to_children(line)) for line in cleaned]
                children.append(ParentNode("ul", list_items))
            case BlockType.ORDERED_LIST:
                lines = block.split("\n")
                cleaned = [line.split(". ", maxsplit=1)[1] for line in lines]
                list_items = [ParentNode("li", text_to_children(line)) for line in cleaned]
                children.append(ParentNode("ol", list_items))
            case BlockType.CODE:
                inner_text = block[4:-3]
                text_node = TextNode(inner_text, TextType.TEXT)
                code_node = ParentNode("code", [text_node_to_html_node(text_node)])
                children.append(ParentNode("pre", [code_node]))

    return ParentNode("div", children)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes
