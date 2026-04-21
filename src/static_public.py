import shutil
import os


def copy_source_to_destination(source, destination):
    
    if not os.path.exists(destination):
        os.mkdir(destination)
        print(f"<=== Created {destination} ===>")

    for c in os.listdir(source):
        src = os.path.join(source, c)
        dst = os.path.join(destination, c)

        if not os.path.isfile(src):
            print(f"<== Source: {source}\n to \nDestination: {destination} ==>\n")
            copy_source_to_destination(src, dst)
        else:
            print(f"Creating file: {dst}")
            shutil.copy(src, dst)

    return f"Copied Static to Public!"