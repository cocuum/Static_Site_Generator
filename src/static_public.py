from shutil import copy, rmtree
from os import mkdir, listdir
from os.path import exists, join, isfile


SRC = "/Users/the_core/boots/cocuum/Static_Site_Generator/static"
DST = "/Users/the_core/boots/cocuum/Static_Site_Generator/public"


def copy_source_to_destination(source, destination):
    #print(f"<== Source: {source}\n to \nDestination: {destination} ==>\n")
    content = list_directory_content(source)
    for c in content:
        src = join(source, c)
        dst = join(destination, c)

        if not isfile(src):
            create_new_directory(dst)
            copy_source_to_destination(src, dst)
        else:
            copy_content(src, dst)

def directory_check(destination):
    #print("<== Existence Check ==>")
    result = exists(destination)
    #print(f"{"="*len(destination)}\nDestination existence: {result}\n{"="*len(destination)}")
    return result

def list_directory_content(location):
    #print("<== Directory Content ==>")
    result = listdir(location)
    #print(f"{"="*len(location)}\nContent at {location}\n{"="*len(location)}")
    #print(f'Directory Content: {result}')
    return result

def create_new_directory(destination):
    #print("<== Create Directory ==>")
    #print(f"{"="*len(destination)}\nCreating new directory: {destination}\n{"="*len(destination)}")
    mkdir(destination)

def copy_content(source, destination):
    #print("<== Coping ==>")
    copy(source, destination)
    #print(f"{"="*len(destination)}\nSource: {source}\nDestination: {destination}\n{"="*len(destination)}")

def remove_destination(destination):
    #print("<== Remove Directory ==>")
    rmtree(destination)
    #print(f"{"="*len(destination)}\nRemoved destination: {destination}\n{"="*len(destination)}")
