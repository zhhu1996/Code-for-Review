# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 1. 尾插法，重新生成每个链表的节点
        if not head:
            return None
        pHead = ListNode(-1)
        nit = pHead
        it = head
        right = []
        while it:
            if it.val < x:
                nit.next = ListNode(it.val)
                nit = nit.next
            else:
                right.append(it.val)
            it = it.next
        for value in right:
            nit.next = ListNode(value)
            nit = nit.next
        return pHead.next

        # 2. 双指针生成两段链表，然后进行连接。不用生成新的链表节点
