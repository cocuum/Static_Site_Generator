from textnode import TextNode, TextType

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