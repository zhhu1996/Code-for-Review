# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """K个一组翻转链表
        1. 先计算链表长, 得到需要反转的轮数. 每一轮通过三指针法反转k个节点, 需要额外记录上一轮的终点, 当前轮的起点(共5个指针)
        """
        if not head: return None
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next
        end = cnt // k
        dummy = ListNode(-1, head)
        pre, cur, post = dummy, head, head.next
        steps = 0
        while steps < end:
            last_end = pre
            this_start = cur
            for i in range(k):
                cur.next = pre
                pre = cur
                cur = post
                if post:
                    post = post.next
            this_start.next = cur
            last_end.next = pre
            pre = this_start
            steps += 1
        return dummy.next