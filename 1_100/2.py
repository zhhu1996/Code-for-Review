# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # # 1. 先计算出数字之和，然后生成链表
        # res = self.getNumber(l1) + self.getNumber(l2)
        # if res == 0:
        #     return [0]
        # # 加上头指针比较方便
        # pHead = ListNode(-1)
        # it = pHead
        # while res:
        #     temp = res % 10
        #     # 尾插法
        #     it.next = ListNode(temp)
        #     it = it.next
        #     res = res // 10
        # return pHead.next

        # 2. 一边遍历链表一边计算结果
        # 先计算l1和l2公共的部分的和，然后对于超出的部分单独加上前面的进位值，如果最后一位的值也超过10，那么需要新建一个节点保存在最后
        head = ListNode(-1)
        tail = head
        carry = 0
        while l1 and l2:
            temp = l1.val + l2.val + carry
            carry = temp // 10
            temp %= 10
            tail.next = ListNode(temp)
            tail = tail.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            tail.next = l1
            while l1:
                l1.val += carry
                carry = l1.val // 10
                l1.val %= 10
                tail = l1
                l1 = l1.next
        if l2:
            tail.next = l2
            while l2:
                l2.val += carry
                carry = l2.val // 10
                l2.val %= 10
                tail = l2
                l2 = l2.next
        if carry:
            tail.next = ListNode(carry)

        return head.next

    def getNumber(self, head):
        it = head
        num = 0
        base = 1
        while it:
            num += base * it.val
            base *= 10
            it = it.next
        return num