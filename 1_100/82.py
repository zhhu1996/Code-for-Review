# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        numDict = {}
        it = head
        while it:
            if it.val not in numDict:
                numDict[it.val] = 1
            else:
                numDict[it.val] += 1
            it = it.next
        pHead = ListNode(-1)
        pHead.next = head
        pre = pHead
        it = head
        while it:
            if numDict[it.val] > 1:
                pre.next = it.next
                it = it.next
            else:
                pre = it
                it = it.next
        return pHead.next