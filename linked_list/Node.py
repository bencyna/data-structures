class Node():
    def __init__(self, data, tail):
        self.data = data
        self.next = None
        self.prev = tail

    def setNext(self, node):
        self.next = node

    def setPrev(self, node):
        self.prev = node