class Solution(object):
    def permuteUnique(self, nums):
        # 1. 在46题的基础上用set去重
        self.res = set()
        check = [0] * len(nums)

        def calcPermute(nums, index, nowArray, check):
            if index == len(nums):
                self.res.add(tuple(nowArray.copy()))
                return
            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                check[i] = 1
                nowArray.append(nums[i])
                calcPermute(nums, index + 1, nowArray, check)
                nowArray.pop()
                check[i] = 0

        calcPermute(nums, 0, [], check)
        return list(self.res)

        # 2. 不借助set，在回溯的时候剪枝
