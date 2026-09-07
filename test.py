from files import *
from commands import *

root = Directory("random data", "/root")

folder = Directory("random data", "folder")
print(root.add_child(folder))

folder = Directory("random data", "folder")
print(root.add_child(folder))

random = Directory("random data", "random")
root.add_child(random)

alphabetical = Directory("random data", "alphabetical")
root.add_child(alphabetical)

bottom = Directory("random data", "bottom")
root.add_child(bottom)

cow = Directory("random data", "cow")
alphabetical.add_child(cow)

bottom = Directory("random data", "bottom")
alphabetical.add_child(bottom)

ls(root)
tree(root)