from files import *

current_directory = Directory('data', '/')

def ls(directory: Directory=current_directory) -> list[Directory | File]:
    children = directory.get_children()
    for child in children:
        print(child.name)