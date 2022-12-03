from Tree import Tree
from Node import Node
import random

tree = Tree()

for i in range(0, 15):
    node = Node(random.randint(0, 50))
    tree.insert(node)


tree.printInOrder()