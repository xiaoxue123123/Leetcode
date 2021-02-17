class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #self = ListNode(0)
        #self.next = None
        self.size = 0
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        else:
            node = self.head
            for i in range(index+1):
                node = node.next
            return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node_add = ListNode(val)
        node_add.next = self.head.next
        self.head.next = node_add
        self.size += 1
        print(self.head.next.val)



    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """

        if index > self.size:
            return
        if index <0:
            index = 0
        node = self.head
        for _ in range(index):
            node = node.next
        to_add = ListNode(val)
        to_add.next = node.next
        node.next = to_add
        self.size += 1

        # predesessor = node
        # predesessor.next = after_node
        # predesessor.next = ListNode(val)
        # predesessor.next.next = after_node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        return self.addAtIndex(self.size,val)


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index <= self.size -1:
            node = self.head
            for _ in range(index):
                node = node.next
            node.next = node.next.next
            self.size -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)