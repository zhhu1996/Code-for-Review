# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """相交链表
        1. 集合, 时间复杂度O(m+n), 空间复杂度O(m)

        2. 双指针, 时间复杂度O(m+n), 空间复杂度O(1)
        A链长度为a, B链长度为b => 链表总长为a+b => 若有交点, 那么先走完A, 再走B必定与先走完B, 再走A汇合于交点处
        """
        # # 1.
        # exists = set()
        # it = headA
        # while it:
        #     exists.add(it)
        #     it = it.next
        # it = headB
        # while it:
        #     if it in exists:
        #         return it
        #     it = it.next
        # return None

        # 2.
        pa, pb = headA, headB
        while pa != pb:
            pa = (headB if not pa else pa.next)
            pb = (headA if not pb else pb.next)
        return pa