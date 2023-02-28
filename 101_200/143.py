# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """重排链表
        1. 前半部分链表不变, 后半部分链表反转, 之后归并两个链表

        2. 将链表每个元素存入数组中, 然后双指针求解
        """
        # # 1.
        # if not head: return None
        # cnt, it = 0, head
        # while it:
        #     cnt += 1
        #     it = it.next
        # mid = (1+cnt) // 2
        # print(mid)
        # pre = None
        # it = head
        # for i in range(mid):
        #     pre = it
        #     it = it.next
        # pre.next = None
        # pre = None
        # while it:
        #     post = it.next
        #     it.next = pre
        #     pre = it
        #     it = post
        # phead = head
        # ptail = pre
        # it = phead
        # cur = it
        # i = 0
        # while it and ptail:
        #     if i == 0:
        #         post = cur.next
        #         cur.next = ptail
        #         cur = ptail
        #         it = post
        #         i = 1
        #     else:
        #         post = cur.next
        #         cur.next = it
        #         cur = it
        #         ptail = post
        #         i = 0
        # return phead

        # 2.
        nums = []
        it = head
        while it:
            nums.append(it)
            it = it.next
        i, j = 0, len(nums)-1
        flag = 0
        while i < j:
            if not flag:
                nums[i].next = nums[j]
                i += 1
                flag = 1
            else:
                nums[j].next = nums[i]
                j -= 1
                flag = 0
        nums[j].next = None
        return nums[0]
        