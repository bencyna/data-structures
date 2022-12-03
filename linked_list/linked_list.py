class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
   
    def Search(self, data):
        pass

    def Insert(self, node):
        if (self.head == None):
            self.head = node
            self.tail = node
        else:
            node.setPrev(self.tail)
            self.tail.setNext(node)
            self.tail = node

    def Delete(self, index):
        pass

    def Sort(self):
        pass


    def printList(self):
        current = self.head
        while current != None:
            current.printData()
            current = current.next