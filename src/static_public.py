import shutil
import os
import os.path


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
