# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. 遍历, 时间复杂度O(n^2)

        2. 前缀和 + 哈希表, 时间复杂度O(n)
        哈希表记录前缀和的状态, key为前缀和, value为第一次出现的节点; 
        如果sum已存在哈希表, 说明区间和为0, 逐个删除节点并清理哈希表
        优化 -> 删除区间时不维护哈希表状态, 直接遍历两次 
        """
        # # 1.
        # if not head: return None
        # phead = ListNode(-1, head)
        # pre, fst = phead, head
        # while fst:
        #     cumsum = 0
        #     sec = fst
        #     flag = False
        #     while sec:
        #         cumsum += sec.val
        #         if cumsum == 0:
        #             pre.next = sec.next
        #             fst = sec.next
        #             flag = True
        #             break
        #         sec = sec.next
        #     if not flag:
        #         pre = fst
        #         fst = fst.next
        # return phead.next


        # 2.
        phead = ListNode(0, head)
        it = phead
        presum = {}
        cumsum = 0
        while it:
            cumsum += it.val
            if cumsum in presum: # 区间和=0
                last = presum[cumsum]
                dt = last.next
                last.next = it.next
                dsum = cumsum
                while dt != it:
                    dsum += dt.val
                    del presum[dsum]
                    dt = dt.next
            else:                # 区间和!=0
                presum[cumsum] = it
            it = it.next
        return phead.next