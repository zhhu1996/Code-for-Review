# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        phead = ListNode(-1, head)
        pre, it = phead, head
        cnt = 0
        while it:
            cnt += 1
            it = it.next
        it = head
        while cnt>=k: # 反转过程
            t = k
            ps = pre
            while t > 0 and it: # 每k个进行反转
                post = it.next
                it.next = pre
                pre = it
                it = post
                t -= 1
                cnt -= 1
            # 更新反转子表的首尾节点
            left = ps.next
            left.next = it
            ps.next = pre
            pre = left
        return phead.next
            