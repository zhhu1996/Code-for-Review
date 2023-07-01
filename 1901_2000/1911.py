class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        """最大子序列交替和 (同买卖股票)
        1. dp
        带维度单串, 位置i可不取, O(1)个子问题
        f[i][0] = 前i个元素长为偶数的最大交替和, f[i][1] = 前i个元素长为奇数的最大交替和
        """
        n = len(nums)
        f = [[0, 0] for i in range(n+1)]
        f[0][0], f[0][1] = 0, -float('inf')
        for i in range(1, n+1):
            f[i][0] = max(f[i-1][0], f[i-1][1] - nums[i-1])
            f[i][1] = max(f[i-1][1], f[i-1][0] + nums[i-1])
        return max(f[n][0], f[n][1])