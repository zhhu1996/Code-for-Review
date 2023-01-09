# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # 1. 迭代(双指针)
        # if not head:
        #     return head
        # it = head
        # pre = None
        # while it:
        #     post = it.next
        #     it.next = pre
        #     pre = it
        #     it = post
        # return pre

        # # 2. 递归解法1
        # def reverseNode(pre, cur):
        #     """
        #         pre: last node, 已经反转好的链表
        #         cur: current node, 待反转的链表
        #     """
        #     if not cur:
        #         return pre
        #     post = cur.next
        #     cur.next = pre
        #     return reverseNode(cur, post)

        # return reverseNode(None, head)

        # 递归解法2
        # head表示当前遍历的节点，返回已经反转好的链表的第一个节点
        if not head or not head.next:
            return head
        cur = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return cur
