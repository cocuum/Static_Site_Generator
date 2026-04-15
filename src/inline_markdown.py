import re
from textnode import TextNode, TextType

def extract_markdown_images(text):
    return re.findall(r'!\[([^\[\]]*)\]\(([^\(\)]*)\)', text)

def extract_markdown_links(text):
    return re.findall(r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)', text)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parsed_nodes = []
        parsed_text = node.text.split(delimiter)

        if len(parsed_text) % 2 == 0:
            raise ValueError("invalid markdown: missing formatting element")

        for i in range(len(parsed_text)):
            if parsed_text[i] == "":
                continue
            if i % 2 == 0:
                parsed_nodes.append(TextNode(parsed_text[i], TextType.TEXT))
            else:
                parsed_nodes.append(TextNode(parsed_text[i], text_type))
        
        new_nodes.extend(parsed_nodes)
    
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        parsed_nodes = []
        parsed_text = re.split(r'!\[([^\[\]]*)\]\(([^\(\)]*)\)', node.text)
        parsed_image = extract_markdown_images(node.text)

        if len(parsed_image) == 0:
            new_nodes.append(node)

        for i in range(len(parsed_text)):
            if parsed_text[i] == "":
                continue
            if i % 3 == 0:
                parsed_nodes.append(TextNode(parsed_text[i], TextType.TEXT))
            elif i % 3 == 1:
                parsed_nodes.append(TextNode(parsed_image[i//3][0], TextType.IMAGE, parsed_image[i//3][1]))
        
        new_nodes.extend(parsed_nodes)
    
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        parsed_nodes = []
        parsed_text = re.split(r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)', node.text)
        parsed_link = extract_markdown_links(node.text)

        if len(parsed_link) == 0:
            new_nodes.append(node)

        for i in range(len(parsed_text)):
            if parsed_text[i] == "":
                continue
            if i % 3 == 0:
                parsed_nodes.append(TextNode(parsed_text[i], TextType.TEXT))
            elif i % 3 == 1:
                parsed_nodes.append(TextNode(parsed_link[i//3][0], TextType.LINK, parsed_link[i//3][1]))
        
        new_nodes.extend(parsed_nodes)
    
    return new_nodes
        

        