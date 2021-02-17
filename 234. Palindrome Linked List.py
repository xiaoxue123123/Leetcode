#head = [1,2,1]

# solution 1
# pi = 0
# pj = len(head)-1
#
# flag = True
# while pi <=pj:
#     if head[pi] != head[pj]:
#         flag = False
#     pi +=1
#     pj -=1

# solution 2
# print(head == head[::-1])
#
# class Node:
#     # Function to initialize the node object
#     def __init__(self, data):
#         self.data = data  # Assign data
#         self.next = None  # Initialize
#         # next as null
#
#
# # Linked List class
# class LinkedList:
#     # Function to initialize the Linked
#     # List object
#     def __init__(self):
#         self.head = None
#
# llist = LinkedList()
# llist.head = Node(1)
# second = Node(2)
# third = Node(3)
#
# llist.head.next = second
# second.next = third



#网上的solution
def isPalindrome(self, head):
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    return not rev
