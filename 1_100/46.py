class Solution(object):
    def permute(self, nums):
        # # 1. 遍历生成
        # self.res = []
        #
        # def calcPermute(nums, index, nowArray):
        #     if len(nums) == index:
        #         self.res.append(nowArray.copy())
        #         return
        #     for i in range(len(nums)):
        #         if nums[i] in nowArray:
        #             continue
        #         nowArray.append(nums[i])
        #         calcPermute(nums, index + 1, nowArray)
        #         nowArray.pop()
        #
        # calcPermute(nums, 0, [])
        # return self.res

        # # 2. 回溯交换
        # self.res = []
        #
        # def calcPermute(nums, index):
        #     if index == len(nums):
        #         self.res.append(nums.copy())
        #         return
        #     for i in range(index, len(nums)):
        #         nums[index], nums[i] = nums[i], nums[index]
        #         calcPermute(nums, index + 1)
        #         nums[index], nums[i] = nums[i], nums[index]
        #
        # calcPermute(nums, 0)
        # return self.res

        # 3. 方法1的另一种判断数组中的元素是否使用过的方法
        self.res = []
        check = [0] * len(nums)

        def calcPermute(nums, index, nowArray, check):
            if index == len(nums):
                self.res.append(nowArray.copy())
                return
            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                check[i] = 1
                nowArray.append(nums[i])
                calcPermute(nums, index+1, nowArray, check)
                nowArray.pop()
                check[i] = 0

        calcPermute(nums, 0, [], check)
        return self.res

        # # 4. 库函数itertools.permutations
        # from itertools import permutations
        # return list(permutations(nums, len(nums))) 




