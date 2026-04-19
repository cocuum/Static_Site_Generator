from static_public import (
    copy_source_to_destination,
    create_new_directory,
    directory_check,
    generate_page,
    remove_destination,
)

SRC = "/Users/the_core/boots/cocuum/Static_Site_Generator/static"
DST = "/Users/the_core/boots/cocuum/Static_Site_Generator/public"

fp = "/Users/the_core/boots/cocuum/Static_Site_Generator/content/index.md"
tp = "/Users/the_core/boots/cocuum/Static_Site_Generator/template.html"


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
    generated_template = generate_page(fp, tp, DST)
    print(f"<=== {generated_template} ===>")

    return f'Process Complete!!'

result = main()
print(result)
