class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    """设计链表
    1. 单链表/双链表
    基函数addAtIndex, 在索引index前插入元素
    """

    def __init__(self):
        self.size = 0
        self.dummy = ListNode(-1)

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.dummy
        for i in range(index+1):
            cur = cur.next
        return cur.val      

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        pre, cur = self.dummy, self.dummy.next
        for i in range(1, index+1):
            pre = cur
            cur = cur.next
        node = ListNode(val, cur)
        pre.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        pre, cur = self.dummy, self.dummy.next
        for i in range(1, index+1):
            pre = cur
            cur = cur.next
        pre.next = cur.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)