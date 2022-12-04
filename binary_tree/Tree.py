import collections

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
        if self.root is None: return None
        q = collections.deque([self.root])
        while len(q) > 0:
            current = q.popleft()
            if current.getData() == number:
                return current

            if current.getRight() is not None:
                q.append(current.getRight())
            if current.getLeft() is not None:
                q.append(current.getLeft())

            
          
        print("not found")
        return


    def delete(self, number):
         current = self.root
         parent = None
         fromLeft = False

         while current is not None:
            curData = current.getData()
            if curData == number:
                if current.getLeft() is None and current.getRight() is None:
                    if fromLeft:
                        parent.setLeft(None)
                    else:
                        parent.setRight(None)
                else: 
                    #find the right most leaf
                    pass
            
            if curData > number:
                fromLeft = True
                current = current.getLeft()
            else:
                fromLeft = False
                current = current.getRight()
        

         print("not found")

         def findRightLeafAndDelete(self, node, parent, fromLeft):
            pass