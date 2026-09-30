from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from blocktype import BlockType
from parentnode import ParentNode
from leafnode import LeafNode
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node

def text_to_children(text):
    nodes = text_to_textnodes(text)
    return [text_node_to_html_node(n) for n in nodes]

def paragraph_to_html(block):
    block=block.replace("\n", " ")
    children=text_to_children(block)
    return ParentNode("p", children)
def heading_to_html(block):
    level = 0
    for c in block:
        if c == "#":
            level += 1
        else:
            break
    text = block[level+1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html(block):
    inner = block[3:-3]
    code_node = LeafNode("code", inner)
    return ParentNode("pre", [code_node])

def quote_to_html(block):
    lines = block.split("\n")
    stripped = "\n".join(line[1:].lstrip() for line in lines)
    children = text_to_children(stripped)
    return ParentNode("blockquote", children)

def unordered_list_to_html(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        items.append(ParentNode("li", children))
    return ParentNode("ul", items)

def ordered_list_to_html(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        text = line.split(". ", 1)[1]
        children = text_to_children(text)
        items.append(ParentNode("li", children))
    return ParentNode("ol", items)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        t = block_to_block_type(block)
        if t == BlockType.PARAGRAPH:
            children.append(paragraph_to_html(block))
        elif t == BlockType.HEADING:
            children.append(heading_to_html(block))
        elif t == BlockType.CODE:
            children.append(code_to_html(block))
        elif t == BlockType.QUOTE:
            children.append(quote_to_html(block))
        elif t == BlockType.UNORDERED_LIST:
            children.append(unordered_list_to_html(block))
        elif t == BlockType.ORDERED_LIST:
            children.append(ordered_list_to_html(block))
    return ParentNode("div", children)
