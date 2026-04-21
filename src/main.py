import os
import shutil
import sys

from static_public import copy_source_to_destination
from content_generator import generate_pages_recursive


static_path = "./static"
public_path = "./docs"
content_path = "./content"
template_path = "./template.html"
default_path = "/"


def main():
    basepath = default_path
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    #check for destination, if present remove it
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
        print("<=== Deleted Public Directory ===>")
    
    #copy source to destination
    copy_source_to_destination(static_path, public_path)
    print("<=== Copied Static to Public ===>")

    #generate template in destination
    print("<=== Generate HTML pages ===>")
    generated_templates = generate_pages_recursive(content_path, template_path, public_path, basepath)
    print(f"<=== {generated_templates} ===>")

    return f'Process Complete!!'

result = main()
print(result)
