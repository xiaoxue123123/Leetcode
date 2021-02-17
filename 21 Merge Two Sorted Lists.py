class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode()
l1.val = 1
l1.next = ListNode()
l1.next.val = 2
l1.next.next = ListNode()
l1.next.next.val = 4

l2 = ListNode()
l2.val = 1
l2.next = ListNode()
l2.next.val = 3
l2.next.next = ListNode()
l2.next.next.val = 4


# 网上的答案
def mergeTwoLists(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2

a = mergeTwoLists(l1,l2)