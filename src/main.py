from static_public import *
#from static_public import SRC, DST


def main():
    #check for destination, if present remove it
    if directory_check(DST):
        remove_destination(DST)
    
    # create new destination
    create_new_directory(DST)

    #copy source to destination
    copy_source_to_destination(SRC, DST)

    return f'Process Complete!!'

result = main()
print(result)
