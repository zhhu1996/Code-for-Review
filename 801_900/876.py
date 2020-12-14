# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        it1, it2 = head, head
        while it2 and it2.next:
            it1 = it1.next
            it2 = it2.next.next
        return it1
