class Directory:
    def __init__(self: Directory, name: str, parent: Directory=None):
        self.name = f"{name}/"
        self.children = []
    
    def add_child(self: Directory, new_child: Directory | File) -> int:
        for child in self.children:
            if new_child.name == child.name:
                return 1
        if isinstance(new_child, Directory):
            new_child.parent = self
        self.children.append(new_child)
        self.children.sort(key=lambda x: x.name)
        return 0
    
    def build_tree(self: Directory, layer: int=1) -> str:
        tree_str = f"{self.name}\n"
        for child in self.children:
            for i in range(0, layer):
                if i == layer-1:
                    tree_str += "  └──"
                else:
                    tree_str += "  │  "

            tree_str += child.build_tree(layer+1)
        return tree_str

class File:
    def __init__(self: File, name: str):
        self.name = name

    def build_tree(self: File, layer: int=1) -> str:
        return f"{self.name}\n"
        
