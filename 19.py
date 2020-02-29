# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # # 1. 先完整遍历一次链表，得出链表长度，然后根据题目给出的n，就可以知道需要删除的节点的位置。再次从头遍历链表就可以进
        # 行操作得出结果。
        # if not head:
        #     return None
        # it = head
        # cnt = 0
        # while it:
        #     cnt += 1
        #     it = it.next
        # # 特殊情况：返回第一个节点
        # if cnt - n <= 0:
        #     return head.next
        # it = head
        # i = 1
        # while i != cnt-n:
        #     it = it.next
        #     i += 1
        # it.next = it.next.next
        # return head

        # 2. 一趟扫描实现
        # 使用前后两个指针，前指针先走n步，之后前后指针同时出发，当前指针到达表尾的时候，后指针指向了倒数第n个节点
        # 假设共有k个节点，当前指针和后指针同时行动时，两个指针都会前进k-n步，后指针的终点就是倒数第n个节点
        # 注意单独处理要删除的节点是第一个节点的情况
        it, start = head, head
        while n > 0:
            it = it.next
            n -= 1
        while it and it.next:
            it = it.next
            start = start.next
        if it:
            start.next = start.next.next
        else:
            head = head.next
        return head
