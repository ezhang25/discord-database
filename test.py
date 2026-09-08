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

randomfile = File("random data", "randomfile")
alphabetical.add_child(randomfile)

randomfile2 = File("random data", "randomfile2")
cow.add_child(randomfile2)

ls(root)
tree(root)
ls()
tree()
mkdir(Directory("random data", "cow"))
tree()
tree(alphabetical)

print("\n\n")

curr = cd("alphabetical/" , curr)
tree(curr)

print("\n\n")

curr = cd(".." , curr)
tree(curr)