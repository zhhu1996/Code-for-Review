# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """删除排序链表中的重复元素II
        1. 递归
        返回以head为头结点的含重复值的链表, 根据cur与cur.next是否相等分情况讨论

        2. 迭代 + 哈希表, 需要两次遍历链表

        3. 迭代 + 1次遍历链表
        """
        # # 1.
        # if not head or not head.next:
        #     return head
        # if head.val != head.next.val:
        #     head.next = self.deleteDuplicates(head.next)
        #     return head
        # else:
        #     move = head.next
        #     while move and move.val == head.val:
        #         move = move.next
        #     return self.deleteDuplicates(move)


        # 3.
        dummy = ListNode(-1, head)
        pre, cur = dummy, head
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if pre.next == cur:
                pre = cur
            else:
                pre.next = cur.next
            cur = cur.next
        return dummy.next