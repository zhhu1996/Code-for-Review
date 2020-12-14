# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        """
        首先划分区间，求出每个区间的元素个数；之后根据元素个数去切割链表（或者新建链表节点）
        """
        lenL = 0
        it = root
        while it:
            lenL += 1
            it = it.next
        nlist = [lenL // k for i in range(k)]
        for i in range(lenL % k):
            nlist[i] += 1
        p = root
        result = []
        for i in range(len(nlist)):
            it = p
            for j in range(nlist[i] - 1):
                it = it.next
            result.append(p)
            if it:
                p = it.next
                it.next = None
        return result
