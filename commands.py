from files import *

current_directory = Directory('data', '/')

def ls(directory: Directory=current_directory) -> list[Directory | File]:
    children = directory.get_children()
    for child in children:
        print(child.name)

def tree(directory: Directory=current_directory, layer: int=1) -> str:
    print(directory.name)
    for child in directory.children:
        for i in range(0, layer):
            if i == layer-1:
                print("  └──", end="")
            else:
                print("  │", end="  ")
        tree(child, layer+1)