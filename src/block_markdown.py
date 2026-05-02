from enum import Enum

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
