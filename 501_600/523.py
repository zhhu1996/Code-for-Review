class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """连续的子数组和
        1. 前缀和
        用字典存储前缀和, key为前缀和s[i]%k, value是第一次出现的位置
        """
        n = len(nums)
        dp = [0 for i in range(1+n)]
        index_map = {0:0}
        for i in range(n):
            dp[i+1] = dp[i] + nums[i]
            if dp[i+1] % k in index_map and i+1-index_map[dp[i+1] % k] >= 2:
                return True
            if dp[i+1] % k not in index_map:
                index_map[dp[i+1] % k] = i+1
        return False