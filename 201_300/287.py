class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1. 排序后查找，nlogn

        # 2. set，查找

        # 3. hash

        # 4. 数学方法，不成立，因为这个重复数字可能不只出现一次

        # 5. 只能用二分查找了
        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     cnt = 0
        #     for i in range(len(nums)):
        #         if nums[i] <= mid:
        #             cnt += 1
        #     if cnt > mid:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return left

        # 6. 双指针, 根据数组的索引与值构建链表, 由于存在重复元素, 因此链表中必定有1个节点可以可由两个位置跳转到, 因此链表存环=> 求解链表环的入口
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow