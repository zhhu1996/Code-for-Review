# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """删除排序链表中的重复元素
        方法1: 统计每个元素出现的次数，再生成唯一值的链表

        方法2: 遍历一次链表，删除所有重复元素
        """
        # # 方法1
        # numDict = {}
        # it = head
        # while it:
        #     if it.val not in numDict:
        #         numDict[it.val] = 1
        #     else:
        #         numDict[it.val] += 1
        #     it = it.next
        # pHead = ListNode(-1)
        # pHead.next = head
        # pre = pHead
        # it = head
        # while it:
        #     if numDict[it.val] > 1:
        #         pre.next = it.next
        #         it = it.next
        #     else:
        #         pre = it
        #         it = it.next
        # return pHead.next

        # 方法2
        pHead = ListNode(-1)
        pHead.next = head
        pre = pHead
        it = head
        post = it
        while it:
            while post and post.val == it.val:
                post = post.next
            if not post:
                pre.next = None
            elif post == it:
                pre = post
                it = it.next
                post = it
            else:
                pre.next = post.next
                it = post.next
                post = it
        return pHead.next