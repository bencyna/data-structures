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
         fromLeft = False

         q = collections.deque([[self.root, None]])

         while len(q) > 0:
            current = q.popleft()
            parent = current[1]
            current = current[0]

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
                    rightMostLeaf.setLeft(current.getLeft())
                    rightMostLeaf.setRight(current.getRight())
            
                return
            
            if current.getLeft() is not None:
                q.append([current.getLeft(), current])
            
            if current.getRight() is not None:
                q.append([current.getRight(), current])


         print("not found")

         def findRightLeafAndDelete(self, node, parent, fromLeft):
            if node.getRight() == None and node.getLeft() == None:
                if fromLeft:
                    parent.setLeft(None)
                elif parent is not None:
                    parent.setRight(None)

                return node

            if node.getRight() is None:
                return findRightLeafAndDelete(node.getLeft(), node, True)

            return findRightLeafAndDelete(node.getRight(), node, False)