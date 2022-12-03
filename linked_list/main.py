from linked_list import LinkedList
from Node import Node

list = LinkedList()
for i in range(0, 5):
    node = Node(i)
    list.Insert(node)



list.Search(6)



node = Node(20)
list.Insert(node)


list.printList()