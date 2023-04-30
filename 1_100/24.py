# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """两两交换链表中的节点
        1. 递归
        递归返回以head为头结点的交还相邻节点后的链表

        2. 迭代
        三指针法, pre/cur/post
        """
        # # 1.
        # if not head or not head.next:
        #     return head
        # ans = head.next
        # nexts = self.swapPairs(ans.next)
        # ans.next = head
        # head.next = nexts
        # return ans


        # 2.
        if not head: return head
        dummy = ListNode(-1, head)
        pre, cur, post = dummy, head, head.next
        while cur and post:
            pre.next = post
            cur.next = post.next
            post.next = cur
            pre = cur
            cur = cur.next
            if cur:
                post = cur.next
        return dummy.next