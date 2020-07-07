class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """寻找数组中出现次数超过一半的数字
        1. 数组中出现次数超过一半：遍历数组，保存两个变量，一个是被认为出现次数超过一半的数字，一个是该数字出现的次数，
        时间复杂度: O(n)

        2.
        """
        # # 方法1
        # if not nums:
        #     return -1
        # result, cnt = nums[0], 0
        # for i in range(len(nums)):
        #     if nums[i] == result:
        #         cnt += 1
        #     else:
        #         cnt -= 1
        #     if cnt == 0:
        #         result = nums[i]
        #         cnt = 1
        # return result

        def partition(nums, length, start, end):
            if start < 0 or end >= length:
                return None
            index = start - 1
            point = start
            while point < end:
                if nums[point] < nums[end]:
                    index += 1
                    nums[index], nums[point] = nums[point], nums[index]
                point += 1
            index += 1
            nums[index], nums[end] = nums[end], nums[index]
            return index

        if not nums:
            return -1
        length, start, end = len(nums), 0, len(nums)-1
        mid = (start + end) // 2
        index = partition(nums, length, start, end)
        while index != mid:
            if index < mid:
                start = index + 1
                index = partition(nums, length, start, end)
            else:
                end = index - 1
                index = partition(nums, length, start, end)
        return nums[index]