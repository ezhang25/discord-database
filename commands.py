from files import *

root_directory = Directory('data', 'root')

def ls(directory: Directory=root_directory) -> list[Directory | File]:
    children = directory.get_children()
    for child in children:
        print(child.name)

def cd(name: str, current_directory: Directory):
    if name == "..":
        if current_directory.parent != None:
            return current_directory.parent
        return current_directory
    else:
        for directory in current_directory.children:
            if name == directory.name:
                return directory
        return current_directory

def mkdir(new_directory: Directory, directory: Directory=root_directory) -> int:
    directory.add_child(new_directory)

def touch(new_file: File, directory: Directory):
    directory.add_child(new_file)

def rm(target: str, directory: Directory):
    directory.children = [c for c in directory.children if c.name != target]

def tree(directory: Directory=root_directory, layer: int=1) -> str:
    print(directory.name)
    for child in directory.children:
        for i in range(0, layer):
            if i == layer-1:
                print("  └──", end="")
            else:
                print("  │", end="  ")
        if isinstance(child, Directory):
            tree(child, layer+1)
        else:
            print(child.name)