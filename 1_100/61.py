# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 1. 先求链表长度，然后旋转
        # i. 空链表
        # ii. k % cnt = 0时候不需要旋转
        # iii. 其他情况需要旋转
        if not head:
            return None

        cnt = 0
        pre = ListNode()
        pre.next = head
        tail = None
        it = head
        while it:
            cnt += 1
            tail = it
            it = it.next
        k = k % cnt
        it = head
        if k == 0:
            return head

        for i in range(cnt - k):
            pre = it
            it = it.next
        pre.next = None
        tail.next = head
        return it

        # 2. 先做成闭环，然后找到头节点和尾节点断开


