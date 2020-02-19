class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. 暴力遍历，时间复杂度O(n^2)
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # 2.两遍hash法
        data = {}
        for k, v in enumerate(nums):
            data[v] = k
        for k, v in enumerate(nums):
            if target - v in data and data[target - v] != k:
                return [k, data[target - v]]

        # 3. hash表, key代表元素的大小，value代表与key之和==target的元素的索引，时间O(n)，空间O(n)
        # data = {}
        # for k, v in enumerate(nums):
        #     if v in data:
        #         return [data[v], k]
        #     else:
        #         data[target-v] = k