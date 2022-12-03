class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def setNext(self, node):
        self.next = node

    def getNext(self):
        return self.next


    def setPrev(self, node):
        self.prev = node

    def printData(self):
        print(self.data)

    def getData(self):
        return self.data