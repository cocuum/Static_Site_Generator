import shutil
import os
import os.path

from markdown_blocks import markdown_to_html_node, extract_title

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



def copy_source_to_destination(source, destination):
    print(f"<== Source: {source}\n to \nDestination: {destination} ==>\n")
    content = list_directory_content(source)
    for c in content:
        src = os.path.join(source, c)
        dst = os.path.join(destination, c)

        if not os.path.isfile(src):
            create_new_directory(dst)
            copy_source_to_destination(src, dst)
        else:
            copy_content(src, dst)

    return f"Copied Static to Public!"

def directory_check(destination):
    result = os.path.exists(destination)
    return result

def list_directory_content(location):
    result = os.listdir(location)
    return result

def create_new_directory(destination):
    os.mkdir(destination)

def copy_content(source, destination):
    shutil.copy(source, destination)

def remove_destination(destination):
    shutil.rmtree(destination)
