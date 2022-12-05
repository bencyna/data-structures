from Tree import Tree
from Node import Node
import random

tree = Tree()

for i in range(0, 15):
    node = Node(random.randint(0, 50))
    tree.insert(node)

num = Node(7)
num2 = Node(7)
tree.insert(num2)
tree.insert(num)
tree.delete(7)
node = tree.search(7)
if node is not None:
    print(f"data: {node.getData()}")

tree.printInOrder()