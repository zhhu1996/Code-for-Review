# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # # 1. 递归, head是当前需要交换的节点, 返回已经交换好的节点
        # if not head:
        #     return None
        # if not head.next:
        #     return head

        # p = head.next
        # head.next = self.swapPairs(p.next)
        # p.next = head

        # return p

        # 2. 循环
        if not head:
            return None
        pre = ListNode(-1)
        pre.next = head
        Phead = pre
        it = head
        post = it.next
        while it and post:
            pre.next = post
            it.next = post.next
            post.next = it
            pre = it
            it = pre.next
            if it:
                post = it.next

        return Phead.next