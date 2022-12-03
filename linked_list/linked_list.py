class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
   
    def Search(self, data):
        current = self.head
        index = 0

        while current != None:
            if current.getData() == data:
                return index

            index +=1
            current = current.getNext()
        
        print("Data not in list")

    def Insert(self, node):
        if (self.head == None):
            self.head = node
            self.tail = node
        else:
            node.setPrev(self.tail)
            self.tail.setNext(node)
            self.tail = node

    def Delete(self, index):
        if (self.head == None):
            print("Error, nothing to delete")
        
        current = self.head
        prev = None
        nodeNum = 1

        if index == 0:
            self.head = current.getNext()
            if current == self.tail:
                self.tail = None

            del current
            return

        current = current.next
        while current != None:
            if index == nodeNum:
                prev.setNext(current.getNext())
                if current == self.tail:
                    self.tail = prev

                del current
                return
            nodeNum += 1
            prev = current
            current = current.next


        print("index not found")


    def printList(self):
        current = self.head
        while current != None:
            current.printData()
            current = current.next