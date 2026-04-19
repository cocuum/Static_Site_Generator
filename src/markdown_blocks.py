from enum import Enum

from htmlnode import ParentNode
from markdown_inline import text_to_textnodes

from textnode import (
    TextNode,
    TextType,
    text_node_to_html_node,
)

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "order_list"

def extract_title(markdown):
    blocks = markdown.strip().split("\n\n")
    if not blocks[0].startswith("#"):
        raise Exception("Missing Title: No h1")
    title = heading_to_htmlnode(blocks[0])
    return title.children[0].to_html()

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    stripped_blocks = []

    for block in blocks:
        if block == "":
            continue
        stripped_blocks.append(block.strip())
    
    return stripped_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    if block.startswith("- "):
        i = 1
        for line in lines:
            new_line = line.strip()
            if new_line.startswith(f"{i}. "):
                i += 1
                continue
            if not new_line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    
    if block.startswith("1. "):
        i = 1
        for line in lines:
            new_line = line.strip()
            if new_line.startswith("- "):
                continue
            if not new_line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    
    return BlockType.PARAGRAPH

def text_to_children(text):
    children_htmlnodes = []
    textnodes = text_to_textnodes(text)

    for node in textnodes:
        child = text_node_to_html_node(node)
        children_htmlnodes.append(child)

    return children_htmlnodes

def paragraph_to_htmlnode(text):
    lines = text.split('\n')
    new_lines = " ".join(lines)
    if new_lines.startswith("!") or new_lines.startswith("["):
        tag = "div"
    else:
        tag = "p"
    children = text_to_children(new_lines)
    return ParentNode(tag, children)

def code_to_htmlnode(text):
    if not text.startswith("```") or not text.endswith("```"):
        raise ValueError("invalid code block: missing code block markdown")
    line = text[4:-3]
    textnode = TextNode(line, TextType.TEXT)
    node = text_node_to_html_node(textnode)
    result = ParentNode("code", [node])
    return ParentNode("pre", [result])

def heading_to_htmlnode(block):
    parts = block.split(" ", 1)

    if len(parts) != 2:
        raise ValueError("invalid heading markdown: missing heading text")
    if len(parts[0]) + 1 >= len(block):
        raise ValueError("invalid heading level")

    tag = f'h{len(parts[0])}'
    children = text_to_children(parts[1])
    return ParentNode(tag, children)

def ulist_to_htmlnode(block):
    parts = block.split("\n")
    listing = []
    for part in parts:
        children = text_to_children(part[2:])
        listing.append(ParentNode("li", children))
    return ParentNode("ul", listing)

def olist_to_htmlnode(block):
    parts = block.split("\n")
    listing = []
    
    for part in parts:
        line = part.split(". ", 1)
        children = text_to_children(line[1])
        listing.append(ParentNode("li", children))
    
    return ParentNode("ol", listing)

def quote_to_htmlnode(block):
    if not block.startswith(">"):
        raise ValueError("invalid heading markdown: missing heading text")
    
    parts = block.split("\n")
    new_lines = []
    
    for part in parts:
        new_lines.append(part.lstrip(">").strip())
    
    line = " ".join(new_lines)
    children = text_to_children(line)
    
    return ParentNode("blockquote", children)

def block_to_htmlnode(block):
    block_type = block_to_block_type(block)

    if block_type == BlockType.HEADING:
        return heading_to_htmlnode(block)
    
    elif block_type == BlockType.CODE:
        return code_to_htmlnode(block)
    
    elif block_type == BlockType.QUOTE:
        return quote_to_htmlnode(block)
    
    elif block_type == BlockType.ULIST:
        return ulist_to_htmlnode(block)
    
    elif block_type == BlockType.OLIST:
        return olist_to_htmlnode(block)
    
    elif block_type == BlockType.PARAGRAPH:
        return paragraph_to_htmlnode(block)
    
    raise ValueError("invalid block type")

def markdown_to_html_node(markdown):
    html_nodes=[]

    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        node = block_to_htmlnode(block)
        html_nodes.append(node)
    
    return ParentNode("div", html_nodes)