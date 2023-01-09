# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 1. 遍历数组中所有链表的首元素, 得到最小值再插入合并链表中
        # ->优化: 使用优先队列来存取最小值
        def is_valid(lists):
            for ll in lists:
                if ll:
                    return True
            return False

        phead = ListNode(-1)
        it = phead
        while is_valid(lists):
            pmin = float('inf')
            mini = 0
            for i in range(len(lists)):
                if lists[i] and lists[i].val < pmin:
                    mini = i
                    pmin = lists[i].val
            it.next = lists[mini]
            lists[mini] = lists[mini].next
            it = it.next
        return phead.next

        # 2. 两两合并, 共合并N次
        # ->优化: 分治法合并, 每次合并k个