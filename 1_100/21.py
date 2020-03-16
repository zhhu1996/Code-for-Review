# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 1. 直接遍历两个有序链表
        # 设置头指针会比较方便
        head = ListNode(0)
        first = head
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next
            else :
                head.next = l1
                l1 = l1.next
            head = head.next
        if l1 == None:
            head.next = l2
        elif l2 == None:
            head.next = l1

        return first.next

        # # 2. 递归
        # if not l1 and not l2:
        #     return None
        #
        # elif l1 and l2:
        #     p, q = l1.next, l2.next
        #     if l1.val < l2.val:
        #         l1.next = self.mergeTwoLists(p, l2)
        #         return l1
        #
        #     else:
        #         l2.next = self.mergeTwoLists(l1, q)
        #         return l2
        #
        # else:
        #     if l1:
        #         return l1
        #     else:
        #         return l2
