class Directory:
    def __init__(self: Directory, data: str, name: str, parent: Directory=None):
        self.name = f"{name}/"
        self.data = data
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

    def get_children(self: Directory) -> list[Directory | File]:
        return self.children

    def get_name(self: Directory) -> str:
        return self.name

class File:
    def __init__(self: File, data: str, name: str):
        self.name = name
        self.data = data
    
    def get_name(self: File) -> str:
        return self.name
    
    def get_contents(self: File) -> str:
        return self.data
        
