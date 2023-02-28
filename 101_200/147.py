# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """对链表进行插入排序
        1. 双指针
        head..tail是已排序的链表, head是已排序的第一个节点, tail是最后一个节点
        """
        if not head: return None
        phead = ListNode(-1, head)
        tail = head
        cur = tail.next
        while cur:
            if cur.val >= tail.val:
                tail = tail.next
                cur = cur.next
            else:
                it = phead
                while it.next and it.next.val < cur.val:
                    it = it.next
                tail.next = cur.next # 删除cur节点防止出现环
                cur.next = it.next
                it.next = cur
                cur = tail.next
        return phead.next        