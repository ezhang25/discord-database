class Directory:
    def __init__(self: Directory, data: str, name:str):
        self.name = name
        self.data = data
        self.children = []
    
    def add_child(self: Directory, child: Directory):
        self.children.append(child)
        self.children.sort()

    def get_name(self: Directory) -> str:
        return self.name

class File:
    def __init__(self: File, data: str, name: str):
        self.name = name
        self.data = data
    
    def get_contents(self: File) -> str:
        return self.name
        
