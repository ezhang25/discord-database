from files import *

class FileSystem:
    def __init__(self: FileSystem):
        self.root = Directory("root")
        self.curr = self.root
        
    def resolve_path(self: FileSystem, path: str) -> Directory:
        path = [p for p in path.replace('/', '/,').split(',') if p != '']

        if path[0] == "/":
            path.pop(0)
            curr_path = self.root
            while len(path) != 0:
                next_dir = path.pop(0)
                for child in curr_path.children:
                    if next_dir == child.name:
                        curr_path = child
                        break
                else:
                    return None
        else:
            curr_path = self.curr
            while len(path) != 0:
                next_dir = path.pop(0)
                for child in curr_path.children:
                    if next_dir == child.name:
                        curr_path = child
                else:
                    return None
        
        return curr_path

    def ls(self: FileSystem, path: str=None) -> str:
        all_files = ""
        if path == None:
            start_path = self.curr.get_children()
        else:
            start_path = self.resolve_path(path)
        for child in start_path.children:
            all_files += f"{child.name} "
        return all_files
    
   
"""
     def tree(self: FileSystem, directory: Directory, layer: int=1) -> str:
        tree_paths = []
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

    def cd(self, path: str):
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

    
        """