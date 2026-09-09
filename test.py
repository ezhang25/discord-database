from files import *
from commands import *

file = FileSystem()
folder1 = Directory("folder1")
file.root.add_child(folder1)
file1 = File("file1")
folder1.add_child(file1)
file.root.add_child(Directory("folder2"))
file.root.add_child(Directory("folder3"))
file.resolve_path("/folder1/")
print(file.ls("/folder1/"))
print(file.ls("/"))

print()

print(file.root.tree())

"""
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

rm("randomfile2", cow)
tree(curr)

parse_test = "root/pet/name/"
parsed = parse_test.split("/")
parsed = [p for p in parsed if p!='']
print(f"\n\n{parsed}")
"""