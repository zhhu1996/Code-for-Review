class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # # 1. 暴力解，时间复杂度O(n^3)，超时

        # 2. 先对序列排序。因为要找三个数，每次遍历固定起始元素，然后根据三数之和调整其他两个数的位置。时间复杂度O(n^2)
        # 注意，找到=0的值时需要判断左界和右界是否和下一位置重复
        # 另外，也可以用集合去重
        if not nums or len(nums)<3:
            return []

        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0: # 剪枝加速
                return res
            if i > 0 and nums[i] == nums[i-1]: # 去重逻辑
                continue
            L = i+1
            R = len(nums)-1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    R -= 1
                    L += 1
                elif nums[i] + nums[L] + nums[R] < 0:
                    L += 1
                else:
                    R -= 1

        return res

        # # 3. 先排序，然后将3数之和转换为2数之和的子问题
        # n = len(nums)
        # if n < 3:
        #     return []
        #
        # nums.sort()
        #
        # ret = set()
        # for i in range(n):
        #     # nums[i] 为正数，表示后面不可能有两数之后为负
        #     if nums[i] > 0:
        #         break
        #     # 跳过相等的元素
        #     if i >= 1 and nums[i] == nums[i - 1]:
        #         continue
        #     # 寻找3数之和相等
        #     ll = self.twoSum(nums, -nums[i], i + 1, n - 1)
        #     if ll == set():
        #         continue
        #     ret = ret | ll
        # return list(ret)

    def twoSum(self, nums, target, l, r):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        n = len(nums[l: r + 1])
        if n < 2:
            return set()

        start = nums[l - 1]
        dict1 = dict()
        ret = set()
        for i in range(l, r + 1):
            other = target - nums[i]
            if other in dict1:
                # list无法被加入set
                ret.add((start, other, nums[i]))
            dict1[nums[i]] = i

        return ret