root = BinaryTree(5)
l = [4,8,11,None ,13,4,7,2,None ,None , None,1]
for i in range(len(l)//2):
    root.insert_left(i)
    root.insert_right(i+1)