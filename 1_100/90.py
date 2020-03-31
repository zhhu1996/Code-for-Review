class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # # 1. 回溯+剪枝
        # self.res = []
        # nums.sort()
        #
        # def dfs(nums, index, array):
        #     self.res.append(array.copy())
        #     for i in range(index, len(nums)):
        #         if i > index and nums[i] == nums[i - 1]:
        #             continue
        #         array.append(nums[i])
        #         dfs(nums, i + 1, array)
        #         array.pop()
        #
        # dfs(nums, 0, [])
        # return self.res

        # 2. 递归, 用一个指针表示上次更新的位置
        result = [[]]
        nums.sort()
        start = 1
        for i in range(len(nums)):
            temp = []
            for j in range(len(result)):
                if i > 0 and nums[i] == nums[i - 1] and j < start:
                    continue
                temp.append(result[j] + [nums[i]])
            start = len(result)
            result.extend(temp)
        return result
