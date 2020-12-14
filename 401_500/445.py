# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 1. 先反转链表、加法、再反转回来
        # 2. 用堆栈存储元素，然后构造节点
        def reverseList(listNode):
            pre = None
            it = listNode
            while it:
                post = it.next
                it.next = pre
                pre = it
                it = post
            return pre

        rl1 = reverseList(l1)
        rl2 = reverseList(l2)
        it1, it2 = rl1, rl2
        carry = 0
        headNode = ListNode(-1)  # 头节点
        while it1 and it2:
            tempVal = it1.val + it2.val + carry
            carry = tempVal // 10
            tempNode = ListNode(tempVal % 10)
            tempNode.next = headNode.next
            headNode.next = tempNode
            it1 = it1.next
            it2 = it2.next
        while it1:
            tempVal = it1.val + carry
            carry = tempVal // 10
            tempNode = ListNode(tempVal % 10)
            tempNode.next = headNode.next
            headNode.next = tempNode
            it1 = it1.next
        while it2:
            tempVal = it2.val + carry
            carry = tempVal // 10
            tempNode = ListNode(tempVal % 10)
            tempNode.next = headNode.next
            headNode.next = tempNode
            it2 = it2.next
        if carry:
            tempNode = ListNode(carry)
            tempNode.next = headNode.next
            headNode.next = tempNode
        return headNode.next


