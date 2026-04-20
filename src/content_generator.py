import os.path

from static_public import (
    list_directory_content,
    create_new_directory,
)

from markdown_blocks import (
    markdown_to_html_node,
)
def extract_title(markdown):
    blocks = markdown.strip().split("\n\n")
    if not blocks[0].startswith("#"):
        raise Exception("Missing Title: No h1")
    return blocks[0][2:]

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content = list_directory_content(dir_path_content)
    print(f'{"="*10}\nContent: {content}\n{"="*10}')
    print("\n")
    for c in content:
        src = os.path.join(dir_path_content, c)
        dst = os.path.join(dest_dir_path, c)

        if not os.path.isfile(src):
            create_new_directory(dst)
            generate_pages_recursive(src, template_path, dst)
        else:
            print(f"Generating new template at {dest_dir_path}")
            generate = generate_page(src, template_path, dest_dir_path)
            print(f"{c} - {generate}")

    return f"Copied Content to Public!"

def generate_page(from_path, template_path, dest_path):
    print(f"<== Generating Path: {from_path}\n\n to Destination: {dest_path}\n\n using {template_path} ==>\n")
    
    # access markdown to generate html and title from Source path
    with open(from_path) as md:
        markdown = md.read()
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        title = extract_title(markdown)

    # access template to inject title and html
    t = str("{{ Title }}")
    h = str("{{ Content }}")

    with open(template_path) as tmp:
        template = tmp.read()
        new_template = template.replace(t,title)
        new_template = new_template.replace(h, html)
    
    #Create new template in Destination path
    path = os.path.join(dest_path, "index.html")
    with open(path, "w") as h:
        h.write(new_template)

    return f"New HTML Generated!!"