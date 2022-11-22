# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        it = head
        pre = None
        post = it.next
        cnt = 1
        while it or cnt <= right + 1:
            if cnt >= left and cnt <= right:
                if cnt == left:
                    p = pre
                    s = it
                it.next = pre
            elif cnt > right:
                if p:
                    p.next = pre
                s.next = it
                break
            pre = it
            it = post
            if it:
                post = it.next
            cnt += 1
        if left > 1:
            return head
        else:
            return pre