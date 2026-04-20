from static_public import (
    copy_source_to_destination,
    create_new_directory,
    directory_check,
    remove_destination,
)

from content_generator import generate_pages_recursive


SRC = "./static"
DST = "./public"

fp = "./content"
tp = "./template.html"


def main():
    #check for destination, if present remove it
    print("<=== Delete Public Directory ===>")
    if directory_check(DST):
        remove_destination(DST)
    
    # create new destination
    print("<=== Create New Public Directory ===>")
    create_new_directory(DST)

    #copy source to destination
    print("<=== Copy Static to Public ===>")
    copy_source_to_destination(SRC, DST)

    #generate template in destination
    print("<=== Generate HTML pages ===>")
    generated_templates = generate_pages_recursive(fp, tp, DST)
    print(f"<=== {generated_templates} ===>")

    return f'Process Complete!!'

result = main()
print(result)
