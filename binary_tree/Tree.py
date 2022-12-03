class Tree():
    def __init__(self):
        self.root = None

    def inOrder(self, node):
        if node is None: return

        if node.getRight() is None and node.getLeft() is None:
            print(node.getData())
            return
        
        if node.getLeft() is None:
            print(node.getData())
            return self.inOrder(node.getRight())
        
        self.inOrder(node.getLeft())
        print(node.getData())

        if node.getRight() is not None:
            return self.inOrder(node.getRight())

    def printInOrder(self):
        #dfs
        self.inOrder(self.root)

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