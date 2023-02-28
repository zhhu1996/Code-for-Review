class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """等差数列划分 II - 子序列
        1. 带维度的单串dp
        dp[i][s]表示以位置i结尾, 差为s, 长度>=2的等差序列个数, 由于差有限, 为了节省空间, 只需存储存在的数列即可
        """
        from collections import defaultdict
        n = len(nums)
        if n <= 2:
            return 0
        dp = [defaultdict(int) for i in range(n)]
        dp[1][nums[1]-nums[0]] = 1
        res = 0
        for i in range(2, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
        for i in range(n):
            for k in dp[i]:
                res += dp[i][k]
        res = res - n*(n-1)//2
        return res