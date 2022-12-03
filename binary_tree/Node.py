class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def setLeft(self, node):
        self.left = node

    def getRight(self):
        return self.right
    
    def setRight(self, node):
        self.right = node