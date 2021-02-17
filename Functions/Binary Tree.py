#二叉树类
class BinaryTree(object):
    # 初始化，传入根节点的值
    def __init__(self, root_value):
        self.root = root_value
        self.left = None
        self.right = None
    # 插入左子树
    def insert_left(self, left_value):
        if self.left == None :
            self.left = BinaryTree(left_value)
        else:
            left_subtree = BinaryTree(left_value)
            left_subtree.left = self.left
            self.left = left_subtree
    # 插入右子树
    def insert_right(self, right_value):
        if self.right == None :
            self.right = BinaryTree(right_value)
        else:
            right_subtree = BinaryTree(right_value)
            right_subtree.right = self.right
            self.right = right_subtree
    # 设置根节点的值
    def set_root(self, root_value):
        self.root = root_value
    # 获取根节点的值
    def get_root(self):
        return self.root
    # 获取左子树
    def get_leftchild(self):
        return self.left
    # 获取右子树
    def get_rightchile(self):
        return self.right