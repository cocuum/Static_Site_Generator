import re

from textnode import TextNode, TextType

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

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
        
        text = node.text
        parsed_images = extract_markdown_images(text)

        if len(parsed_images) == 0:
            new_nodes.append(node)
            continue

        for image in parsed_images:
            
            parsed_text = text.split(f'![{image[0]}]({image[1]})', 1)
            
            if len(parsed_text) != 2:
                raise ValueError("invalid markdown: missing formatting element")
            
            if parsed_text[0] != "":
                new_nodes.append(TextNode(parsed_text[0], TextType.TEXT))
            
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))

            text = parsed_text[1]
        
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
            
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        text = node.text
        parsed_link = extract_markdown_links(text)

        if len(parsed_link) == 0:
            new_nodes.append(node)
            continue

        for link in parsed_link:

            parsed_text = text.split(f'[{link[0]}]({link[1]})', 1)

            if len(parsed_text) != 2:
                raise ValueError("invalid markdown: missing formatting element")

            if parsed_text[0] != "":
                new_nodes.append(TextNode(parsed_text[0], TextType.TEXT))

            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))

            text = parsed_text[1]
        
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes
