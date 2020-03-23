class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # # 1. 暴力遍历，时间复杂度O(n^3)

        # # 2. 对1进行改进，可以只用2重循环，时间复杂度O(n^2)

        # # 3. 遍历数组，记录两个变量，thisSum表示当前子序列和，maxSum表示最大子序列和，时间复杂度O(n)
        # thisSum, maxSum = 0, -float('inf')
        # for num in nums:
        #     thisSum += num
        #     if thisSum > maxSum:
        #         maxSum = thisSum
        #     if thisSum < 0:
        #         thisSum = 0
        # return maxSum

        # 4. 动态规划，dp[i] = max(dp[i-1], 0) + nums[i]
        dp = [-float('inf')] * len(nums)
        dp[0] = max(dp[0], nums[0])
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], 0) + nums[i]
        return max(dp)

# class Solution(object):
#     def maxSubArray(self, nums):
#         # 5. 分治法，最大子序和要么在左半部分，要么在右半部分，要么横跨中间元素。
#         # 左半部分和右半部分都可以递归解决，横跨中间的元素只需要向左找到最大连续值，向右找到最大连续值，加起来即可。
#         left = 0
#         right = len(nums)-1
#         maxSum = self.divide(nums,left,right)
#         return maxSum

#     def divide(self,nums,left,right):
#         if left == right:
#             return nums[left]
#         center = (left+right) // 2
#         leftMaxSum = self.divide(nums,left,center)
#         rightMaxSum = self.divide(nums,center+1,right)

#         # 最快情况下，左右元素皆小于0，那么最大元素就是center元素
#         leftBorderSum = nums[center]
#         leftSum = nums[center]
#         for i in range(center-1,left-1,-1):
#             leftSum += nums[i]
#             if leftSum>leftBorderSum:
#                 leftBorderSum = leftSum
#         rightBorderSum = nums[center+1]
#         rightSum = nums[center+1]
#         for i in range(center+2,right+1):
#             rightSum += nums[i]
#             if rightSum>rightBorderSum:
#                 rightBorderSum = rightSum
#         BorderSum = leftBorderSum + rightBorderSum

#         return max(leftMaxSum,rightMaxSum,BorderSum)