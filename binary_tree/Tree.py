class Tree():
    def __init__(self):
        self.root = None

    def printInOrder(self):
        pass

    def printPostOrder(self):
        pass

    def printPreOrder(self):
        pass
    
    def insert(self, node):
        if self.root is None:
            self.root = node
            return

        currentNode = self.root
        
        while currentNode is not None:
            if node.getData() > currentNode.getData():
                if currentNode.getRight() is not None:
                    currentNode = currentNode.getRight()
                else:
                    currentNode.setRight(node)
                    return

            else: 
                if currentNode.getLeft() is not None:
                    currentNode = currentNode.getLeft() 
                else: 
                    currentNode.setLeft(node)
                    return
        




    def search(self, number):
        pass

    def delete():
        pass