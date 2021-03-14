class Solution:
    def removeDuplicates(self, S: str) -> str:
        """删除字符串中的所有相邻重复项
        方法1: 暴力循环，时间复杂度O(n^2)

        方法2: 堆栈，时间复杂度O(n)
        """
        # # 方法1
        # def isUnique(nums):
        #     if len(nums) <= 1:
        #         return True
        #     last = nums[0]
        #     for i in range(1,len(nums)):
        #         if nums[i] == last:
        #             return False
        #         last = nums[i]
        #     return True
        #
        # def delDupArray(nums):
        #     if len(nums) <= 1:
        #         return nums
        #     for i in range(1, len(nums)):
        #         if nums[i] == nums[i-1]:
        #             nums.pop(i)
        #             nums.pop(i-1)
        #             break
        #     return nums
        #
        # nums = list(S)
        # while not isUnique(nums):
        #     nums = delDupArray(nums)
        # return "".join(delDupArray(nums))

        # 方法2
        stack = []
        for c in S:
            if not stack:
                stack.append(c)
            else:
                if c == stack[-1]:
                    stack.pop()
                else:
                    stack.append(c)
        array = []
        while stack:
            array.append(stack.pop())
        return "".join(array[::-1])



