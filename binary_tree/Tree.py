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

        q = collections.deque([self.root])
        
        while len(q) > 0:
            current = q.popleft()
            if current.getLeft() is not None:
                q.append(current.getLeft())
            else:
                current.setLeft(node)
                return

            if current.getRight() is not None:
                q.append(current.getRight())
            else:
                current.setRight(node)
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
                    rightMostLeaf = findRightLeafAndDelete(self.head, None, False)
                    
            
            if curData > number:
                fromLeft = True
                current = current.getLeft()
            else:
                fromLeft = False
                current = current.getRight()
        

         print("not found")

         def findRightLeafAndDelete(self, node, parent, fromLeft):
            if node.getRight() == None and node.getLeft() == None:
                if fromLeft:
                    parent.setLeft(None)
                elif parent is not None:
                    parent.setRight(None)

                return node

            if node.getLeft() is None:
                return findRightLeafAndDelete(node.getRight(), node, False)

            return findRightLeafAndDelete(node.getLeft(), node, True)