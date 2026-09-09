from files import *

class FileSystem:
    def __init__(self: FileSystem):
        self.root = Directory("root")
        self.curr = self.root
        
    def resolve_path(self: FileSystem, path: str) -> Directory | File:
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
    
    def cd(self, path: str):
        for directory in self.curr.children:
            if path == directory.name:
                self.curr = directory
        return self.curr
    
    def tree(self: FileSystem, path: str=None) -> str:
        if path == None:
            return self.curr.build_tree()
        else:
            return self.resolve_path(path).build_tree()
    
    def mkdir(self: FileSystem, name: str) -> bool:
        for child in self.curr.children:
            if name == child.name:
                return False
        self.curr.add_child(Directory(name))
        return True
    
    def touch(self: FileSystem, name: str) -> bool:
        for child in self.curr.children:
            if name == child.name:
                return False
        self.curr.add_child(File(name))
        return True
    
    def rm(self: FileSystem, name: str) -> bool:
        num_items = len(self.curr.children)
        self.curr.children = [child for child in self.curr.children if name != child.name]
        return num_items != len(self.curr.children)