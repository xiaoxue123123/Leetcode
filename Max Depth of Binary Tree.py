# TreeNode = [3,9,20,None,None,15,7]
#
# l = len(TreeNode)
#
# n = 1
# while 2**n<7:
#     n+=1

class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None


root = Tree()
root.data = "root"
root.left = Tree()
root.left.data = "left"
root.right = Tree()
root.right.data = "right"


def maxDepth(self, root: TreeNode) -> int:
    def recur(node, c):
        if not node:
            return c
        return max(recur(node.left, c + 1), recur(node.right, c + 1))

    return recur(root, 0)