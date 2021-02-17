l = [1,2,2,3,4,4,3]


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data <= self.data:
                print(1)
                if self.left is None:
                    self.left = Node(data)
                    print(2)
                else:
                    self.left.insert(data)
                    print(3)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
l = [1, 2, 2, 3, 4, 4, 3]

root = Node(1)
root.insert(2)
root.insert(2)
#root.left.insert(3)

root.PrintTree()