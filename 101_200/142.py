# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """环形链表II
        1. 快慢指针
        i. 先用快慢指针判断是否有环
        快指针经过了f步, 慢指针经过了s步, 非环节点a个, 环节点b个
        => f = 2 * s && f = s + nb
        => s = nb, f = 2nb
        环的入口经过了a+nb个节点
        => 慢指针s再走a步, 也就是head节点再走a步, 两者相遇处即环的入口
        """
        fast, slow = head, head
        # 判断是否有环
        flag = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                flag = True
                break
        if not flag:
            return None
        # 求环入口
        phead= head
        while phead != slow:
            slow = slow.next
            phead = phead.next
        return slow