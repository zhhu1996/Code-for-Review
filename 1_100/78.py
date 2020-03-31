class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 1. 回溯实现
        # self.res = []
        # self.dfs(nums, [], 0)
        # return self.res

        # 2. 递归实现
        n = len(nums)
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]

        return output

    def dfs(self, nums, temp, i):
        # nums表示原始数组，temp表示当前已经挑选的数组
        # [i, len(nums)-1]中挑选一个元素进行回溯，小于i的已经被计算过，不用重复计算了
        self.res.append(temp.copy())
        for j in range(i, len(nums)):
            temp.append(nums[j])
            self.dfs(nums, temp, j + 1)
            temp.pop()