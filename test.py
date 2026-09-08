from files import *
from commands import *

root = root_directory
curr = root_directory

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
ls()
tree()
mkdir(Directory("random data", "cow"))
tree()
tree(alphabetical)

curr = cd("alphabetical/" , curr)
tree(curr)
curr = cd(".." , curr)
tree(curr)