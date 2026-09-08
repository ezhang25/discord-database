from files import *

root_directory = Directory('data', 'root')

def ls(directory: Directory=root_directory) -> list[Directory | File]:
    children = directory.get_children()
    for child in children:
        print(child.name)

def mkdir(new_directory: Directory, directory: Directory=root_directory) -> int:
    directory.add_child(new_directory)

def cd(name: str, current_directory: Directory):
    if name == "..":
        return current_directory.parent
    else:
        for directory in current_directory.children:
            if name == directory.name:
                return directory
            else:
                return current_directory

def tree(directory: Directory=root_directory, layer: int=1) -> str:
    print(directory.name)
    for child in directory.children:
        for i in range(0, layer):
            if i == layer-1:
                print("  └──", end="")
            else:
                print("  │", end="  ")
        tree(child, layer+1)