# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        it = head.next
        pre = head
        while it:
            if it.val == pre.val:
                pre.next = it.next
                it = it.next
            else:
                pre = it
                it = it.next
        return head