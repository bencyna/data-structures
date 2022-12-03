class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def setNext(self, node):
        self.next = node

    def setPrev(self, node):
        self.prev = node

    def printData(self):
        print(self.data)