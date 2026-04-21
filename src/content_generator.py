import os
from pathlib import Path

from markdown_blocks import (
    markdown_to_html_node,
)
def extract_title(markdown):
    blocks = markdown.strip().split("\n\n")
    if not blocks[0].startswith("#"):
        raise Exception("Missing Title: No h1")
    return blocks[0][2:]

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    content = os.listdir(dir_path_content)
    print(f'{"="*10}\nContent: {content}\n{"="*10}')
    for c in content:
        src = os.path.join(dir_path_content, c)
        dst = os.path.join(dest_dir_path, c)

        if not os.path.isfile(src):
            print(f"{"="*10}\nCreating Directory: {dst}\n{"="*10}")
            os.mkdir(dst)
            generate_pages_recursive(src, template_path, dst, basepath)
        else:
            print(f"Generating new template at {dest_dir_path}")
            generate = generate_page(src, template_path, dst, basepath)
            print(f"{generate[1]} ===> {generate[0]}")

    return f"Copied Content to Public!"

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"<== Generating Path: {from_path}\n\n to Destination: {dest_path}\n\n using {template_path} ==>\n")
    
    # access markdown to generate html and title from Source path
    with open(from_path) as md:
        markdown = md.read()
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        title = extract_title(markdown)

    # access template to inject title and html
    with open(template_path) as tmp:
        template = tmp.read()
        template = template.replace("{{ Title }}", title)
        template = template.replace("{{ Content }}", html)
        template = template.replace('href="/', f'href="{ basepath }')
        template = template.replace('src="/', f'src="{ basepath }')
    
    #Create new template in Destination path
    path = Path(dest_path).with_suffix(".html")
    print(f"path: {path}")
    with open(path, "w") as h:
        h.write(template)

    return path , f"New HTML Generated!!"