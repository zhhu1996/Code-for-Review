class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        """和等于 k 的最长子数组长度
        1. 前缀和, 时间与空间复杂度都是O(n)
        将前缀和s[i]存入map中, key是前缀和s[i], 因为要求最长子数组, 所以value记录第一次出现时的索引
        更新前缀和时判断s[i]-k是否存在
        """
        n = len(nums)
        dp = [0 for i in range(1+n)]
        index_map = {0: 0} # dp[i+1]==k
        max_len = 0
        for i in range(n):
            dp[i+1] = dp[i] + nums[i]
            if dp[i+1] - k in index_map:
                max_len = max(max_len, i+1-index_map[dp[i+1]-k])
            if dp[i+1] not in index_map:
                index_map[dp[i+1]] = i+1
        return max_len
