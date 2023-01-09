class Solution(object):
    def permuteUnique(self, nums):
        # # 1. 在46题的基础上用set去重
        # self.res = set()
        # check = [0] * len(nums)
        #
        # def calcPermute(nums, index, nowArray, check):
        #     if index == len(nums):
        #         self.res.add(tuple(nowArray.copy()))
        #         return
        #     for i in range(len(nums)):
        #         if check[i] == 1:
        #             continue
        #         check[i] = 1
        #         nowArray.append(nums[i])
        #         calcPermute(nums, index + 1, nowArray, check)
        #         nowArray.pop()
        #         check[i] = 0
        #
        # calcPermute(nums, 0, [], check)
        # return list(self.res)

        # 2. 不借助set，在回溯的时候剪枝，剪枝条件为：和前一个元素值相同（此处隐含这个元素的index>0），并且前一个元素还没有被使用过
        self.res = []
        check = [0] * len(nums)
        nums.sort()

        def calcPermute(nums, index, nowArray, check):
            if index == len(nums):
                self.res.append(nowArray.copy())
                return
            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i-1] and check[i-1] == 0:
                    continue
                check[i] = 1
                nowArray.append(nums[i])
                calcPermute(nums, index + 1, nowArray, check)
                nowArray.pop()
                check[i] = 0

        calcPermute(nums, 0, [], check)
        return self.res


q47 = Solution()
for ll in q47.permuteUnique([1,2,3,4]):
    print(ll)